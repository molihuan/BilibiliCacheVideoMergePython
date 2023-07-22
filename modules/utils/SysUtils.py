import sys
from enum import Enum

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap


class SysType(Enum):
    UNKNOWN = 0
    WIN = 1
    LINUX = 2
    MAC = 3


class SysUtils():
    # 获取系统类型
    @staticmethod
    def getSysType():
        if sys.platform.startswith('win'):
            return SysType.WIN
        elif sys.platform.startswith('linux'):
            return SysType.LINUX
        elif sys.platform.startswith('darwin'):
            return SysType.MAC
        else:
            return SysType.UNKNOWN

    @staticmethod
    def getTransparentIcon() -> QIcon:
        # 创建透明图标
        transparent_icon = QIcon()
        transparent_pixmap = QPixmap(1, 1)
        transparent_pixmap.fill(Qt.transparent)
        transparent_icon.addPixmap(transparent_pixmap)

        return transparent_icon
