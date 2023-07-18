import unicodedata


class StrUtils():
    # 检查是否存在中文
    @staticmethod
    def contains_chinese(str):
        for ch in str:
            name = unicodedata.name(ch)
            if "CJK UNIFIED" in name \
                    or "CJK COMPATIBILITY" in name:
                return True
        return False

    @staticmethod
    def has_whitespace(string):
        if not string:
            return False
        for char in string:
            if char.isspace():
                return True
        return False

    # 检查路径是否合规
    @staticmethod
    def isPathConforms(context, pathdict) -> bool:
        dialog = context.Dialog
        for key, value in pathdict.items():
            if not key:
                dialog.shows(value + ':' + "\n为空", lambda: dialog.close())
                return False
            if StrUtils.has_whitespace(key):
                dialog.shows(value + ':' + key + "\n中存在空格,请修改", lambda: dialog.close())
                return False
        return True
