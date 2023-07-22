from modules.service.convertbar.ConvertAction import ConvertAction
from modules.service.convertbar.ExtractMP3Action import ExtractMP3Action
from modules.service.dataarea.DataShowManage import DataShowManage
from modules.service.init.InitManager import InitManager
from modules.service.operatebar.down.CacheAraeAdjust import CacheAraeAdjust
from modules.service.operatebar.up.CachePathShow import CachePathShow
from modules.service.toolbar.HelpGroup import HelpGroup

from modules.utils.DialogUtils import DialogUtils
from modules.utils.ToastUtils import ToastUtils
from modules.widgets.BaseDataWorkPage import BaseDataWorkPage


class WorkPage(BaseDataWorkPage):
    def __init__(self, configManager):
        super().__init__(configManager)
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

        # 工具
        self.HelpGroup = HelpGroup(self)
        self.CachePathShow = CachePathShow(self)
        self.CacheAraeAdjust = CacheAraeAdjust(self)
        self.DataShowManage = DataShowManage(self)
        self.ConvertAction = ConvertAction(self)
        self.ExtractMP3Action = ExtractMP3Action(self)

        self.SettingsView = None
        self.AboutView = None
        self.FFmpegProgressDialog = None
        self.MP3CopyProgressDialog = None

    # 初始化视图
    def initView(self):
        self.DataShowManage.showDataPageByFileStructure(self.getCachePath())
        pass

    # 设置监听
    def setConnect(self):
        pass
