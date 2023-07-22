import os
# 编译资源文件
if __name__ =="__main__":
    cmd = "pyside6-rcc ../modules/resources.qrc -o ../modules/resources_rc.py"
    os.system(cmd)