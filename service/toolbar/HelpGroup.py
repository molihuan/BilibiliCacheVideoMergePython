import os

from PySide6.QtCore import Qt

from service.base.BaseService import BaseService
from utils.HttpUtils import HttpUtils
from utils.PathUtils import PathUtils
from views.AboutView import AboutView


class HelpGroup(BaseService):

    def __init__(self, context):
        super().__init__(context)
        context.ui.helpItem.triggered.connect(self.openHelpWebsite)
        context.ui.checkUpdateItem.triggered.connect(self.checkUpdate)
        context.ui.aboutItem.triggered.connect(self.openAboutView)

    # 打开教程网址
    def openHelpWebsite(self):
        HttpUtils.openUrlByCallSystemBrowser()
        pass

    # 检查更新
    def checkUpdate(self):
        pass

    # 打开关于页面
    def openAboutView(self):
        context = self.getContext()
        if not context.AboutView:
            # 实例化窗口
            context.AboutView = AboutView(context)
            mdDirPath = PathUtils.getResMdPath()
            statementFilePath = os.path.join(mdDirPath, "statement.md")
            context.AboutView.loadFile(statementFilePath)
        context.AboutView.setWindowModality(Qt.ApplicationModal)  # 设置窗口二为模态窗口
        context.AboutView.show()
        pass
