import os

from service.base.BaseService import BaseService
from service.dataarea.DataShowManage import DataShowManage
from utils.JsonUtils import JsonUtils
from utils.PathUtils import PathUtils, CacheCompleteState


class BaseAction(BaseService):
    def __init__(self, context):
        super().__init__(context)

    # 集合列表转章节列表 如果已经是章节列表则直接返回
    def collection2ChapterList(self, manage: DataShowManage):
        # 如果是合集页面需要做更多的处理
        if manage.isCollectionPage():
            newSelectedCacheList = []
            for item in manage.selectedCacheList:
                # 获取合集里的章节路径
                chapterPathList = manage.getAllChapterPathByCollection(item.getPath())
                for ite in chapterPathList:
                    # 通过章节路径获取缓存信息
                    info = manage.getCacheInfo(ite)
                    status = PathUtils.verifyCacheFileComplete(info)

                    if CacheCompleteState.AUDIODELETION in status or CacheCompleteState.VIDEODELETION in status:
                        print(f"详细检查文件夹:{item}\n------缺少audio.m4s或video.m4s文件")
                        
                    elif CacheCompleteState.JSONDELETION in status:
                        print(f"粗略检查文件夹:{item}\n------缺少entry.json文件")
                        json_info = JsonUtils.getUUIDJson()
                    else:
                        json_info = JsonUtils.parse_json(info.getJsonPath())

                    info.setPath(os.path.dirname(ite))

                    info.setTitle(json_info.get_subTitle())
                    info.setDirName(json_info.get_title())

                    info.setChecked(False)

                    newSelectedCacheList.append(info)
            return newSelectedCacheList
        else:
            return manage.selectedCacheList
