from abc import abstractmethod

from PySide6.QtWidgets import QMainWindow

from ui_main import Ui_MainWindow


class BaseService():
    def __init__(self, context):
        self.context = context
        self.ui: Ui_MainWindow = context.ui
        self.setConnect(context)

    # 获取上下文
    def getContext(self) -> QMainWindow:
        return self.context

    # 获取ui
    def getUI(self) -> Ui_MainWindow:
        return self.ui

    # 设置监听
    @abstractmethod
    def setConnect(self, context: QMainWindow):
        pass
