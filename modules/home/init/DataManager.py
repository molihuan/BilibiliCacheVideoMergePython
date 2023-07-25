


# 数据管理者
from modules.home.base.BaseService import BaseService


class DataManager(BaseService):
    appName = "HLB站缓存合并1.1"

    def __init__(self, mContext):
        super().__init__(mContext)
        self.selfPath: str
        self.cachePath: str
        self.completePath: str
        self.configJsonPath: str
        self.sysFFmpegPath: str
        self.cacheFileTpye = None
