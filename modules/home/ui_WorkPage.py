# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WorkPageihuHCJ.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from modules.home.ui.MlLineEdit import MlLineEdit

class Ui_WorkPageWidget(object):
    def setupUi(self, WorkPageWidget):
        if not WorkPageWidget.objectName():
            WorkPageWidget.setObjectName(u"WorkPageWidget")
        WorkPageWidget.resize(802, 600)
        self.settingItem = QAction(WorkPageWidget)
        self.settingItem.setObjectName(u"settingItem")
        self.exitItem = QAction(WorkPageWidget)
        self.exitItem.setObjectName(u"exitItem")
        self.helpItem = QAction(WorkPageWidget)
        self.helpItem.setObjectName(u"helpItem")
        self.checkUpdateItem = QAction(WorkPageWidget)
        self.checkUpdateItem.setObjectName(u"checkUpdateItem")
        self.aboutItem = QAction(WorkPageWidget)
        self.aboutItem.setObjectName(u"aboutItem")
        self.verticalLayout_2 = QVBoxLayout(WorkPageWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CatchVedioDirLayout = QHBoxLayout()
        self.CatchVedioDirLayout.setObjectName(u"CatchVedioDirLayout")
        self.vedioDirLabel = QLabel(WorkPageWidget)
        self.vedioDirLabel.setObjectName(u"vedioDirLabel")

        self.CatchVedioDirLayout.addWidget(self.vedioDirLabel)

        self.vedioDirShowLineEdit = MlLineEdit(WorkPageWidget)
        self.vedioDirShowLineEdit.setObjectName(u"vedioDirShowLineEdit")
        self.vedioDirShowLineEdit.setMinimumSize(QSize(0, 30))
        self.vedioDirShowLineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.vedioDirShowLineEdit.setProperty("dragEnabled", True)
        self.vedioDirShowLineEdit.setProperty("clearButtonEnabled", True)

        self.CatchVedioDirLayout.addWidget(self.vedioDirShowLineEdit)

        self.selectVedioDirBtn = QPushButton(WorkPageWidget)
        self.selectVedioDirBtn.setObjectName(u"selectVedioDirBtn")
        self.selectVedioDirBtn.setMinimumSize(QSize(120, 30))
        self.selectVedioDirBtn.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.CatchVedioDirLayout.addWidget(self.selectVedioDirBtn)


        self.verticalLayout.addLayout(self.CatchVedioDirLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.goBackBtn = QPushButton(WorkPageWidget)
        self.goBackBtn.setObjectName(u"goBackBtn")
        self.goBackBtn.setMinimumSize(QSize(120, 30))
        self.goBackBtn.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout.addWidget(self.goBackBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.completeFileBtn = QPushButton(WorkPageWidget)
        self.completeFileBtn.setObjectName(u"completeFileBtn")
        self.completeFileBtn.setMinimumSize(QSize(120, 30))
        self.completeFileBtn.setAcceptDrops(False)
        self.completeFileBtn.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_2.addWidget(self.completeFileBtn)

        self.selectAllBtn = QPushButton(WorkPageWidget)
        self.selectAllBtn.setObjectName(u"selectAllBtn")
        self.selectAllBtn.setMinimumSize(QSize(120, 30))
        self.selectAllBtn.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_2.addWidget(self.selectAllBtn)

        self.refreshBtn = QPushButton(WorkPageWidget)
        self.refreshBtn.setObjectName(u"refreshBtn")
        self.refreshBtn.setMinimumSize(QSize(120, 30))
        self.refreshBtn.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_2.addWidget(self.refreshBtn)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.dataTableWidget = QTableWidget(WorkPageWidget)
        self.dataTableWidget.setObjectName(u"dataTableWidget")
        self.dataTableWidget.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.dataTableWidget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.prePageBtn = QPushButton(WorkPageWidget)
        self.prePageBtn.setObjectName(u"prePageBtn")
        self.prePageBtn.setMinimumSize(QSize(100, 20))
        self.prePageBtn.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_4.addWidget(self.prePageBtn)

        self.curPageEdit = QLineEdit(WorkPageWidget)
        self.curPageEdit.setObjectName(u"curPageEdit")
        self.curPageEdit.setMinimumSize(QSize(100, 20))
        self.curPageEdit.setMaximumSize(QSize(50, 16777215))
        self.curPageEdit.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.curPageEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.curPageEdit)

        self.sufPageBtn = QPushButton(WorkPageWidget)
        self.sufPageBtn.setObjectName(u"sufPageBtn")
        self.sufPageBtn.setMinimumSize(QSize(100, 20))
        self.sufPageBtn.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_4.addWidget(self.sufPageBtn)

        self.totalPageLabel = QLabel(WorkPageWidget)
        self.totalPageLabel.setObjectName(u"totalPageLabel")
        self.totalPageLabel.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_4.addWidget(self.totalPageLabel)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.getMP3Btn = QPushButton(WorkPageWidget)
        self.getMP3Btn.setObjectName(u"getMP3Btn")
        self.getMP3Btn.setMinimumSize(QSize(120, 30))
        self.getMP3Btn.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_3.addWidget(self.getMP3Btn)

        self.mergeBtn = QPushButton(WorkPageWidget)
        self.mergeBtn.setObjectName(u"mergeBtn")
        self.mergeBtn.setMinimumSize(QSize(120, 30))
        self.mergeBtn.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_3.addWidget(self.mergeBtn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(WorkPageWidget)

        QMetaObject.connectSlotsByName(WorkPageWidget)
    # setupUi

    def retranslateUi(self, WorkPageWidget):
        WorkPageWidget.setWindowTitle(QCoreApplication.translate("WorkPageWidget", u"MainWindow", None))
        self.settingItem.setText(QCoreApplication.translate("WorkPageWidget", u"\u8bbe\u7f6e", None))
        self.exitItem.setText(QCoreApplication.translate("WorkPageWidget", u"\u9000\u51fa", None))
        self.helpItem.setText(QCoreApplication.translate("WorkPageWidget", u"\u4f7f\u7528\u6559\u7a0b", None))
        self.checkUpdateItem.setText(QCoreApplication.translate("WorkPageWidget", u"\u68c0\u6d4b\u66f4\u65b0", None))
        self.aboutItem.setText(QCoreApplication.translate("WorkPageWidget", u"\u5173\u4e8e", None))
        self.vedioDirLabel.setText(QCoreApplication.translate("WorkPageWidget", u"\u89c6\u9891\u7f13\u5b58\u76ee\u5f55:", None))
        self.selectVedioDirBtn.setText(QCoreApplication.translate("WorkPageWidget", u"\u9009\u62e9\u76ee\u5f55", None))
        self.goBackBtn.setText(QCoreApplication.translate("WorkPageWidget", u"\u4e0a\u4e00\u7ea7", None))
        self.completeFileBtn.setText(QCoreApplication.translate("WorkPageWidget", u"\u5b8c\u6210\u6587\u4ef6", None))
        self.selectAllBtn.setText(QCoreApplication.translate("WorkPageWidget", u"\u5168\u9009", None))
        self.refreshBtn.setText(QCoreApplication.translate("WorkPageWidget", u"\u5237\u65b0", None))
        self.prePageBtn.setText(QCoreApplication.translate("WorkPageWidget", u"\u4e0a\u4e00\u9875", None))
        self.sufPageBtn.setText(QCoreApplication.translate("WorkPageWidget", u"\u4e0b\u4e00\u9875", None))
        self.totalPageLabel.setText(QCoreApplication.translate("WorkPageWidget", u"\u603b\u9875\u6570:", None))
        self.getMP3Btn.setText(QCoreApplication.translate("WorkPageWidget", u"\u63d0\u53d6\u97f3\u9891", None))
        self.mergeBtn.setText(QCoreApplication.translate("WorkPageWidget", u"\u5408\u5e76", None))
    # retranslateUi

