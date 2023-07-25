import os

from modules.home.base.BaseService import BaseService
from modules.home.dataarea.DataShowManager import DataShowManager
from modules.utils.FileUtils import FileUtils
from modules.utils.JsonUtils import JsonUtils
from modules.utils.Log import Log


class BaseAction(BaseService):
    def __init__(self, mContext):
        super().__init__(mContext)

    # 集合列表转章节列表 并去除缺少重要文件的元素
    def collection2ChapterList(self, manage: DataShowManager):

        totalCacheDirCount = 0
        # 如果是合集页面需要做更多的处理
        if manage.isCollectionPage():
            newSelectedCacheList = []
            for item in manage.selectedCacheList:
                # 获取合集里的章节路径
                chapterPathList = manage.getAllChapterPathByCollection(item.getPath())
                for ite in chapterPathList:
                    totalCacheDirCount += 1
                    # 通过章节路径获取缓存信息
                    info = manage.getCacheInfoByPhone(ite)
                    blvList = info.getBlvPathList()
                    audioPath = info.getAudioPath()
                    videoPath = info.getVideoPath()

                    if (audioPath is None) or (videoPath is None):
                        if blvList is None:
                            continue
                    json = JsonUtils.parseJson(info)
                    info.setPath(os.path.dirname(ite))
                    info.setSubTitle(json.get_subTitle())
                    info.setTitle(json.get_title())
                    newSelectedCacheList.append(info)

            return totalCacheDirCount, newSelectedCacheList
        else:
            for info in manage.selectedCacheList:
                totalCacheDirCount += 1
                blvList = info.getBlvPathList()
                audioPath = info.getAudioPath()
                videoPath = info.getVideoPath()

                if (audioPath is None) or (videoPath is None):
                    if blvList is None:
                        manage.selectedCacheList.remove(info)
            return totalCacheDirCount, manage.selectedCacheList

    def fixM4s(self, cacheInfo):
        path = cacheInfo.getPath()
        audio_path = cacheInfo.getAudioPath()
        video_path = cacheInfo.getVideoPath()
        hlbAudio = os.path.join(path, "hlbAudio.mp3")
        hlbVideo = os.path.join(path, "hlbVideo.mp4")
        try:
            FileUtils.decryptM4s(audio_path, hlbAudio)
            FileUtils.decryptM4s(video_path, hlbVideo)
        except Exception as e:
            Log.i("fixM4s解密失败")

        cacheInfo.setAudioPath(hlbAudio)
        cacheInfo.setVideoPath(hlbVideo)
        Log.i(cacheInfo)
