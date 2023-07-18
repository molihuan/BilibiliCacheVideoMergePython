import subprocess

from entity.CacheInfo import CacheInfo
from service.base.BaseService import BaseService
from service.base.QDataMainWindow import QDataMainWindow


class FFmpegUtils(BaseService):

    @staticmethod
    def runCommand(content: QDataMainWindow, cacheInfo: CacheInfo, outputAllPath: str, needCover=False):

        ffmpegPath = content.getSysFFmpegPath()
        audioPath = cacheInfo.getAudioPath()
        videoPath = cacheInfo.getVideoPath()

        cmd = f"{ffmpegPath} -i {audioPath} -i {videoPath} -c copy {outputAllPath}"

        if needCover:
            # 强制覆盖
            cmd = f"{ffmpegPath} -f -i {audioPath} -i {videoPath} -c copy {outputAllPath}"

        print(cmd)

        process = subprocess.Popen(cmd, shell=True)
        process.wait()  # 等待命令执行完成
        return_code = process.returncode  # 获取命令的返回值

        if return_code == 0:
            return True
        else:
            return False
