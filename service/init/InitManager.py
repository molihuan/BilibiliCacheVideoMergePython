import json
import os

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QHeaderView

from service.base.BaseService import BaseService
from service.base.QDataMainWindow import QDataMainWindow
from service.init.DataManager import DataManager
from utils.PathUtils import PathUtils
from utils.StrUtils import StrUtils


class InitManager(BaseService):
    # 初始化UI
    def initUI(self):
        context: QDataMainWindow = self.getContext()
        # 加载界面文件绑定在BilibiliCacheVideoMergePython.pyproject中配置
        # context.ui = Ui_MainWindow()
        # context.ui.setupUi(context)

        # 设置图标和标题
        context.setWindowIcon(QIcon("./res/imgs/ml.ico"))
        context.setWindowTitle(DataManager.appName)
        context.statusBar().showMessage("欢迎使用" + DataManager.appName, 4000)

        # 获取和设置TableWidget
        dataList = context.ui.dataTableWidget
        dataList.setColumnCount(3)
        dataList.setHorizontalHeaderLabels(["标题", "路径"])
        dataList.setRowCount(15)

        # 设置表头自适应宽度
        header = dataList.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        # 最后一列拉伸
        # header.setStretchLastSection(True)

    # 初始化数据
    def initData(self):
        context: QDataMainWindow = self.getContext()
        # 程序所在的路径
        selfPath = os.getcwd()
        context.setSelfPath(selfPath)
        # 配置json路径
        configJsonPath = os.path.join(selfPath, 'config.json')
        context.setConfigJsonPath(configJsonPath)

        if os.path.exists(configJsonPath):
            # 存在配置文件
            try:
                # 初始化路径从配置文件中获取
                with open(configJsonPath, encoding='utf-8') as f:
                    configJson = json.load(f)
                if "cachePath" in configJson:
                    cachePath = configJson["cachePath"]
                    context.setCachePath(cachePath)
                if "completePath" in configJson:
                    completePath = configJson["completePath"]
                    context.setCompletePath(completePath)
                if "sysFFmpegPath" in configJson:
                    sysFFmpegPath = configJson["sysFFmpegPath"]
                    context.setSysFFmpegPath(sysFFmpegPath)
            except json.JSONDecodeError as e:
                self.initConfigJson(context)
                print(f"JSON decoding error: {e}")
        else:
            self.initConfigJson(context)

        allPath = context.getConfigPathDict()
        # 检查路径是否有空格
        StrUtils.isPathConforms(context, allPath)

    # 新建config.json文件并设置默认值
    def initConfigJson(self, context):
        # 获取ffmpeg的路径每一种路径都不一样
        sysFFmpegPath = PathUtils.getFFmpegPath()
        context.setSysFFmpegPath(sysFFmpegPath)
        # 缓存路径
        cachePath = ''
        # 不存在配置文件
        context.setCachePath(cachePath)
        # 输出合并文件所在的文件夹
        completePath = os.path.join(os.getcwd(), 'complete')
        context.setCompletePath(completePath)
        # 创建要写入的数据
        configJson = {
            'sysFFmpegPath': sysFFmpegPath,
            'cachePath': cachePath,
            'completePath': completePath
        }
        # 将数据写入到config.json文件中
        with open(context.getConfigJsonPath(), 'w') as file:
            json.dump(configJson, file, indent=4)

    def initView(self):
        context: QDataMainWindow = self.getContext()
        ui = self.getUI()
        cachePathEdit = ui.vedioDirShowLineEdit
        cachePathEdit.setText(context.getCachePath())
