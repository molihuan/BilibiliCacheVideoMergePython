import os
from enum import Enum
from typing import List

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QMainWindow

from modules.home.base.BaseService import BaseService
from modules.home.entity.CacheInfo import CacheInfo
from modules.home.ui.MImageLabel import MImageLabel
from modules.utils.CommonUtils import CommonUtils
from modules.utils.FileUtils import FileUtils
from modules.utils.JsonUtils import JsonUtils
from modules.utils.Log import Log
from modules.utils.PathUtils import PathUtils


class DataPageType(Enum):
    # 合集页
    COLLECTION_PAGE = 0
    # 章节页
    CHAPTER_PAGE = 1


class CacheFileTpye(Enum):
    PC = 0
    PHONE = 1


# 列表数据
class DataShowManager(BaseService):
    def __init__(self, mContext):
        super().__init__(mContext)
        # 页面是在合集页还是章节页
        self.dataPageType = DataPageType.COLLECTION_PAGE
        # 读取到的所有缓存文件
        self.cacheDataList: List[CacheInfo] = list()
        # 勾选的缓存文件
        self.selectedCacheList: List[CacheInfo] = list()
        # 进行分页的索引
        self.pageIndex = 1

    # 设置监听
    def setConnect(self, context: QMainWindow):
        ui = self.getUI()
        dataListWidget: QTableWidget = ui.dataTableWidget
        # 勾选状态改变监听
        dataListWidget.itemChanged.connect(self.handItemChange)
        dataListWidget.itemDoubleClicked.connect(self.handItemDoubleClick)

    # 是否是集合页面
    def isCollectionPage(self):
        if self.dataPageType == DataPageType.COLLECTION_PAGE:
            return True
        else:
            return False

    # 处理item双击
    def handItemDoubleClick(self, item: QTableWidgetItem):
        if self.isCollectionPage():
            cacheInfo = self.cacheDataList[item.row()]
            self.showDataPageByFileStructure(cacheInfo.getPath())

    # 清理所有的数据
    def clearDataList(self):
        ui = self.getUI()
        dataListWidget: QTableWidget = ui.dataTableWidget
        if len(self.cacheDataList) != 0:
            dataListWidget.clear()
            self.cacheDataList.clear()
            self.selectedCacheList.clear()
            dataListWidget.setHorizontalHeaderLabels(["标题", "路径"])

    # 根据文件结构显示数据页面
    def showDataPageByFileStructure(self, cachePath):

        if cachePath == "" or cachePath is None:
            return

        context = self.getContext()
        context.setCachePath(cachePath)

        edit = self.getUI().vedioDirShowLineEdit
        edit.setText(cachePath)

        subDirList = PathUtils.listSubDir(cachePath)
        if CommonUtils.isListEmpty(subDirList):
            self.clearDataList()
            return
        thrFileList = PathUtils.listSubFile(subDirList[0])

        for filePath in thrFileList:
            if filePath.endswith("entry.json"):
                context.setCacheFileTpye(CacheFileTpye.PHONE)
                self.showChapterDataPage(cachePath)
                return
            if filePath.endswith(".videoInfo"):
                context.setCacheFileTpye(CacheFileTpye.PC)
                self.showChapterDataPage(cachePath)
                return
        thrDirList = PathUtils.listSubDir(subDirList[0])
        if CommonUtils.isListEmpty(thrDirList):
            self.clearDataList()
            return
        forFileList = PathUtils.listSubFile(thrDirList[0])
        if CommonUtils.isListEmpty(forFileList):
            self.clearDataList()
            return
        for filePath in forFileList:
            if filePath.endswith("entry.json"):
                self.showCollectionDataPage(cachePath)
                return

    # 显示合集页面
    def showCollectionDataPage(self, cachePath):

        self.dataPageType = DataPageType.COLLECTION_PAGE
        self.pageIndex = 1
        self.clearDataList()

        context = self.getContext()
        ui = self.getUI()
        dataListWidget: QTableWidget = ui.dataTableWidget

        chapterPaths = self.getCollectionPageData(cachePath)

        # chapterPaths = dataPageData
        realIndex = 0
        for index, item in enumerate(chapterPaths):
            info = self.getCacheInfoByPhone(item)
            json = JsonUtils.parseJson(info)
            # 获取父目录
            info.setPath(os.path.dirname(item))
            info.setSubTitle(json.get_subTitle())
            info.setTitle(json.get_title())
            self.cacheDataList.append(info)

            dataItem = QTableWidgetItem(info.getTitle())
            dataListWidget.setItem(realIndex, 0, dataItem)
            dataItem.setTextAlignment(Qt.AlignCenter)  # 设置单元格内容居中对齐
            dataItem.setCheckState(Qt.CheckState.Unchecked)

            dataItem: QTableWidgetItem = QTableWidgetItem(info.getPath())

            dataListWidget.setItem(realIndex, 1, dataItem)

            # 加载封面
            # loader = ImageLoader(dataListWidget, json_info.get_cover(), realIndex, 2)
            # loader.signal.connect(self.handleImageLoaded)
            # thread = threading.Thread(target=loader.load)
            # thread.start()

            realIndex += 1

        # dataListWidget.resizeRowsToContents()
        # 重新设置单元格大小
        # dataListWidget.resizeColumnsToContents()

    def handleImageLoaded(self, table, row, column, pixmap: QPixmap):
        label = MImageLabel(pixmap, "")
        table.setRowHeight(row, 160)
        table.setColumnWidth(column, 220)
        table.setCellWidget(row, column, label)

    def showChapterDataPage(self, collectionPath):

        self.dataPageType = DataPageType.CHAPTER_PAGE
        self.pageIndex = 1

        self.clearDataList()

        context = self.getContext()
        ui = self.getUI()
        dataListWidget: QTableWidget = ui.dataTableWidget

        chapterPaths = self.getChapterPageData(collectionPath)
        realIndex = 0
        for index, item in enumerate(chapterPaths):

            if context.getCacheFileTpye() == CacheFileTpye.PC:
                info = self.getCacheInfoByPC(item)
            else:
                info = self.getCacheInfoByPhone(item)
            json = JsonUtils.parseJson(info)

            info.setPath(item)

            info.setSubTitle(json.get_subTitle())
            info.setTitle(json.get_title())

            self.cacheDataList.append(info)

            if context.getCacheFileTpye() == CacheFileTpye.PC:
                dataItem = QTableWidgetItem(info.getTitle() + "---" + info.getSubTitle())
            else:
                dataItem = QTableWidgetItem(info.getSubTitle())

            dataListWidget.setItem(realIndex, 0, dataItem)
            dataItem.setTextAlignment(Qt.AlignCenter)  # 设置单元格内容居中对齐
            dataItem.setCheckState(Qt.CheckState.Unchecked)

            dataItem = QTableWidgetItem(item)
            dataListWidget.setItem(realIndex, 1, dataItem)

            realIndex += 1

    # 勾选框改变监听
    def handItemChange(self, item: QTableWidgetItem):

        selectList = self.selectedCacheList
        dataList = self.cacheDataList
        # Log.i(item.checkState(), item.text())
        if item.checkState() == Qt.CheckState.Checked:
            selectList.append(dataList[item.row()])

        elif item.checkState() == Qt.CheckState.Unchecked:
            if dataList[item.row()] in selectList:
                selectList.remove(dataList[item.row()])

        ui = self.getUI()
        btn = ui.selectAllBtn

        if len(selectList) == len(dataList) and len(dataList) != 0:
            btn.setText("取消全选")
        if len(selectList) == 0 and len(dataList) != 0:
            btn.setText("全选")

    # 获取第一屏的数据
    def getCollectionPageData(self, cachePath):
        context = self.getContext()
        chapterPaths = self.getAllOneChapterPath(cachePath)
        return chapterPaths
        pass

    # 获取第二屏的数据
    def getChapterPageData(self, collectionPath):
        chapterPaths = self.getAllChapterPathByCollection(collectionPath)
        return chapterPaths

    # 获取所有合集
    def getAllCollectionPath(self, cachePath):
        sub_dir = PathUtils.listSubDir(cachePath)
        return sub_dir

    # 获取所有的章节路径
    def getAllChapterPath(self, cachePath):
        paths = self.getAllCollectionPath(cachePath)
        allChapterPaths = []
        for item in paths:
            chapterPaths = self.getAllChapterPathByCollection(item)
            allChapterPaths += chapterPaths
        return allChapterPaths

    # 获取一个合集里的所有章节路径
    def getAllChapterPathByCollection(self, collectionPath):
        sub_dir = PathUtils.listSubDir(collectionPath)
        chapterPaths = []
        if len(sub_dir) <= 0:
            Log.i("文件夹不完整")
        else:
            chapterPaths += sub_dir
        return chapterPaths

    # 获取一个合集里的一个章节路径
    def getOneChapterPathByCollection(self, collectionPath):
        sub_dir = PathUtils.listSubDir(collectionPath)
        chapterPath = []
        if len(sub_dir) <= 0:
            Log.i("文件夹不完整")
        else:
            chapterPath.append(sub_dir[0])
        return chapterPath

    # 每一个集合只获取一个章节，用于合集数据页面的展示
    def getAllOneChapterPath(self, cachePath):
        allChapterPath = []
        allCollectionPath = self.getAllCollectionPath(cachePath)
        for collPath in allCollectionPath:
            chapterPath = self.getOneChapterPathByCollection(collPath)
            allChapterPath += chapterPath
        return allChapterPath

    def getCacheInfo(slef, chapterPath) -> CacheInfo:

        pass

    # 通过章节路径获取缓存信息audio、video
    def getCacheInfoByPC(slef, chapterPath) -> CacheInfo:
        info = CacheInfo()
        m4sPathList = []
        for root, dirs, files in os.walk(chapterPath):
            for file in files:
                file_path = str(os.path.join(root, file))

                if file_path.endswith(".videoInfo"):
                    info.setJsonPath(file_path)
                elif file_path.endswith(".m4s"):
                    m4sPathList.append(file_path)
                # elif file_path.endswith("image.jpg"):
                #     info.setVideoPath(file_path)
                elif file_path.endswith("dm1"):
                    info.setDanmakuPath(file_path)
        if len(m4sPathList) == 2:
            temp = FileUtils.compareFileSize(m4sPathList[0], m4sPathList[1])
            if temp:
                info.setVideoPath(m4sPathList[0])
                info.setAudioPath(m4sPathList[1])
            else:
                info.setVideoPath(m4sPathList[1])
                info.setAudioPath(m4sPathList[0])

        return info

    # 通过章节路径获取缓存信息audio、video
    def getCacheInfoByPhone(slef, chapterPath) -> CacheInfo:
        info = CacheInfo()

        blvPathList = []

        for root, dirs, files in os.walk(chapterPath):
            for file in files:
                file_path = str(os.path.join(root, file))

                if file_path.endswith("entry.json"):
                    info.setJsonPath(file_path)
                elif file_path.endswith("danmaku.xml"):
                    info.setDanmakuPath(file_path)
                elif file_path.endswith("audio.m4s"):
                    info.setAudioPath(file_path)
                elif file_path.endswith("video.m4s"):
                    info.setVideoPath(file_path)
                elif file_path.endswith(".blv"):
                    blvPathList.append(file_path)
        if len(blvPathList) > 0:
            info.setBlvPathList(blvPathList)
        return info
