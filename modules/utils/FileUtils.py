import os

from modules.utils.Log import Log


class FileUtils:
    def t1(s):
        pass

    @staticmethod
    def deleteFile(path):
        try:
            os.remove(path)
        except OSError as e:
            Log.i("文件删除失败:", e)

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

    # 解密m4s
    @staticmethod
    def decryptM4s(target_path: str, output_path: str, bufsize: int = 256 * 1024 * 1024) -> None:
        assert bufsize > 0
        with open(target_path, 'rb') as target_file:
            header = target_file.read(32)
            new_header = header.replace(b'000000000', b'')
            new_header = new_header.replace(b'$', b' ')
            new_header = new_header.replace(b'avc1', b'')
            with open(output_path, 'wb') as output_file:
                output_file.write(new_header)
                i = target_file.read(bufsize)
                while i:
                    output_file.write(i)
                    i = target_file.read(bufsize)

    @staticmethod
    def compareFileSize(file1, file2):
        size1 = os.path.getsize(file1)
        size2 = os.path.getsize(file2)

        if size1 > size2:
            return True
        elif size1 < size2:
            return False
        else:
            return False
