import os
import threading
from enum import Enum
from typing import List

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QMainWindow

from entity.CacheInfo import CacheInfo
from service.base.BaseService import BaseService
from service.base.QDataMainWindow import QDataMainWindow
from ui.MImageLabel import ImageLoader, MImageLabel
from utils.CommonUtils import CommonUtils
from utils.JsonUtils import JsonUtils
from utils.PathUtils import PathUtils, CacheCompleteState


class DataPageType(Enum):
    # 合集页
    COLLECTION_PAGE = 0
    # 章节页
    CHAPTER_PAGE = 1


# 列表数据
class DataShowManage(BaseService):
    def __init__(self, context):
        super().__init__(context)
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

    # 显示数据页面根据文件结构
    def showDataPageByFileStructure(self, cachePath):

        context: QDataMainWindow = self.getContext()
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

    def showCollectionDataPage(self, cachePath):

        self.dataPageType = DataPageType.COLLECTION_PAGE
        self.pageIndex = 1
        self.clearDataList()

        context = self.getContext()
        ui = self.getUI()
        dataListWidget: QTableWidget = ui.dataTableWidget

        chapterPaths = self.getFirstDataPageData(cachePath)

        # chapterPaths = dataPageData
        realIndex = 0
        for index, item in enumerate(chapterPaths):
            info = self.getCacheInfo(item)

            status = PathUtils.verifyCacheFileComplete(info)

            if CacheCompleteState.AUDIODELETION in status or CacheCompleteState.VIDEODELETION in status:
                print(f"粗略检查文件夹:{item}\n------缺少audio.m4s或video.m4s文件")
                if CacheCompleteState.JSONDELETION in status:
                    print(f"粗略检查文件夹:{item}\n------缺少entry.json文件")
                    json_info = JsonUtils.getUUIDJson()
                else:
                    # 解析json
                    json_info = JsonUtils.parse_json(info.getJsonPath())
            elif CacheCompleteState.JSONDELETION in status:
                print(f"粗略检查文件夹:{item}\n------缺少entry.json文件")
                json_info = JsonUtils.getUUIDJson()
            else:
                json_info = JsonUtils.parse_json(info.getJsonPath())

            # 获取父目录
            info.setPath(os.path.dirname(item))
            info.setTitle(json_info.get_subTitle())
            info.setDirName(json_info.get_title())

            info.setChecked(False)
            info.setIndex(realIndex)
            self.cacheDataList.append(info)

            dataItem = QTableWidgetItem(info.getDirName())
            dataListWidget.setItem(realIndex, 0, dataItem)
            dataItem.setTextAlignment(Qt.AlignCenter)  # 设置单元格内容居中对齐
            dataItem.setCheckState(Qt.CheckState.Unchecked)

            dataItem = QTableWidgetItem(info.getPath())
            dataListWidget.setItem(realIndex, 1, dataItem)
            # 加载封面
            loader = ImageLoader(dataListWidget, json_info.get_cover(), realIndex, 2)
            loader.signal.connect(self.handleImageLoaded)
            thread = threading.Thread(target=loader.load)
            thread.start()

            realIndex += 1

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

        chapterPaths = self.getSecondDataPageData(collectionPath)
        realIndex = 0
        for index, item in enumerate(chapterPaths):
            info = self.getCacheInfo(item)

            status = PathUtils.verifyCacheFileComplete(info)

            if CacheCompleteState.AUDIODELETION in status or CacheCompleteState.VIDEODELETION in status:
                print(f"粗略检查文件夹:{item}\n------缺少audio.m4s或video.m4s文件")
                if CacheCompleteState.JSONDELETION in status:
                    print(f"粗略检查文件夹:{item}\n------缺少entry.json文件")
                    json_info = JsonUtils.getUUIDJson()
                else:
                    # 解析json
                    json_info = JsonUtils.parse_json(info.getJsonPath())
            elif CacheCompleteState.JSONDELETION in status:
                print(f"粗略检查文件夹:{item}\n------缺少entry.json文件")
                json_info = JsonUtils.getUUIDJson()
            else:
                json_info = JsonUtils.parse_json(info.getJsonPath())

            # info.setPath(os.path.dirname(item))

            info.setPath(item)

            info.setTitle(json_info.get_subTitle())
            info.setDirName(json_info.get_title())

            info.setChecked(False)
            info.setIndex(realIndex)
            self.cacheDataList.append(info)

            dataItem = QTableWidgetItem(info.getTitle())
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
        # print(item.checkState(), item.text())
        if item.checkState() == Qt.CheckState.Checked:
            selectList.append(dataList[item.row()])

        elif item.checkState() == Qt.CheckState.Unchecked:
            if dataList[item.row()] in selectList:
                selectList.remove(dataList[item.row()])

        print("选择数量", len(self.selectedCacheList))

        ui = self.getUI()
        btn = ui.selectAllBtn

        if len(selectList) == len(dataList) and len(dataList) != 0:
            btn.setText("取消全选")
        if len(selectList) == 0 and len(dataList) != 0:
            btn.setText("全选")

    # 获取第一屏的数据
    def getFirstDataPageData(self, cachePath):
        context: QDataMainWindow = self.getContext()
        chapterPaths = self.getAllOneChapterPath(cachePath)
        return chapterPaths
        pass

    # 获取第二屏的数据
    def getSecondDataPageData(self, collectionPath):
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
            print("文件夹不完整")
        else:
            chapterPaths += sub_dir
        return chapterPaths

    # 获取一个合集里的一个章节路径
    def getOneChapterPathByCollection(self, collectionPath):
        sub_dir = PathUtils.listSubDir(collectionPath)
        chapterPath = []
        if len(sub_dir) <= 0:
            print("文件夹不完整")
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

    # 通过章节路径获取缓存信息audio、video
    def getCacheInfo(slef, chapterPath) -> CacheInfo:
        info = CacheInfo()
        CacheInfoDict = {
            "audio": "audio.m4s",
            "video": "video.m4s",
            "json": "entry.json",
            "danmaku": "danmaku.xml",
        }

        for root, dirs, files in os.walk(chapterPath):
            for file in files:
                file_path = str(os.path.join(root, file))

                if file_path.endswith(CacheInfoDict.get("json")):
                    info.setJsonPath(file_path)
                elif file_path.endswith(CacheInfoDict.get("danmaku")):
                    info.setDanmakuPath(file_path)
                elif file_path.endswith(CacheInfoDict.get("audio")):
                    info.setAudioPath(file_path)
                elif file_path.endswith(CacheInfoDict.get("video")):
                    info.setVideoPath(file_path)
        return info
