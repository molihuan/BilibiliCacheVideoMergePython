import json
import os

from PySide6.QtWidgets import QMainWindow

from service.init.DataManager import DataManager
from ui_main import Ui_MainWindow


# 数据获取抽象窗口
class QDataMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 加载界面文件绑定在BilibiliCacheVideoMergePython.pyproject中配置
        self.ui = Ui_MainWindow()
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
        if self.SettingsView:
            self.SettingsView.close()
        if self.AboutView:
            self.AboutView.close()

    # 获取配置路径字典
    def getConfigPathDict(self):
        allPath = {
            os.getcwd(): "软件路径",
            self.getCachePath(): "缓存路径",
            self.getCompletePath(): "合并完成路径"
        }
        return allPath

    # 保存配置数据
    def saveConfigData(self):
        # 创建要写入的数据
        configJson = {
            'sysFFmpegPath': self.getSysFFmpegPath(),
            'cachePath': self.getCachePath(),
            'completePath': self.getCompletePath()
        }
        # 将数据写入到config.json文件中
        with open(self.getConfigJsonPath(), 'w') as file:
            json.dump(configJson, file, indent=4)

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
