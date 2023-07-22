import os
from enum import Enum

from PySide6.QtCore import QDir, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QFileDialog

from modules.entity.CacheInfo import CacheInfo
from modules.utils.StrUtils import StrUtils
from modules.utils.SysUtils import SysUtils, SysType


class CacheCompleteState(Enum):
    COMPLETE = 0
    AUDIODELETION = 1
    VIDEODELETION = 2
    JSONDELETION = 3
    DANMAKUDELETION = 4


class PathUtils():
    # 获取子目录的文件夹
    @staticmethod
    def listSubDir(parentPath: str):
        subfolders = []
        if parentPath == '':
            return subfolders
        try:
            for item in os.listdir(parentPath):
                item_path = os.path.join(parentPath, item)
                if os.path.isdir(item_path):
                    subfolders.append(item_path)
        except FileNotFoundError as e:
            
            pass
        return subfolders

    # 获取子目录的文件
    @staticmethod
    def listSubFile(parentPath):
        subfiles = []
        for item in os.listdir(parentPath):
            item_path = os.path.join(parentPath, item)
            if os.path.isfile(item_path):
                subfiles.append(item_path)
        return subfiles

    """
                if CacheCompleteState.AUDIODELETION in status or CacheCompleteState.VIDEODELETION in status:
                print(f"粗略检查文件夹:{item}\n------缺少audio.m4s或video.m4s文件")
                if CacheCompleteState.JSONDELETION in status:
                    print(f"粗略检查文件夹:{item}\n------缺少entry.json文件")
                    json_info = JsonUtils.getUUIDJson()
                else:
                    # 解析json
                    json_info = JsonUtils.parse_json(info.getJsonPath())
            elif CacheCompleteState.JSONDELETION in status:
                print(f"粗略检查文件夹:{item}\n------缺少entry.json文件")
                json_info = JsonUtils.getUUIDJson()
            else:
                json_info = JsonUtils.parse_json(info.getJsonPath())
    
    """

    @staticmethod
    # 校验缓存文件完整性
    def verifyCacheFileComplete(cacheInfo: CacheInfo):
        stateList = []
        audioPath = cacheInfo.getAudioPath()
        videoPath = cacheInfo.getVideoPath()
        jsonPath = cacheInfo.getJsonPath()
        danmakuPath = cacheInfo.getDanmakuPath()
        blvPathList = cacheInfo.getBlvPathList()
        if not isinstance(audioPath, str):
            stateList.append(CacheCompleteState.AUDIODELETION)
        if not isinstance(videoPath, str):
            stateList.append(CacheCompleteState.VIDEODELETION)
        if not isinstance(jsonPath, str):
            stateList.append(CacheCompleteState.JSONDELETION)
        if not isinstance(danmakuPath, str):
            stateList.append(CacheCompleteState.DANMAKUDELETION)
        if not blvPathList is None:
            stateList.remove(CacheCompleteState.AUDIODELETION)
            stateList.remove(CacheCompleteState.VIDEODELETION)
            stateList.append(CacheCompleteState.DANMAKUDELETION)

        return stateList

    @staticmethod
    def openPathByFileManager(path):
        url = QUrl.fromLocalFile(path)
        if not os.path.exists(path):
            # 路径不存在，创建路径
            success = QDir().mkpath(path)
        # 路径存在，调用系统文件管理器打开路径
        QDesktopServices.openUrl(url)

    ##打开路径选择器
    # 参数：回调方法、校验码
    @staticmethod
    def openPathSelector(callback, fromCode):
        directory_dialog = QFileDialog()
        directory_dialog.setFileMode(QFileDialog.Directory)
        if directory_dialog.exec_():
            selected_path = directory_dialog.selectedFiles()[0]
            callback(selected_path, fromCode)

    @staticmethod
    def getFFmpegPath():
        # 只判断一次并存入配置文件中，接下来就在配置文件中获取ffmpeg的路径
        sysType = SysUtils.getSysType()

        resPath = PathUtils.getResPath()

        resffmpeg = os.path.join(resPath, "ffmpeg")
        WinFFmpegPath = os.path.join(resffmpeg, "ffmpeg.exe")
        MacFFmpegPath = os.path.join(resffmpeg, "ffmpeg-mac")
        linuxDir = os.path.join(resffmpeg, "ffmpeg-linux")
        linuxFFmpegPath = os.path.join(linuxDir, "ffmpeg")

        if sysType == SysType.WIN:
            return WinFFmpegPath
        elif sysType == SysType.MAC:
            return MacFFmpegPath
        elif sysType == SysType.LINUX:
            return linuxFFmpegPath
        else:
            print("不支持系统")

    @staticmethod
    def getResPath():
        workPath = os.getcwd()
        resPath = os.path.join(workPath, "res")
        return resPath

    @staticmethod
    def getResMdPath():
        resPath = PathUtils.getResPath()
        mdDirPath = os.path.join(resPath, "md")
        return mdDirPath

    @staticmethod
    def isPathConforms(cacheInfo, context, outputAllPath):
        dialog = context.Dialog
        path = cacheInfo.getPath()
        if cacheInfo.getBlvPathList() is None:
            # cacheInfo里面的路径是否合规判断

            audioPath = cacheInfo.getAudioPath()
            videoPath = cacheInfo.getVideoPath()

            if audioPath is None or audioPath == "":
                dialog.shows(f"{path}下的音频m4s文件没有找到(大概是audio.m4s没找到)", lambda: dialog.close())
                return False
            if StrUtils.has_whitespace(audioPath):
                dialog.shows(f"({audioPath})中存在空格,请修改:{path}，使其路径中不存在空格,或者移动此文件夹({path})到其他路径中(路径中不能有空格),并重新加载",
                             lambda: dialog.close())
                return False

            if videoPath is None or videoPath == "":
                dialog.shows(f"{path}下的视频m4s文件没有找到(大概是video.m4s没找到)", lambda: dialog.close())
                return False
            if StrUtils.has_whitespace(videoPath):
                dialog.shows(f"({videoPath})中存在空格,请修改:{path}，使其路径中不存在空格,或者移动此文件夹({path})到其他路径中(路径中不能有空格),并重新加载",
                             lambda: dialog.close())
                return False

        else:
            blvPath = cacheInfo.getBlvPathList()[0]

            if blvPath is None or blvPath == "":
                dialog.shows(f"{path}下的.blv文件没有找到", lambda: dialog.close())
                return False
            if StrUtils.has_whitespace(blvPath):
                dialog.shows(f"({blvPath})中存在空格,请修改:{path}，使其路径中不存在空格,或者移动此文件夹({path})到其他路径中(路径中不能有空格),并重新加载",
                             lambda: dialog.close())
                return False

        if outputAllPath is None or outputAllPath == "":
            dialog.shows(f"完成路径(输出路径):{path}为空", lambda: dialog.close())
            return False
        if StrUtils.has_whitespace(outputAllPath):
            dialog.shows(
                f"({outputAllPath})中存在空格,请修改在设置中重新选择完成路径，使其路径中不存在空格,或者移动此文件夹({path})到其他路径中(路径中不能有空格),并重新加载,还是不行请联系开发者",
                lambda: dialog.close())
            return False

        return True

    # 检查路径是否合规
    @staticmethod
    def checkBasePathNullOrWhitespace(context) -> bool:
        dialog = context.Dialog
        self_path = context.getSelfPath()
        cache_path = context.getCachePath()
        complete_path = context.getCompletePath()

        if StrUtils.has_whitespace(self_path):
            dialog.shows(f"软件所在路径中存在空格,请修改:{self_path}，使其路径中不存在空格,或者移动软件到其他路径中(路径中不能有空格)", lambda: dialog.close())
            return False
        if cache_path is None or cache_path == "":
            dialog.shows(f"缓存路径为空", lambda: dialog.close())
            return False
        if StrUtils.has_whitespace(cache_path):
            dialog.shows(f"缓存路径中存在空格,请修改:{cache_path}，使其路径中不存在空格,或者移动此文件夹({cache_path})到其他路径中(路径中不能有空格)",
                         lambda: dialog.close())
            return False

        if complete_path is None or complete_path == "":
            dialog.shows(f"完成路径(输出路径)为空", lambda: dialog.close())
            return False
        if StrUtils.has_whitespace(complete_path):
            dialog.shows(f"完成路径(输出路径)中存在空格,请修改:{complete_path}，使其路径中不存在空格,或者在设置页面中选择新的输出路径(路径中不能有空格)",
                         lambda: dialog.close())
            return False
        return True
