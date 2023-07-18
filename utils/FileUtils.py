import os


class FileUtils:
    def t1(s):
        pass

    @staticmethod
    def deleteFile(path):
        try:
            os.remove(path)
        except OSError as e:
            print("文件删除失败:", e)

    # 获取文件夹下唯一的文件名
    @staticmethod
    def getUniqueFileName(filename):
        directory = os.path.dirname(filename)

        index = 0
        base_name, extension = os.path.splitext(filename)
        new_filename = filename

        while os.path.exists(os.path.join(directory, new_filename)):
            index += 1
            new_filename = f"{base_name}({index}){extension}"

        return new_filename
