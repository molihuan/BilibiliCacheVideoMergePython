from PySide6.QtCore import Qt

from service.base.BaseService import BaseService
from views.SettingsView import SettingsView


class StartGroup(BaseService):

    def __init__(self, context):
        super().__init__(context)
        context.ui.exitItem.triggered.connect(self.handleExit)
        context.ui.settingItem.triggered.connect(self.openSettingsView)

    # 退出程序
    def handleExit(self):
        self.getContext().close()

    # 打开设置页面
    def openSettingsView(self):
        context = self.getContext()
        if not context.SettingsView:
            # 实例化窗口
            context.SettingsView = SettingsView(context)
        context.SettingsView.setWindowModality(Qt.ApplicationModal)  # 设置窗口二为模态窗口
        context.SettingsView.show()

        # dialog = self.getContext().Dialog
        # dialog.shows("已存在,是否覆盖", lambda: print(9999), lambda: dialog.close())
