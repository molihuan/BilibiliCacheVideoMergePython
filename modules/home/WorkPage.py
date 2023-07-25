from modules.home.convertbar.impl.ConvertAction import ConvertAction
from modules.home.convertbar.impl.ExtractMP3Action import ExtractMP3Action
from modules.home.dataarea.DataShowManager import DataShowManager
from modules.home.init.InitManager import InitManager
from modules.home.toolbar.CacheAraeAdjust import CacheAraeAdjust
from modules.home.toolbar.CachePathShow import CachePathShow


from modules.utils.DialogUtils import DialogUtils
from modules.utils.PathUtils import PathUtils
from modules.utils.ToastUtils import ToastUtils
from modules.home.BaseDataWorkPage import BaseDataWorkPage


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

        self.CachePathShow = CachePathShow(self)
        self.CacheAraeAdjust = CacheAraeAdjust(self)
        self.DataShowManage = DataShowManager(self)
        self.ConvertAction = ConvertAction(self)
        self.ExtractMP3Action = ExtractMP3Action(self)

        self.SettingsView = None
        self.AboutView = None
        self.FFmpegProgressDialog = None
        self.MP3CopyProgressDialog = None

        # path = PathUtils.resource_path("config.json")
        # self.Toast.shows(path)

    # 初始化视图
    def initView(self):
        self.DataShowManage.showDataPageByFileStructure(self.getCachePath())
        pass

    # 设置监听
    def setConnect(self):
        pass
