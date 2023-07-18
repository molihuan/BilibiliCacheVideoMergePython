import sys

from PySide6.QtWidgets import QApplication

from service.base.QDataMainWindow import QDataMainWindow
from service.convertbar.ConvertAction import ConvertAction
from service.convertbar.ExtractMP3Action import ExtractMP3Action
from service.dataarea.DataShowManage import DataShowManage
from service.init.InitManager import InitManager
from service.operatebar.down.CacheAraeAdjust import CacheAraeAdjust
from service.operatebar.up.CachePathShow import CachePathShow
from service.toolbar.HelpGroup import HelpGroup
from service.toolbar.StartGroup import StartGroup
from utils.DialogUtils import DialogUtils
from utils.ToastUtils import ToastUtils


class MainWindow(QDataMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initService()
        self.initView()
        self.setConnect()

    # 初始化服务
    def initService(self):
        # 添加成员变量toast工具
        self.Toast = ToastUtils(self)
        self.Dialog = DialogUtils(self)

        # 初始化管理者
        self.InitManager = InitManager(self)
        self.InitManager.initUI()
        self.InitManager.initData()
        self.InitManager.initView()

        # 开始工具栏
        self.StartGroup = StartGroup(self)
        self.HelpGroup = HelpGroup(self)
        self.CachePathShow = CachePathShow(self)
        self.CacheAraeAdjust = CacheAraeAdjust(self)
        self.DataShowManage = DataShowManage(self)
        self.ConvertAction = ConvertAction(self)
        self.ExtractMP3Action = ExtractMP3Action(self)

        self.SettingsView = None
        self.AboutView = None
        self.FFmpegProgressDialog = None

    # 初始化视图
    def initView(self):
        self.DataShowManage.showDataPageByFileStructure(self.getCachePath())
        pass

    # 设置监听
    def setConnect(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    # 美化库
    # apply_stylesheet(app, theme='light_blue.xml')
    widget.show()
    sys.exit(app.exec())
