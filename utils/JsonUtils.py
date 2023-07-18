import json
import os
import random
import re
import string
import time

from entity.JsonInfo import JsonInfo


class JsonUtils:
    @staticmethod
    def generate_short_id():
        timestamp = str(int(time.time() * 1000))
        random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        short_id = timestamp + random_chars
        return short_id

    @staticmethod
    def parse_json(file_path: str):

        global title, subTitle, bvid, avid, cid, cover
        if not os.path.exists(file_path):
            return JsonUtils.getUUIDJson()
        try:
            with open(file_path, encoding='utf-8') as f:
                data = json.load(f)

            isGetTitle = False
            isGetSubTitle = False
            bvid = None
            avid = None
            cid = None
            cover = None

            if "title" in data:
                title = data["title"]
                isGetTitle = True

            if "bvid" in data:
                bvid = data["bvid"]

                title = title if isGetTitle else bvid
                isGetTitle = True

            if "avid" in data:
                avid = data["avid"]

                title = title if isGetTitle else avid
                isGetTitle = True

            if "page_data" in data and "download_subtitle" in data["page_data"]:
                download_subtitle = data["page_data"]["download_subtitle"]

                subTitle = subTitle if isGetSubTitle else download_subtitle
                subTitle = subTitle.replace(title, '')
                isGetSubTitle = True

            if "page_data" in data and "part" in data["page_data"]:
                part = data["page_data"]["part"]

                subTitle = subTitle if isGetSubTitle else part
                subTitle = subTitle.replace(title, '')
                isGetSubTitle = True

            if "page_data" in data and "page" in data["page_data"]:
                page = data["page_data"]["page"]
                subTitle = subTitle if isGetSubTitle else page
                isGetSubTitle = True

            if "page_data" in data and "cid" in data["page_data"]:
                cid = data["page_data"]["cid"]
                subTitle = subTitle if isGetSubTitle else cid
                isGetSubTitle = True

            if "cover" in data:
                cover = data["cover"]

            if isGetTitle:
                title = re.sub(r'\s', '', title)
            else:
                title = JsonUtils.generate_short_id()
                
            if isGetSubTitle:
                subTitle = re.sub(r'\s', '', subTitle)
            else:
                subTitle = JsonUtils.generate_short_id()

            return JsonInfo(title, subTitle, bvid, avid, cid, cover)

        except json.JSONDecodeError as e:
            print(f"JSON decoding error: {e}")
            return JsonUtils.getUUIDJson()

    @staticmethod
    def getUUIDJson():
        shortId = JsonUtils.generate_short_id()
        title = shortId
        subTitle = shortId
        json_info = JsonInfo(title, subTitle)
        return json_info
