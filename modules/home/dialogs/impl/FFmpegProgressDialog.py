from modules.home.dialogs.BaseProgressDialog import BaseProgressDialog


class FFmpegProgressDialog(BaseProgressDialog):

    def __init__(self, mContext, title="合并进度", content=""):
        super().__init__(mContext, title, content)

        # 勾选的cache数量
        self.totalSelectCacheDirCount = None
        # 有效的缓存数量
        self.effectiveCacheDirCount = None

    def setCacheDirCount(self, totalSelectCacheDirCount, effectiveCacheDirCount):
        # 勾选的cache数量
        self.totalSelectCacheDirCount = totalSelectCacheDirCount
        # 有效的缓存数量
        self.effectiveCacheDirCount = effectiveCacheDirCount

    def renewContent(self, index):
        self.setContent(
            f"总共缓存:{self.totalSelectCacheDirCount},有效缓存:{self.effectiveCacheDirCount}\n正在合并第{index + 1}个")
