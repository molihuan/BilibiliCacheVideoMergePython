import os
import shutil

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QMessageBox

from modules.home.convertbar.BaseAction import BaseAction
from modules.home.dataarea.DataShowManager import DataShowManager, CacheFileTpye
from modules.home.dialogs.impl.MP3CopyProgressDialog import MP3CopyProgressDialog
from modules.utils.Log import Log


class ExtractMP3Action(BaseAction):
    def __init__(self, mContext):
        super().__init__(mContext=mContext)

    def setConnect(self, context: QMainWindow):
        ui = self.getUI()
        ui.getMP3Btn.clicked.connect(self.handleExtractMP3)

    # 提取mp3按钮
    def handleExtractMP3(self):
        context = self.getContext()
        manage: DataShowManager = context.DataShowManage
        # 获取勾选的列表
        totalSelectCacheDirCount, selectedList = self.collection2ChapterList(manage)
        # 有效的缓存数量
        effectiveCacheDirCount = len(selectedList)

        progress_step = 100 / effectiveCacheDirCount
        progress_value = 0

        # 创建进度弹窗
        if not context.MP3CopyProgressDialog:
            # 实例化窗口
            context.MP3CopyProgressDialog = MP3CopyProgressDialog(context)
        context.MP3CopyProgressDialog.setCacheDirCount(totalSelectCacheDirCount, effectiveCacheDirCount)
        context.MP3CopyProgressDialog.setWindowModality(Qt.ApplicationModal)  # 设置窗口二为模态窗口
        context.MP3CopyProgressDialog.show()

        reply = QMessageBox.question(None, "操作确认", f"提取勾选缓存文件的音频",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.No:
            context.MP3CopyProgressDialog.close()
            return

        mergeSuccessCount = 0

        for index, cacheInfo in enumerate(selectedList):
            # 更新进度弹窗内容
            context.MP3CopyProgressDialog.renewContent(index)
            # 进度框点击取消
            if context.MP3CopyProgressDialog.cancelled:
                break
            # 组合输出文件夹
            outputDirPath = os.path.join(context.getCompletePath(), cacheInfo.getTitle())
            if not os.path.exists(outputDirPath):
                os.makedirs(outputDirPath)

            # 组合输出全路径
            outputAllPath = os.path.join(outputDirPath, cacheInfo.getSubTitle() + ".mp3")
            if os.path.exists(outputAllPath):

                reply = QMessageBox.question(None, "覆盖确认", f"文件 {outputAllPath} 已经存在，是否覆盖？",
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if reply == QMessageBox.StandardButton.No:
                    # 更新进度
                    progress_value += progress_step
                    context.MP3CopyProgressDialog.setProgress(progress_value)
                    mergeSuccessCount += 1
                    continue

            # 更新进度
            progress_value += progress_step
            context.MP3CopyProgressDialog.setProgress(progress_value)
            try:

                if cacheInfo.getAudioPath() is None:
                    raise shutil.Error("cacheInfo.getAudioPath() is None")

                if context.getCacheFileTpye() == CacheFileTpye.PC:
                    self.fixM4s(cacheInfo)
                    shutil.copy(cacheInfo.getAudioPath(), outputAllPath)
                else:
                    shutil.copy(cacheInfo.getAudioPath(), outputAllPath)
                mergeSuccessCount += 1
            except shutil.Error as e:
                Log.i(f"复制失败: {e}")

            if context.MP3CopyProgressDialog.progressBar.value() == 100:
                context.MP3CopyProgressDialog.setContent(
                    f"总共缓存:{totalSelectCacheDirCount},有效缓存:{effectiveCacheDirCount}\n提取成功:{mergeSuccessCount}")
