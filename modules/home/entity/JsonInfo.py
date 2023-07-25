class JsonInfo:
    __title: str
    __subTitle: str

    __cover: str
    __avid: str
    __cid: str
    __bvid: str

    def __init__(self, title=None, subTitle=None, bvid=None, avid=None, cid=None, cover=None):
        self.__title = str(title)
        self.__subTitle = str(subTitle)
        self.__bvid = str(bvid)
        self.__avid = str(avid)

        self.__cid = str(cid)
        self.__cover = str(cover)

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = str(title)
        return self

    def get_cover(self):
        return self.__cover

    def set_cover(self, cover):
        self.__cover = str(cover)
        return self

    def get_avid(self):
        return self.__avid

    def set_avid(self, avid):
        self.__avid = str(avid)
        return self

    def get_cid(self):
        return self.__cid

    def set_cid(self, cid):
        self.__cid = str(cid)
        return self

    def get_bvid(self):
        return self.__bvid

    def set_bvid(self, bvid):
        self.__bvid = str(bvid)
        return self

    def get_subTitle(self):
        return self.__subTitle

    def set_subTitle(self, subTitle):
        self.__subTitle = str(subTitle)
        return self

    def __str__(self):
        fields = []
        if self.__title is not None:
            fields.append(f"__title: {self.__title}")
        if self.__cover is not None:
            fields.append(f"__cover: {self.__cover}")
        if self.__avid is not None:
            fields.append(f"__avid: {self.__avid}")
        if self.__cid is not None:
            fields.append(f"__cid: {self.__cid}")
        if self.__part is not None:
            fields.append(f"__part: {self.__part}")
        if self.__bvid is not None:
            fields.append(f"__bvid: {self.__bvid}")
        if self.__subTitle is not None:
            fields.append(f"__subTitle: {self.__subTitle}")
        return f"JsonInfo({', '.join(fields)})"
