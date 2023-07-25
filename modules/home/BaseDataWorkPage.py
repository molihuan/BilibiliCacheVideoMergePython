import os

# 数据获取抽象窗口
from PySide6.QtWidgets import QWidget
# 这里可能有循环依赖的问题注意全包名
from modules.framework.manager.ConfigManager import ConfigKey
from modules.home.init.DataManager import DataManager
from modules.home.ui_WorkPage import Ui_WorkPageWidget
from modules.utils.PathUtils import PathUtils


class BaseDataWorkPage(QWidget):
    def __init__(self, configManager):
        super().__init__()
        self.ConfigManager = configManager
        # 加载界面文件绑定在BilibiliCacheVideoMergePython.pyproject中配置
        self.ui = Ui_WorkPageWidget()
        # 加载视图
        self.ui.setupUi(self)
        self.initDataManager()

    # 关闭之前调用
    def closeEvent(self, event):
        # 在窗口关闭之前执行自定义方法
        self.saveConfigData()
        self.closeSubWindow()
        # 调用父类的closeEvent方法，实现正常的窗口关闭行为
        super().closeEvent(event)

    # 关闭子窗口
    def closeSubWindow(self):
        # if self.SettingsView:
        #     self.SettingsView.close()
        # if self.AboutView:
        #     self.AboutView.close()
        pass

    # 获取配置路径字典
    def getConfigPathDict(self):
        allPath = {
            "SelfPath": PathUtils.getcwd(),
            ConfigKey.CACHE_PATH: self.getCachePath(),
            ConfigKey.COMPLETE_PATH: self.getCompletePath(),
        }
        return allPath

    # 保存配置数据
    def saveConfigData(self):
        # 创建要写入的数据
        configJson = {
            # ConfigKey.SYS_FFMPEG_PATH: self.getSysFFmpegPath(),
            ConfigKey.CACHE_PATH: self.getCachePath(),
            # ConfigKey.COMPLETE_PATH: self.getCompletePath()
        }
        self.ConfigManager.updateByDict(configJson)
        self.ConfigManager.save()

    def initDataManager(self):
        self.DataManager = DataManager(self)

    def getSelfPath(self) -> str:
        return self.DataManager.selfPath

    def setSelfPath(self, value: str):
        self.DataManager.selfPath = value

    def getCachePath(self) -> str:
        return self.DataManager.cachePath

    def setCachePath(self, value: str):
        self.DataManager.cachePath = value

    def getCompletePath(self) -> str:
        return self.DataManager.completePath

    def setCompletePath(self, value: str):
        self.DataManager.completePath = value

    def getConfigJsonPath(self) -> str:
        return self.DataManager.configJsonPath

    def setConfigJsonPath(self, value: str):
        self.DataManager.configJsonPath = value

    def getSysFFmpegPath(self) -> str:
        return self.DataManager.sysFFmpegPath

    def setSysFFmpegPath(self, value: str):
        self.DataManager.sysFFmpegPath = value

    def getCacheFileTpye(self):
        return self.DataManager.cacheFileTpye

    def setCacheFileTpye(self, value):
        self.DataManager.cacheFileTpye = value
