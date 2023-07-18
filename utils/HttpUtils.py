from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices


class HttpUtils():
    @staticmethod
    def openUrlByCallSystemBrowser(url="https://www.baidu.com"):
        qUrl = QUrl(url)  # 设置要打开的网址
        QDesktopServices.openUrl(qUrl)
