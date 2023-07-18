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
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

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
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CatchVedioDirLayout = QHBoxLayout()
        self.CatchVedioDirLayout.setObjectName(u"CatchVedioDirLayout")
        self.vedioDirLabel = QLabel(self.centralwidget)
        self.vedioDirLabel.setObjectName(u"vedioDirLabel")

        self.CatchVedioDirLayout.addWidget(self.vedioDirLabel)

        self.vedioDirShowLineEdit = QLineEdit(self.centralwidget)
        self.vedioDirShowLineEdit.setObjectName(u"vedioDirShowLineEdit")
        self.vedioDirShowLineEdit.setDragEnabled(True)
        self.vedioDirShowLineEdit.setClearButtonEnabled(True)

        self.CatchVedioDirLayout.addWidget(self.vedioDirShowLineEdit)

        self.selectVedioDirBtn = QPushButton(self.centralwidget)
        self.selectVedioDirBtn.setObjectName(u"selectVedioDirBtn")

        self.CatchVedioDirLayout.addWidget(self.selectVedioDirBtn)


        self.verticalLayout.addLayout(self.CatchVedioDirLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.goBackBtn = QPushButton(self.centralwidget)
        self.goBackBtn.setObjectName(u"goBackBtn")

        self.horizontalLayout.addWidget(self.goBackBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.completeFileBtn = QPushButton(self.centralwidget)
        self.completeFileBtn.setObjectName(u"completeFileBtn")

        self.horizontalLayout_2.addWidget(self.completeFileBtn)

        self.selectAllBtn = QPushButton(self.centralwidget)
        self.selectAllBtn.setObjectName(u"selectAllBtn")

        self.horizontalLayout_2.addWidget(self.selectAllBtn)

        self.refreshBtn = QPushButton(self.centralwidget)
        self.refreshBtn.setObjectName(u"refreshBtn")

        self.horizontalLayout_2.addWidget(self.refreshBtn)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.dataTableWidget = QTableWidget(self.centralwidget)
        self.dataTableWidget.setObjectName(u"dataTableWidget")

        self.verticalLayout.addWidget(self.dataTableWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.getMP3Btn = QPushButton(self.centralwidget)
        self.getMP3Btn.setObjectName(u"getMP3Btn")

        self.horizontalLayout_3.addWidget(self.getMP3Btn)

        self.mergeBtn = QPushButton(self.centralwidget)
        self.mergeBtn.setObjectName(u"mergeBtn")

        self.horizontalLayout_3.addWidget(self.mergeBtn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

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
        self.vedioDirLabel.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u7f13\u5b58\u76ee\u5f55:", None))
        self.selectVedioDirBtn.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u76ee\u5f55", None))
        self.goBackBtn.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u7ea7", None))
        self.completeFileBtn.setText(QCoreApplication.translate("MainWindow", u"\u5b8c\u6210\u6587\u4ef6", None))
        self.selectAllBtn.setText(QCoreApplication.translate("MainWindow", u"\u5168\u9009", None))
        self.refreshBtn.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.getMP3Btn.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u53d6\u97f3\u9891", None))
        self.mergeBtn.setText(QCoreApplication.translate("MainWindow", u"\u5408\u5e76", None))
        self.startMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.helpMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

