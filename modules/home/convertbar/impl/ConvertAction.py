import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QMessageBox

from modules.home.convertbar.BaseAction import BaseAction
from modules.home.dataarea.DataShowManager import DataShowManager, CacheFileTpye
from modules.home.dialogs.impl.FFmpegProgressDialog import FFmpegProgressDialog
from modules.utils.FFmpegUtils import FFmpegUtils
from modules.utils.FileUtils import FileUtils
from modules.utils.PathUtils import PathUtils


class ConvertAction(BaseAction):
    def __init__(self, mContext):
        super().__init__(mContext)

    def setConnect(self, context: QMainWindow):
        ui = self.getUI()
        ui.mergeBtn.clicked.connect(self.handleMerge)

    # 处理合并按钮
    def handleMerge(self):
        context = self.getContext()
        # 检查基础是否有空格
        if not PathUtils.checkBasePathNullOrWhitespace(context):
            return

        manage: DataShowManager = context.DataShowManage

        # 勾选的cache数量
        # 如果是合集页面需要做更多的处理
        totalSelectCacheDirCount, selectedList = self.collection2ChapterList(manage)
        # 有效的缓存数量
        effectiveCacheDirCount = len(selectedList)

        if(effectiveCacheDirCount==0):
            QMessageBox.question(None, "提示", f"你还没有勾选",QMessageBox.StandardButton.Ok)
            return

        progress_step = 100 / effectiveCacheDirCount
        progress_value = 0

        # 创建进度弹窗
        if not context.FFmpegProgressDialog:
            # 实例化窗口
            context.FFmpegProgressDialog = FFmpegProgressDialog(context)
        context.FFmpegProgressDialog.setCacheDirCount(totalSelectCacheDirCount, effectiveCacheDirCount)
        context.FFmpegProgressDialog.setWindowModality(Qt.ApplicationModal)  # 设置窗口二为模态窗口
        context.FFmpegProgressDialog.show()

        reply = QMessageBox.question(None, "操作确认", f"合并勾选缓存文件为mp4格式",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.No:
            context.FFmpegProgressDialog.close()
            return

        mergeSuccessCount = 0

        for index, cacheInfo in enumerate(selectedList):
            # 更新进度弹窗内容
            context.FFmpegProgressDialog.renewContent(index)

            # 进度框点击取消
            if context.FFmpegProgressDialog.cancelled:
                break

            # 组合输出文件夹
            outputDirPath = os.path.join(context.getCompletePath(), cacheInfo.getTitle())
            if not os.path.exists(outputDirPath):
                os.makedirs(outputDirPath)
            # 组合输出全路径
            outputAllPath = os.path.join(outputDirPath, cacheInfo.getSubTitle() + ".mp4")
            # 判断输入输出文件路径是否有空格
            if not PathUtils.isPathConforms(cacheInfo, context, outputAllPath):
                # 更新进度
                progress_value += progress_step
                context.FFmpegProgressDialog.setProgress(progress_value)
                mergeSuccessCount += 1
                continue

            # 如果已经存在输出的文件已经存在
            if os.path.exists(outputAllPath):
                reply = QMessageBox.question(None, "覆盖确认", f"文件 {outputAllPath} 已经存在，是否覆盖？",
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if reply == QMessageBox.StandardButton.No:
                    # 重命名输出的文件名并执行合并命令
                    outputAllPath = FileUtils.getUniqueFileName(outputAllPath)
            if context.getCacheFileTpye() == CacheFileTpye.PC:
                self.fixM4s(cacheInfo)
            run_result = FFmpegUtils.runCommand(context, cacheInfo, outputAllPath)

            # 更新进度
            progress_value += progress_step
            context.FFmpegProgressDialog.setProgress(progress_value)
            if run_result:
                mergeSuccessCount += 1

            if context.FFmpegProgressDialog.progressBar.value() == 100:
                context.FFmpegProgressDialog.setContent(
                    f"总共缓存:{totalSelectCacheDirCount},有效缓存:{effectiveCacheDirCount}\n合并成功:{mergeSuccessCount}")

        # context.FFmpegProgressDialog.close()
