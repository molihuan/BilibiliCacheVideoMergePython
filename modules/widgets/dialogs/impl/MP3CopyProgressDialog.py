from modules.widgets.dialogs.BaseProgressDialog import BaseProgressDialog


class MP3CopyProgressDialog(BaseProgressDialog):

    def __init__(self, context, title="提取进度", content=""):
        super().__init__(context, title, content)

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
            f"总共缓存:{self.totalSelectCacheDirCount},有效缓存:{self.effectiveCacheDirCount}\n正在提取第{index + 1}个文件中的音频")
