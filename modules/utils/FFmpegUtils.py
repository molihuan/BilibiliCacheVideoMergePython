import os
import subprocess

from modules.entity.CacheInfo import CacheInfo
from modules.service.base.BaseService import BaseService


class FFmpegUtils(BaseService):

    @staticmethod
    def runCommand(content, cacheInfo: CacheInfo, outputAllPath: str):

        ffmpegPath = content.getSysFFmpegPath()
        outputAllPath = outputAllPath
        blvPathList = cacheInfo.getBlvPathList()

        if blvPathList is None:
            audioPath = cacheInfo.getAudioPath()
            videoPath = cacheInfo.getVideoPath()
            
            cmd = f"{ffmpegPath} -i {audioPath} -i {videoPath} -c copy -y {outputAllPath}"
        else:
            srcDir = os.path.dirname(blvPathList[0])
            blvTxtPath = os.path.join(srcDir, "blv.txt")

            with open(blvTxtPath, "w") as file:
                for item in blvPathList:
                    file.write(f"file '{item}'\n")

            cmd = f"{ffmpegPath} -f concat -safe 0 -i {blvTxtPath} -c copy -y {outputAllPath}"

        print(cmd)

        process = subprocess.Popen(cmd, shell=True)
        process.wait()  # 等待命令执行完成
        return_code = process.returncode  # 获取命令的返回值

        if return_code == 0:
            return True
        else:
            return False
