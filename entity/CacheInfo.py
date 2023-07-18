class CacheInfo():
    __danmakuPath: str
    __jsonPath: str
    __audioPath: str
    __videoPath: str
    __blvPath: str

    __checked: bool
    __title: str
    __path: str
    __parentPath: str

    __index: int

    __dirName: str

    def __init__(self, danmakuPath=None, jsonPath=None, audioPath=None, videoPath=None, blvPath=None):
        self.__danmakuPath = str(danmakuPath) if danmakuPath is not None else None
        self.__jsonPath = str(jsonPath) if jsonPath is not None else None
        self.__audioPath = str(audioPath) if audioPath is not None else None
        self.__videoPath = str(videoPath) if videoPath is not None else None
        self.__blvPath = str(blvPath) if blvPath is not None else None
        self.__checked = None
        self.__title = None
        self.__path = None
        self.__parentPath = None
        self.__index = -1
        self.__dirName = ''

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

    def getAudioPath(self):
        return self.__audioPath

    def setVideoPath(self, values):
        self.__videoPath = values
        return self

    def getVideoPath(self):
        return self.__videoPath

    def setBlvPath(self, values):
        self.__blvPath = values
        return self

    def getBlvPath(self):
        return self.__blvPath

    def setChecked(self, value):
        self.__checked = value
        return self

    def isChecked(self):
        return self.__checked

    def setTitle(self, value):
        self.__title = value
        return self

    def getTitle(self):
        return self.__title

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

    def setIndex(self, value):
        self.__index = value
        return self

    def getIndex(self):
        return self.__index

    def setDirName(self, value):
        self.__dirName = value
        return self

    def getDirName(self):
        return self.__dirName

    def __str__(self):
        fields = []
        for field_name in dir(self):
            if not field_name.startswith("__"):
                field_value = getattr(self, field_name)
                if field_value is not None:
                    fields.append(f"{field_name}={field_value}")
        return f"CacheInfo({', '.join(fields)})"
