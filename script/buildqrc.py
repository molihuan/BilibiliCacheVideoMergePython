import os
# 编译资源文件
if __name__ =="__main__":
    cmd = "pyside6-rcc ../modules/framework/resources.qrc -o ../modules/framework/resources_rc.py"
    os.system(cmd)