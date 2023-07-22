import os
import subprocess
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

    # 检查ffmpeg文件是否具有可执行权限
    @staticmethod
    def checkFFmpegExecPermissions(ffmpeg_path: str):
        if os.access(ffmpeg_path, os.X_OK):
            print("ffmpeg具有执行权限")
        else:
            print("ffmpeg没有执行权限")
            # 使用subprocess执行chmod命令给ffmpeg文件添加可执行权限
            cmd = f"chmod 775 {ffmpeg_path}"
            exit_code = subprocess.call(cmd, shell=True)

            if os.access(ffmpeg_path, os.X_OK):
                print(f"自动授权成功")
            else:
                print(f"自动授权失败，请手动给{ffmpeg_path}授予执行权限")
