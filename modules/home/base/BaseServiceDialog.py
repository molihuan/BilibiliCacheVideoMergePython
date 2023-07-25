from PySide6.QtWidgets import QMainWindow, QWidget, QDialog


class BaseServiceDialog(QDialog):
    def __init__(self, mContext=None):
        super().__init__()
        self.mContext = mContext
        self.ui = mContext.ui
        self.setConnect(mContext)

    # 获取上下文
    def getContext(self) -> QMainWindow:
        return self.mContext

    # 获取ui
    def getUI(self):
        return self.ui

    def setConnect(self, mContext: QMainWindow):
        pass
