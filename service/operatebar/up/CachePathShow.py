from PySide6.QtWidgets import QMainWindow

from service.base.BaseService import BaseService
from service.base.QDataMainWindow import QDataMainWindow
from utils.CallbackUtils import PathSelectCallCode
from utils.PathUtils import PathUtils


class CachePathShow(BaseService):

    def __init__(self, context):
        super().__init__(context)

    def setConnect(self, context: QMainWindow):
        self.ui = self.getUI()
        self.context = self.getContext()
        self.ui.selectVedioDirBtn.clicked.connect(
            lambda: PathUtils.openPathSelector(self.callbackSelectedPath, PathSelectCallCode.CACHEPATH))
        self.ui.vedioDirShowLineEdit.textChanged.connect(self.handleTextChanged)

    # 文件选择器回调
    def callbackSelectedPath(self, path, fromCode: PathSelectCallCode):
        context: QDataMainWindow = self.getContext()
        if fromCode == PathSelectCallCode.CACHEPATH:
            context.DataShowManage.showDataPageByFileStructure(path)

    def handleTextChanged(self):
        text = self.ui.vedioDirShowLineEdit.text()
        self.context.cachePath = text
        print(text)
