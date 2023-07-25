class CacheInfo():
    __checked: bool
    __index: int

    def __init__(self):
        # 路径
        self.__path = None
        self.__parentPath = None
        # 缓存信息
        self.__danmakuPath = None
        self.__jsonPath = None
        self.__audioPath = None
        self.__videoPath = None
        self.__blvPathList = None
        # 主标题（文件夹名）
        self.__title = None
        # 副标题文件名
        self.__subTitle = None

    def setDanmakuPath(self, values):
        self.__danmakuPath = values
        return self

    def getDanmakuPath(self):
        return self.__danmakuPath

    def setJsonPath(self, values):
        self.__jsonPath = values
        return self

    def getJsonPath(self):
        return self.__jsonPath

    def setAudioPath(self, values):
        self.__audioPath = values
        return self

    def getAudioPath(self) -> str:
        return self.__audioPath

    def setVideoPath(self, values):
        self.__videoPath = values
        return self

    def getVideoPath(self) -> str:
        return self.__videoPath

    def setTitle(self, value):
        self.__title = value
        return self

    def getTitle(self):
        return self.__title

    def setSubTitle(self, value):
        self.__subTitle = value
        return self

    def getSubTitle(self):
        return self.__subTitle

    def setPath(self, value):
        self.__path = value
        return self

    def getPath(self):
        return self.__path

    def setParentPath(self, value):
        self.__parentPath = value
        return self

    def getParentPath(self):
        return self.__parentPath

    def setBlvPathList(self, value):
        self.__blvPathList = value
        return self

    def getBlvPathList(self):
        return self.__blvPathList

    def __str__(self):
        fields = []
        for field_name in dir(self):
            if not field_name.startswith("__"):
                field_value = getattr(self, field_name)
                if field_value is not None:
                    fields.append(f"{field_name}={field_value}")
        return f"CacheInfo({', '.join(fields)})"
