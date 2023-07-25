# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'playerHxezsM.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
                               QWidget)


class Ui_PlayerWidget(object):
    def setupUi(self, PlayerWidget):
        if not PlayerWidget.objectName():
            PlayerWidget.setObjectName(u"PlayerWidget")
        PlayerWidget.resize(832, 557)
        self.layoutWidget = QWidget(PlayerWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 20, 671, 491))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.videoWidget = QVideoWidget(self.layoutWidget)
        self.videoWidget.setObjectName(u"videoWidget")

        self.verticalLayout.addWidget(self.videoWidget)

        self.btnPlay = QPushButton(self.layoutWidget)
        self.btnPlay.setObjectName(u"btnPlay")

        self.verticalLayout.addWidget(self.btnPlay)

        self.retranslateUi(PlayerWidget)

        QMetaObject.connectSlotsByName(PlayerWidget)

    # setupUi

    def retranslateUi(self, PlayerWidget):
        PlayerWidget.setWindowTitle(QCoreApplication.translate("PlayerWidget", u"Form", None))
        self.btnPlay.setText(QCoreApplication.translate("PlayerWidget", u"PushButton", None))
    # retranslateUi
