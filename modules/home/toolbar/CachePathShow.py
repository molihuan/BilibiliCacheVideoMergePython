from PySide6.QtWidgets import QMainWindow

from modules.home.base.BaseService import BaseService
from modules.home.ui.MlLineEdit import MlLineEdit
from modules.utils.CallbackUtils import PathSelectCallCode
from modules.utils.Log import Log
from modules.utils.PathUtils import PathUtils


class CachePathShow(BaseService):

    def __init__(self, mContext):
        super().__init__(mContext)

    def setConnect(self, context: QMainWindow):
        self.ui = self.getUI()
        self.context = self.getContext()
        self.ui.selectVedioDirBtn.clicked.connect(
            lambda: PathUtils.openPathSelector(self.callbackSelectedPath, PathSelectCallCode.CACHEPATH))

        edit:MlLineEdit = self.ui.vedioDirShowLineEdit
        edit.textChanged.connect(self.handleTextChanged)
        edit.returnPressed.connect(self.handleReturnPressed)

    # 文件选择器回调
    def callbackSelectedPath(self, path, fromCode: PathSelectCallCode):
        context = self.getContext()
        if fromCode == PathSelectCallCode.CACHEPATH:
            context.DataShowManage.showDataPageByFileStructure(path[0])

    def handleTextChanged(self):
        text = self.ui.vedioDirShowLineEdit.text()
        self.context.cachePath = text
        # Log.i(text)
    def handleReturnPressed(self):
        context = self.getContext()
        text = self.ui.vedioDirShowLineEdit.text()
        context.DataShowManage.showDataPageByFileStructure(text)
