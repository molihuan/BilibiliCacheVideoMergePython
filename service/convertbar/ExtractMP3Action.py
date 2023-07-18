import os
import shutil

from PySide6.QtWidgets import QMainWindow, QMessageBox

from service.base.QDataMainWindow import QDataMainWindow
from service.convertbar.BaseAction import BaseAction
from service.dataarea.DataShowManage import DataShowManage


class ExtractMP3Action(BaseAction):
    def __init__(self, context):
        super().__init__(context)

    def setConnect(self, context: QMainWindow):
        ui = self.getUI()
        ui.getMP3Btn.clicked.connect(self.handleExtractMP3)

    # 提取mp3按钮
    def handleExtractMP3(self):
        context: QDataMainWindow = self.getContext()
        manage: DataShowManage = context.DataShowManage
        # 获取勾选的列表
        selectedList = self.collection2ChapterList(manage)

        for cacheInfo in selectedList:
            # self.startExtractMP3(context, cacheInfo)
            # 组合输出文件夹
            outputDirPath = os.path.join(context.getCompletePath(), cacheInfo.getDirName())
            if not os.path.exists(outputDirPath):
                os.makedirs(outputDirPath)

            # 组合输出全路径
            outputAllPath = os.path.join(outputDirPath, cacheInfo.getTitle() + ".mp3")
            if os.path.exists(outputAllPath):

                reply = QMessageBox.question(None, "覆盖确认", f"文件 {outputAllPath} 已经存在，是否覆盖？",
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if reply == QMessageBox.StandardButton.No:
                    continue

            shutil.copy(cacheInfo.getAudioPath(), outputAllPath)
