import requests
from datetime import datetime
import json
manga_url = 'https://api.mangadex.org/manga?includes[]=cover_art&includes[]=author&order[followedCount]=desc&contentRating[]=safe&limit=100&offset='
manga = []
for i in range(0, 2):
    r = requests.get(url=f"{manga_url}{i*100}")
    for data in r.json().get("data"):
        data_attribute = data.get("attributes")
        title = data_attribute.get("title")
        relationships = data.get("relationships")
        author = []
        cover_art_url = ""
        for relationship in relationships:
            if relationship.get("type") == "author":
                author.append(relationship.get("attributes").get("name"))
            if relationship.get("type") == "cover_art":
                cover_file_name = relationship.get(
                    "attributes").get("fileName")
                cover_art_url = f"https://uploads.mangadex.org/covers/{data.get('id')}/{cover_file_name}.256.jpg"
        tags = data_attribute.get("tags")
        tag_list = []
        for tag in tags:
            tag_list.append(tag.get("attributes").get("name").get("en"))
        manga_data = {
            "_id": data.get("id"),
            "title": title.get("ja-ro") or title.get("en"),
            "description": data_attribute.get("description").get("en"),
            "year": data_attribute.get("year"),
            "status": data_attribute.get("status"),
            "demographic": data_attribute.get("publicationDemographic"),
            "cover_art_url": cover_art_url,
            "author": ', '.join(author),
            "tags": tag_list,
            "original_language": data_attribute.get("originalLanguage"),
            "_deleted": None,
            "_updated": str(datetime.now()),
            "_updater": None,
            "_created": data_attribute.get("createdAt")
        }
        manga.append(manga_data)
with open('manga.json', 'w', encoding='utf-8') as f:
    json.dump(manga, f, ensure_ascii=False, indent=4)
