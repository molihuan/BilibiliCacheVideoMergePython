import os
import sys

from PySide6.QtWidgets import QHeaderView, QTableWidget

from modules.framework.manager.ConfigManager import ConfigKey
from modules.home.BaseDataWorkPage import BaseDataWorkPage
from modules.home.base.BaseService import BaseService
from modules.home.dataarea.DataShowManager import PAGE_SIZE
from modules.utils.PathUtils import PathUtils
from modules.utils.SysUtils import SysUtils


class InitManager(BaseService):
    # 初始化UI
    def initUI(self):
        context = self.getContext()

        # 获取和设置TableWidget
        dataTableWidget: QTableWidget = context.ui.dataTableWidget
        dataTableWidget.setColumnCount(2)
        dataTableWidget.setHorizontalHeaderLabels(["标题", "路径"])
        dataTableWidget.setRowCount(PAGE_SIZE)

        # 设置表头自适应宽度
        header = dataTableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        header = dataTableWidget.verticalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # 最后一列拉伸
        # header.setStretchLastSection(True)

    # 初始化数据
    def initData(self):
        context: BaseDataWorkPage = self.getContext()
        # 程序所在的路径
        selfPath = PathUtils.getcwd()
        context.setSelfPath(selfPath)

        # if getattr(sys, 'frozen', False):
        #     absPath = os.path.dirname(os.path.abspath(sys.executable))
        # elif __file__:
        #     absPath = os.path.dirname(os.path.abspath(__file__))
        # themeFile = os.path.abspath(os.path.join(absPath, "themes/py_dracula_light.qss"))
        #
        # print(themeFile)

        resource_path = PathUtils.getcwd()
        print(resource_path)

        # 配置json路径
        configJsonPath = os.path.join(selfPath, 'config.json')
        context.setConfigJsonPath(configJsonPath)

        configManager = context.ConfigManager

        if not configManager.isExist(ConfigKey.INIT_NEED_PATH):
            self.initNeedPath(context)

        cachePath = configManager.get(ConfigKey.CACHE_PATH)
        context.setCachePath(cachePath)

        completePath = configManager.get(ConfigKey.COMPLETE_PATH)
        context.setCompletePath(completePath)

        sysFFmpegPath = configManager.get(ConfigKey.SYS_FFMPEG_PATH)
        context.setSysFFmpegPath(sysFFmpegPath)

        # 检查ffmpeg是否有执行权限
        SysUtils.checkFFmpegExecPermissions(sysFFmpegPath)

        # allPath = context.getConfigPathDict()
        # # 检查路径是否有空格
        # StrUtils.isNullOrWhitespace(context, allPath)

    # 新建config.json文件并设置默认值
    def initNeedPath(self, context):
        # 获取ffmpeg的路径每一种路径都不一样
        sysFFmpegPath = PathUtils.getFFmpegPath()
        context.setSysFFmpegPath(sysFFmpegPath)
        # 缓存路径
        cachePath = ''
        # 不存在配置文件
        context.setCachePath(cachePath)
        # 输出合并文件所在的文件夹
        completePath = os.path.join(context.getSelfPath(), 'complete')
        context.setCompletePath(completePath)
        # 创建要写入的数据
        configJson = {
            ConfigKey.INIT_NEED_PATH: 1,
            ConfigKey.SYS_FFMPEG_PATH: sysFFmpegPath,
            ConfigKey.CACHE_PATH: cachePath,
            ConfigKey.COMPLETE_PATH: completePath
        }
        # 将数据写入到config.json文件中
        context.ConfigManager.addByDict(configJson)
        context.ConfigManager.save()

    def initView(self):
        context = self.getContext()
        ui = self.getUI()
        cachePathEdit = ui.vedioDirShowLineEdit
        cachePathEdit.setText(context.getCachePath())
        pass
