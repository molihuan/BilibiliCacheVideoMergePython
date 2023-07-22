from enum import Enum

from PySide6.QtCore import Qt, QPropertyAnimation, QTimer
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

from modules.service.base.BaseService import BaseService


class ToastType(Enum):
    INFO = 0
    SUCCESS = 1
    ERROR = 2
    WARNING = 3


class ToastUtils(QWidget, BaseService):

    def __init__(self, context):
        super().__init__(context=context)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setStyleSheet(self.getToastColor(ToastType.INFO))

        layout = QVBoxLayout()
        self.label = QLabel()
        palette = self.label.palette()  # 获取当前的调色板
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))  # 设置文字颜色
        self.label.setPalette(palette)  # 应用调色板

        layout.addWidget(self.label)

        self.setLayout(layout)

    # 重新居中
    def showEvent(self, event):
        super().showEvent(event)
        self.move_to_center()

    def move_to_center(self):
        screen_geometry = QApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

    def shows(self, message, toastType: ToastType = ToastType.INFO, timeout=2000):
        colorTxt = self.getToastColor(toastType)
        self.setStyleSheet(colorTxt)

        self.label.setText(message)
        self.show()
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

        self.timer = QTimer()
        self.timer.timeout.connect(self.hides)
        self.timer.start(timeout)

    # 获取颜色样式
    def getToastColor(self, toastType: ToastType) -> str:
        colorDict = {
            ToastType.INFO: "background-color: #909399;",
            ToastType.SUCCESS: "background-color: #67c23a;",
            ToastType.ERROR: "background-color: #f56c6c;",
            ToastType.WARNING: "background-color: #e6a23c;"
        }
        return colorDict.get(toastType)

    def hides(self):
        self.animation.setDuration(1000)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.finished.connect(self.close)
        self.animation.start()
