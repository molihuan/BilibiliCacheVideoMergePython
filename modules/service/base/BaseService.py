from abc import abstractmethod

from PySide6.QtWidgets import QMainWindow




class BaseService():
    def __init__(self, context):
        self.context = context
        self.ui = context.ui
        self.setConnect(context)

    # 获取上下文
    def getContext(self) -> QMainWindow:
        return self.context

    # 获取ui
    def getUI(self):
        return self.ui

    # 设置监听
    @abstractmethod
    def setConnect(self, context: QMainWindow):
        pass
