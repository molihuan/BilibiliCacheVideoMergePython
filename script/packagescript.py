import os
import shutil
from enum import Enum
import sys

import PyInstaller.__main__
#///////////////不能改变导入顺序///////////////////////////////
workPath = os.getcwd()
workParentPath = os.path.dirname(workPath)
# 将workParentPath也设置为工作目录
sys.path.append(workParentPath)

from modules.utils.SysUtils import SysType, SysUtils

from script.appDetails import APP_NAME

#//////////////////////////////////////////////


# 未打包路径
ffmpegExePath = os.path.join(workParentPath,"res/ffmpeg/ffmpeg.exe")
# 打包后的路径
ffmpegPackageDir = "./res/ffmpeg"
ffmpegPackageDirUpkg = "./res/ffmpeg/ffmpeg.exe"
pythonMainPath = os.path.join(workParentPath, 'main.py')
outputDir = os.path.join(workPath, "dist")
icoPath =os.path.join(workParentPath,'res/images/images/ml.ico')
macIcoPath =os.path.join(workParentPath,'res/images/images/ml.icns')
themesPath = os.path.join(workParentPath, 'themes')
themesPackageDir = "./themes"

softName = APP_NAME + ".exe"


def beforePkgMac():
    global ffmpegExePath
    global ffmpegPackageDirUpkg
    ffmpegExePath = os.path.join(workParentPath,"res/ffmpeg/ffmpeg-mac")
    ffmpegPackageDirUpkg = "./res/ffmpeg"


def beforePkgLinux():
    global ffmpegExePath
    global ffmpegPackageDirUpkg
    ffmpegExePath = os.path.join(workParentPath, "res/ffmpeg/ffmpeg-linux")
    ffmpegPackageDirUpkg = "./res/ffmpeg/ffmpeg-linux"


class PkgType(Enum):
    PYINSTALLER_PKG = 0
    NUITKA = 1
    NON = 2


# PyInstaller打包
def Ppkg(sysType):
    # 执行打包命令
    cmd = [
        pythonMainPath,  # 指定你的Python脚本文件
        '--add-binary', f'{ffmpegExePath};{ffmpegPackageDir}',  # 将ffmpeg文件复制到指定目录
        '-n', softName,
        '--add-data', f'{themesPath};{themesPackageDir}',
        '-i', icoPath,
        # 前面的顺序不要动
        # '--add-binary', f'{ffmpegExePath}:{ffmpegPackageDir}',  # 将ffmpeg文件夹复制到指定目录
        # '--onefile',  # 打包成一个单独的可执行文件
        '--noconsole',  # 不显示控制台窗口
        '--clean',
        '--distpath', outputDir
    ]
    # 需要打包文件夹
    if sysType == SysType.LINUX:
        cmd[1] = "--add-binary"
        cmd[2] = f'{ffmpegExePath}:{ffmpegPackageDirUpkg}'
        cmd[4] = APP_NAME
        cmd[5] = '--add-data'
        cmd[6] = f'{themesPath}:{themesPackageDir}'
    # 需要打包文件夹
    if sysType == SysType.MAC:
        cmd[1] = "--add-binary"
        cmd[2] = f'{ffmpegExePath}:{ffmpegPackageDirUpkg}'
        cmd[4] = APP_NAME
        cmd[5] = '--add-data'
        cmd[6] = f'{themesPath}:{themesPackageDir}'
        cmd[8] = macIcoPath

    PyInstaller.__main__.run(cmd)


# Nuitka打包
def Npkg(sysType):
    cmd = [
        'nuitka',
        f'--include-data-files={ffmpegExePath}={ffmpegPackageDirUpkg}',
        '-o', softName,
        # 前面的顺序不要动
        # f'--include-data-dir={ffmpegExePath}={ffmpegPackageDirUpkg}',
        # '--onefile'# 打包成一个单独的可执行文件
        f'--include-data-dir={themesPath}={themesPackageDir}',
        '--output-dir=' + outputDir,
        '--windows-icon-from-ico=' + icoPath,
        '--remove-output',
        '--standalone',  # 独立环境
        '--enable-plugin=pyside6',
        '--disable-console',
        '--show-progress',
        # '--windows-icon=' + icoPath,  # 替换为你的图标文件路径

        pythonMainPath
    ]
    # 需要打包文件夹
    if sysType == SysType.LINUX:
        cmd[1] = f'--include-data-dir={ffmpegExePath}={ffmpegPackageDirUpkg}'
        cmd[3] = APP_NAME

    allstr = ''
    for item in cmd:
        allstr = allstr + item + " "
    print(allstr)

    # 执行打包命令
    os.system(allstr)
    # subprocess.run(cmd)


def chooseType(sysType, inType):
    if inType == PkgType.PYINSTALLER_PKG.value:
        # 使用PyInstaller打包工具
        if sysType == SysType.WIN:
            pass
        elif sysType == SysType.MAC:
            beforePkgMac()
        elif sysType == SysType.LINUX:
            beforePkgLinux()
        else:
            print("不支持系统")
            sys.exit()
        Ppkg(sysType)
    elif inType == PkgType.NUITKA.value:
        # 使用Nuitka打包工具
        if sysType == SysType.WIN:
            pass
        elif sysType == SysType.MAC:
            beforePkgMac()
        elif sysType == SysType.LINUX:
            beforePkgLinux()
        else:
            print("不支持系统")
            sys.exit()
        Npkg(sysType)
        pass
    else:
        print("无效的选择")


# 打包脚本
if __name__ == "__main__":
    sysType = SysUtils.getSysType()
    if os.path.exists(outputDir):
        # 删除输出目录
        shutil.rmtree(outputDir)
    print(
        f"请选择打包方式:\n{PkgType.PYINSTALLER_PKG.value}.PyInstaller\n{PkgType.NUITKA.value}.Nuitka\n{PkgType.NON.value}.什么也不做\n请输入前面的序号:")
    inType = int(input())
    # sysType = SysType.MAC
    # sysType = SysType.LINUX
    if inType == PkgType.NON.value:
        exit()
    chooseType(sysType, inType)
