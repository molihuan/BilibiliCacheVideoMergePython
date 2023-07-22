# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import time

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////

from modules import *
from modules import Settings
from modules.service.manager.ConfigManager import ConfigManager, ConfigKey

from modules.utils.SysUtils import SysUtils, SysType
from modules.widgets.WorkPage import WorkPage
from modules.widgets.settings.BaseSettingsPage import BaseSettingsPage
from script.appDetails import APP_NAME, APP_VERSION

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

appVersion = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # 程序所在的路径
        self.selfPath = os.getcwd()
        configJsonPath = os.path.join(self.selfPath, 'config.json')
        # 配置管理者
        self.ConfigManager = ConfigManager(configJsonPath)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        # 加载视图
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        self.afterLoadUi()

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        if SysUtils.getSysType() == SysType.WIN:
            Settings.ENABLE_CUSTOM_TITLE_BAR = True
        else:
            Settings.ENABLE_CUSTOM_TITLE_BAR = False

        # APP 名称和版本
        # ///////////////////////////////////////////////////////////////
        appName = APP_NAME
        description = APP_NAME
        # APPLY TEXTS
        self.setWindowTitle(appName)
        widgets.titleRightInfo.setText(description)
        widgets.version.setText(APP_VERSION)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # 按钮点击事件
        # ///////////////////////////////////////////////////////////////
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_demonstrate.clicked.connect(self.buttonClick)
        widgets.btn_exit.clicked.connect(self.buttonClick)
        widgets.btn_base_settings.clicked.connect(self.buttonClick)
        widgets.btn_change_theme.clicked.connect(self.buttonClick)

        # 左边伸缩盒子
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # 右边伸缩盒子
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)

        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # 设置自定义主题
        # ///////////////////////////////////////////////////////////////
        # 路径冻结，防止打包成exe后路径错乱
        # if getattr(sys, 'frozen', False):
        #     absPath = os.path.dirname(os.path.abspath(sys.executable))
        # elif __file__:
        #     absPath = os.path.dirname(os.path.abspath(__file__))

        self.useCustomTheme = True

        if not self.ConfigManager.isExist(ConfigKey.THEMES_PATH):
            themesPath = os.path.join(self.selfPath, "themes/py_dracula_dark.qss")
            self.ConfigManager.add(ConfigKey.THEMES_PATH, themesPath)
            self.ConfigManager.save()
        self.themeFile = self.ConfigManager.get(ConfigKey.THEMES_PATH)

        # SET THEME AND HACKS
        if self.useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, self.themeFile, True)
            # SET HACKS
            AppFunctions.setThemeHack(self)

        # 默认加载视图
        # ///////////////////////////////////////////////////////////////
        # 实例化视图
        self.workPage: WorkPage = WorkPage(self.ConfigManager)
        # 添加到StackedWidget中
        widgets.stackedWidget.addWidget(self.workPage)
        # 设置为当前显示页
        widgets.stackedWidget.setCurrentWidget(self.workPage)
        # 设置选中按钮样式
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    # 处理按钮点击
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # 显示主页面
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(self.workPage)  # 加载页面
            UIFunctions.resetStyle(self, btnName)  # 重新设置样式
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # 设置侧边菜单item为选中样式

        # 控件演示(例子)页面
        if btnName == "btn_demonstrate":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            print(self.workPage.DataShowManage.selectedCacheList)
            pass

        # 改变主题
        if btnName == "btn_change_theme":
            darkTheme = os.path.join(self.selfPath, "themes/py_dracula_dark.qss")

            if self.themeFile == darkTheme:
                self.themeFile = os.path.join(self.selfPath, "themes/py_dracula_light.qss")
            else:
                self.themeFile = darkTheme

            self.ConfigManager.update(ConfigKey.THEMES_PATH, self.themeFile)
            self.ConfigManager.save()
            UIFunctions.theme(self, self.themeFile, True)
            # SET HACKS
            AppFunctions.setThemeHack(self)
        # 退出
        if btnName == "btn_exit":
            self.close()
        # 基础设置按钮
        if btnName == "btn_base_settings":
            # 实例化视图
            settingsPage = BaseSettingsPage(self.workPage)
            # 添加到StackedWidget中
            widgets.stackedWidget.addWidget(settingsPage)
            # 设置为当前显示页
            widgets.stackedWidget.setCurrentWidget(settingsPage)
            # 设置选中按钮样式
            widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

            pass

        # PRINT BTN NAME
        print(f'按钮 "{btnName}" 点击!')

    # 加载ui后要进行的处理
    def afterLoadUi(self):
        # 隐藏控件演示页面按钮
        widgets.btn_demonstrate.hide()
        pass

    # 设置大小事件
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # 鼠标点击事件
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    # 关闭之前调用
    def closeEvent(self, event):
        self.workPage.closeEvent(event)
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./res/images/images/ml.ico"))
    window = MainWindow()
    sys.exit(app.exec())
