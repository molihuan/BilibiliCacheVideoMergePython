import os
from enum import Enum

from PySide6.QtCore import QDir, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QFileDialog

from entity.CacheInfo import CacheInfo
from utils.SysUtils import SysUtils, SysType


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
        for item in os.listdir(parentPath):
            item_path = os.path.join(parentPath, item)
            if os.path.isdir(item_path):
                subfolders.append(item_path)
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

    @staticmethod
    # 校验缓存文件完整性
    def verifyCacheFileComplete(cacheInfo: CacheInfo):
        stateList = []
        audioPath = cacheInfo.getAudioPath()
        videoPath = cacheInfo.getVideoPath()
        jsonPath = cacheInfo.getJsonPath()
        danmakuPath = cacheInfo.getDanmakuPath()
        if not isinstance(audioPath, str):
            stateList.append(CacheCompleteState.AUDIODELETION)
        if not isinstance(videoPath, str):
            stateList.append(CacheCompleteState.VIDEODELETION)
        if not isinstance(jsonPath, str):
            stateList.append(CacheCompleteState.JSONDELETION)
        if not isinstance(danmakuPath, str):
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
