import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidget

from modules.service.base.BaseService import BaseService



# 数据表格上一栏
from modules.service.dataarea.DataShowManage import DataShowManage, DataPageType
from modules.utils.PathUtils import PathUtils


class CacheAraeAdjust(BaseService):
    def __init__(self, context):
        super().__init__(context)

    def setConnect(self, context):
        ui = self.getUI()
        ui.refreshBtn.clicked.connect(self.handleRefresh)
        ui.completeFileBtn.clicked.connect(self.openComplete)
        ui.selectAllBtn.clicked.connect(self.handleSelectAll)
        ui.goBackBtn.clicked.connect(self.handleGoBack)

    # 返回上一级
    def handleGoBack(self):
        context = self.getContext()
        manage: DataShowManage = context.DataShowManage
        if manage.dataPageType == DataPageType.COLLECTION_PAGE:
            return
        elif manage.dataPageType == DataPageType.CHAPTER_PAGE:
            manage.showDataPageByFileStructure(os.path.dirname(context.getCachePath()))

    # 处理全选
    def handleSelectAll(self):
        context = self.getContext()
        manage: DataShowManage = context.DataShowManage
        cacheDataList = manage.cacheDataList
        ui = self.getUI()
        btn = ui.selectAllBtn
        dataList: QTableWidget = ui.dataTableWidget
        rowCount = len(cacheDataList)
        print(rowCount)
        if btn.text() == '全选':
            # manage.selectedCacheList = list(cacheDataList)
            for row in range(rowCount):
                dataList.item(row, 0).setCheckState(Qt.CheckState.Checked)
            btn.setText("取消全选")
        else:
            # manage.selectedCacheList.clear()
            for row in range(rowCount):
                dataList.item(row, 0).setCheckState(Qt.CheckState.Unchecked)
            btn.setText("全选")

    # 打开合并完成目录
    def openComplete(self):
        context = self.getContext()
        PathUtils.openPathByFileManager(context.getCompletePath())

    # 刷新列表
    # 获取数据
    # 显示到UI
    def handleRefresh(self):
        context = self.getContext()
        manage: DataShowManage = context.DataShowManage

        if manage.dataPageType == DataPageType.COLLECTION_PAGE:
            manage.showDataPageByFileStructure(context.getCachePath())
            pass
        elif manage.dataPageType == DataPageType.CHAPTER_PAGE:
            manage.showDataPageByFileStructure(context.getCachePath())
            pass
        # dataList: QTableWidget = context.ui.dataTableWidget
