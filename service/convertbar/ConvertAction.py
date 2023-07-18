import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QMessageBox

from service.base.QDataMainWindow import QDataMainWindow
from service.convertbar.BaseAction import BaseAction
from service.dataarea.DataShowManage import DataShowManage
from utils.FFmpegUtils import FFmpegUtils
from utils.FileUtils import FileUtils
from utils.StrUtils import StrUtils
from views.FFmpegProgressDialog import FFmpegProgressDialog


class ConvertAction(BaseAction):
    def __init__(self, context):
        super().__init__(context)

    def setConnect(self, context: QMainWindow):
        ui = self.getUI()
        ui.mergeBtn.clicked.connect(self.handleMerge)

    # 处理合并按钮
    def handleMerge(self):
        context: QDataMainWindow = self.getContext()
        allPath = context.getConfigPathDict()
        # 检查路径是否有空格
        if not StrUtils.isPathConforms(context, allPath):
            return

        manage: DataShowManage = context.DataShowManage

        # 如果是合集页面需要做更多的处理
        selectedList = self.collection2ChapterList(manage)
        # 创建进度弹窗
        if not context.FFmpegProgressDialog:
            # 实例化窗口
            context.FFmpegProgressDialog = FFmpegProgressDialog(context)
        context.FFmpegProgressDialog.setWindowModality(Qt.ApplicationModal)  # 设置窗口二为模态窗口
        context.FFmpegProgressDialog.show()

        total_commands = len(selectedList)
        progress_step = 100 / total_commands
        progress_value = 0

        for cacheInfo in selectedList:
            # 进度框点击取消
            if context.FFmpegProgressDialog.cancelled:
                break

            # cacheInfo里面的路径为空判断
            needPath = {
                cacheInfo.getAudioPath(): cacheInfo.getPath() + "下audio.m4s文件路径",
                cacheInfo.getVideoPath(): cacheInfo.getPath() + "下video.m4s文件路径"
            }
            if not StrUtils.isPathConforms(context, needPath):
                continue

            # 组合输出文件夹
            outputDirPath = os.path.join(context.getCompletePath(), cacheInfo.getDirName())
            if not os.path.exists(outputDirPath):
                os.makedirs(outputDirPath)
            # 组合输出全路径
            outputAllPath = os.path.join(outputDirPath, cacheInfo.getTitle() + ".mp4")

            if os.path.exists(outputAllPath):
                reply = QMessageBox.question(None, "覆盖确认", f"文件 {outputAllPath} 已经存在，是否覆盖？",
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if reply == QMessageBox.StandardButton.Yes:
                    run_result = FFmpegUtils.runCommand(context, cacheInfo, outputAllPath, True)
                    continue
                elif reply == QMessageBox.StandardButton.No:
                    # 重命名输出的文件名并执行合并命令
                    outputAllPath = FileUtils.getUniqueFileName(outputAllPath)

            run_result = FFmpegUtils.runCommand(context, cacheInfo, outputAllPath)

            # 更新进度
            progress_value += progress_step
            context.FFmpegProgressDialog.setProgress(progress_value)
        context.FFmpegProgressDialog.close()
