import requests
import json
from datetime import datetime
import uuid
import os
import time
f = open('chapter.json', encoding='utf8')
chapter_data = json.load(f)
count = 0
image_list = []
for chapter in chapter_data:
    os.system("cls")
    count += 1
    print(chapter.get("_id"))
    print(f"{count}/{len(chapter_data)}")
    try:
        manga_chapter_url = f"https://api.mangadex.org/at-home/server/{chapter.get('_id')}"
        r = requests.get(url=manga_chapter_url)
        time.sleep(1)
        base_url = r.json().get("baseUrl")
        chapter_image = r.json().get("chapter")
        page = 0
        for file in chapter_image.get("dataSaver"):
            page += 1
            image_url = f"https://uploads.mangadex.org/data-saver/{chapter_image.get('hash')}/{file}"
            image_data = {
                "_id": str(uuid.uuid4()),
                "chapter_id": chapter.get('_id'),
                "page": page,
                "image_url": image_url,
                "_created": str(datetime.now()),
                "_deleted": None,
                "_updated": str(datetime.now()),
                "_updater": None,
            }
            image_list.append(image_data)
    except:
        continue
with open('chapter_image.json', 'w', encoding='utf-8') as f:
    json.dump(image_list, f, ensure_ascii=False, indent=4)
