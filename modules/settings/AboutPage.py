from PySide6.QtWidgets import QWidget, QTextBrowser, QHBoxLayout

from modules.home.base import BaseService
from modules.utils.SysUtils import SysUtils


class AboutPage(QWidget, BaseService):
    def __init__(self, mContext):
        super().__init__(mContext=mContext)
        self.resize(600, 500)
        self.setWindowTitle("关于")
        # 设置透明icon
        icon = SysUtils.getTransparentIcon()
        self.setWindowIcon(icon)
        self.main_layout = QHBoxLayout()
        self.text_browser = QTextBrowser(self)
        self.main_layout.addWidget(self.text_browser)

        self.setLayout(self.main_layout)

    def loadFile(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        self.text_browser.setText(text)
