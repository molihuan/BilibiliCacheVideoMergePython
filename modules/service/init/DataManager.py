from modules.service.base.BaseService import BaseService


# 数据管理者
class DataManager(BaseService):
    appName = "HLB站缓存合并1.1"

    def __init__(self, context):
        super().__init__(context)
        self.selfPath: str
        self.cachePath: str
        self.completePath: str
        self.configJsonPath: str
        self.sysFFmpegPath: str
        self.cacheFileTpye = None
