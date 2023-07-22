import json
import os
import random
import re
import string
import time

from modules.entity.CacheInfo import CacheInfo
from modules.entity.JsonInfo import JsonInfo

# 去除一些特殊的字符的正则表达式 /r去换行
SPECIAL_CHARACTERS_REGULAR_RULE = "[\t\r\n`~!@#$%^&*()+=|{}':;',\\[\\].<>/?~！_@#￥%……&*·（）\\\\——+|{}【】 ️ 《》\"‘；：”“’。， 、？-]*"


class JsonUtils:

    @staticmethod
    def parseJson(cacheInfo: CacheInfo) -> JsonInfo:
        jsonPath = cacheInfo.getJsonPath()
        if jsonPath is None:
            return JsonUtils.getUUIDJson()
        else:
            return JsonUtils.parseJsonByPath(cacheInfo.getJsonPath())

    @staticmethod
    def parseJsonByPath(file_path: str) -> JsonInfo:
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

            if "groupTitle" in data:
                title = data["groupTitle"]
                isGetTitle = True

            if "groupId" in data:
                temp = data["groupId"]
                if not isGetTitle:
                    title = temp
                    isGetTitle = True

            if "title" in data:
                temp = data["title"]
                if isGetTitle:
                    subTitle = temp
                    isGetSubTitle = True
                    pass
                else:
                    title = temp
                    isGetTitle = True

            if "tabName" in data:
                temp = data["tabName"]
                if isGetSubTitle:
                    pass
                else:
                    subTitle = temp
                    isGetSubTitle = True

            if "bvid" in data:
                bvid = data["bvid"]

                title = title if isGetTitle else bvid
                isGetTitle = True

            if "avid" in data:
                avid = data["avid"]

                title = title if isGetTitle else avid
                isGetTitle = True

            if "page_data" in data:
                # 普通视频
                if "download_subtitle" in data["page_data"]:
                    download_subtitle = data["page_data"]["download_subtitle"]

                    subTitle = subTitle if isGetSubTitle else download_subtitle
                    subTitle = subTitle.replace(title, '')
                    isGetSubTitle = True

                if "part" in data["page_data"]:
                    part = data["page_data"]["part"]

                    subTitle = subTitle if isGetSubTitle else part
                    subTitle = subTitle.replace(title, '')
                    isGetSubTitle = True

                if "page" in data["page_data"]:
                    page = data["page_data"]["page"]
                    subTitle = subTitle if isGetSubTitle else page
                    isGetSubTitle = True

                if "cid" in data["page_data"]:
                    cid = data["page_data"]["cid"]
                    subTitle = subTitle if isGetSubTitle else cid
                    isGetSubTitle = True
            elif "ep" in data:
                # 番剧视频
                if "index_title" in data["ep"]:
                    index_title = data["ep"]["index_title"]
                    subTitle = subTitle if isGetSubTitle else index_title
                    isGetSubTitle = True

                if "index" in data["ep"]:
                    index = data["ep"]["index"]
                    subTitle = subTitle if isGetSubTitle else index
                    isGetSubTitle = True

            if "coverPath" in data:
                cover = data["coverPath"]

            if "cover" in data and cover is None:
                cover = data["cover"]

            # 去除特殊字符还有空格
            if isGetTitle:
                title = re.sub(SPECIAL_CHARACTERS_REGULAR_RULE, '', title)
            else:
                title = JsonUtils.generate_short_id()

            if isGetSubTitle:
                subTitle = re.sub(SPECIAL_CHARACTERS_REGULAR_RULE, '', subTitle)
            else:
                subTitle = JsonUtils.generate_short_id()
            
            return JsonInfo(title, subTitle, bvid, avid, cid, cover)

        except json.JSONDecodeError as e:
            print(f"JSON decoding error: {e}")
            return JsonUtils.getUUIDJson()

    @staticmethod
    def generate_short_id():
        timestamp = str(int(time.time() * 1000))
        random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        short_id = timestamp + random_chars
        return short_id

    @staticmethod
    def getUUIDJson():
        shortId = JsonUtils.generate_short_id()
        title = shortId
        subTitle = shortId
        json_info = JsonInfo(title, subTitle)
        return json_info


if __name__ == "__main__":
    title = "咬人猫x咬人喵胭脂❤️我的姐姐不可能这么撩人国风单曲"
    title = re.sub(SPECIAL_CHARACTERS_REGULAR_RULE, '', title)

    print(title)
