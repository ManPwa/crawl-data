import requests
import json
from datetime import datetime
import os
f = open('manga.json', encoding='utf8')
manga_data = json.load(f)
count = 0
chapter_list = []
for manga in manga_data:
    os.system("cls")
    count += 1
    print(f"{count}/{len(manga_data)}")
    manga_chapter_url = f"https://api.mangadex.org/manga/{manga.get('_id')}/feed?translatedLanguage[]=en&order[chapter]=desc&limit=500"
    r = requests.get(url=manga_chapter_url)
    data = r.json().get("data")
    for chapter in data:
        chapter_attributes = chapter.get("attributes")
        chapter_data = {
            "_id": chapter.get("id"),
            "manga_id": manga.get('_id'),
            "chapter": chapter_attributes.get("chapter"),
            "title": chapter_attributes.get("title"),
            "volumne": chapter_attributes.get("volumne"),
            "pages": chapter_attributes.get("pages"),
            "_created": chapter_attributes.get("createdAt"),
            "_deleted": None,
            "_updated": str(datetime.now()),
            "_updater": None,
        }
        chapter_list.append(chapter_data)
with open('chapter.json', 'w', encoding='utf-8') as f:
    json.dump(chapter_list, f, ensure_ascii=False, indent=4)
