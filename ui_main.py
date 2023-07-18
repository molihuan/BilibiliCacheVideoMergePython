# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 600)
        self.settingItem = QAction(MainWindow)
        self.settingItem.setObjectName(u"settingItem")
        self.exitItem = QAction(MainWindow)
        self.exitItem.setObjectName(u"exitItem")
        self.helpItem = QAction(MainWindow)
        self.helpItem.setObjectName(u"helpItem")
        self.checkUpdateItem = QAction(MainWindow)
        self.checkUpdateItem.setObjectName(u"checkUpdateItem")
        self.aboutItem = QAction(MainWindow)
        self.aboutItem.setObjectName(u"aboutItem")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.goBackBtn = QPushButton(self.centralwidget)
        self.goBackBtn.setObjectName(u"goBackBtn")
        self.goBackBtn.setGeometry(QRect(10, 50, 93, 31))
        self.dataTableWidget = QTableWidget(self.centralwidget)
        self.dataTableWidget.setObjectName(u"dataTableWidget")
        self.dataTableWidget.setGeometry(QRect(10, 90, 781, 421))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 781, 41))
        self.CatchVedioDirLayout = QHBoxLayout(self.layoutWidget)
        self.CatchVedioDirLayout.setObjectName(u"CatchVedioDirLayout")
        self.CatchVedioDirLayout.setContentsMargins(0, 0, 0, 0)
        self.vedioDirLabel = QLabel(self.layoutWidget)
        self.vedioDirLabel.setObjectName(u"vedioDirLabel")

        self.CatchVedioDirLayout.addWidget(self.vedioDirLabel)

        self.vedioDirShowLineEdit = QLineEdit(self.layoutWidget)
        self.vedioDirShowLineEdit.setObjectName(u"vedioDirShowLineEdit")
        self.vedioDirShowLineEdit.setDragEnabled(True)
        self.vedioDirShowLineEdit.setClearButtonEnabled(True)

        self.CatchVedioDirLayout.addWidget(self.vedioDirShowLineEdit)

        self.selectVedioDirBtn = QPushButton(self.layoutWidget)
        self.selectVedioDirBtn.setObjectName(u"selectVedioDirBtn")

        self.CatchVedioDirLayout.addWidget(self.selectVedioDirBtn)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(500, 40, 295, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.completeFileBtn = QPushButton(self.layoutWidget1)
        self.completeFileBtn.setObjectName(u"completeFileBtn")

        self.horizontalLayout_2.addWidget(self.completeFileBtn)

        self.selectAllBtn = QPushButton(self.layoutWidget1)
        self.selectAllBtn.setObjectName(u"selectAllBtn")

        self.horizontalLayout_2.addWidget(self.selectAllBtn)

        self.refreshBtn = QPushButton(self.layoutWidget1)
        self.refreshBtn.setObjectName(u"refreshBtn")

        self.horizontalLayout_2.addWidget(self.refreshBtn)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(300, 520, 195, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.getMP3Btn = QPushButton(self.layoutWidget2)
        self.getMP3Btn.setObjectName(u"getMP3Btn")

        self.horizontalLayout_3.addWidget(self.getMP3Btn)

        self.mergeBtn = QPushButton(self.layoutWidget2)
        self.mergeBtn.setObjectName(u"mergeBtn")

        self.horizontalLayout_3.addWidget(self.mergeBtn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 802, 26))
        self.startMenu = QMenu(self.menubar)
        self.startMenu.setObjectName(u"startMenu")
        self.helpMenu = QMenu(self.menubar)
        self.helpMenu.setObjectName(u"helpMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.startMenu.menuAction())
        self.menubar.addAction(self.helpMenu.menuAction())
        self.startMenu.addAction(self.settingItem)
        self.startMenu.addSeparator()
        self.startMenu.addAction(self.exitItem)
        self.helpMenu.addAction(self.helpItem)
        self.helpMenu.addAction(self.checkUpdateItem)
        self.helpMenu.addSeparator()
        self.helpMenu.addAction(self.aboutItem)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.settingItem.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.exitItem.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.helpItem.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u6559\u7a0b", None))
        self.checkUpdateItem.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u66f4\u65b0", None))
        self.aboutItem.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.goBackBtn.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u7ea7", None))
        self.vedioDirLabel.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u7f13\u5b58\u76ee\u5f55:", None))
        self.selectVedioDirBtn.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u76ee\u5f55", None))
        self.completeFileBtn.setText(QCoreApplication.translate("MainWindow", u"\u5b8c\u6210\u6587\u4ef6", None))
        self.selectAllBtn.setText(QCoreApplication.translate("MainWindow", u"\u5168\u9009", None))
        self.refreshBtn.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.getMP3Btn.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u53d6\u97f3\u9891", None))
        self.mergeBtn.setText(QCoreApplication.translate("MainWindow", u"\u5408\u5e76", None))
        self.startMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.helpMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

