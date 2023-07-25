import fileinput
import sys


class UiResource():
    @staticmethod
    def doConnect(filePath='modules/ui_main.py'):

        # 定义替换的内容
        search_text = 'import rc_resources'
        replace_text = 'from .resources_rc import *'

        # 替换或添加import语句
        file_modified = False
        for line in fileinput.input(filePath, inplace=True):
            if search_text in line:
                line = line.replace(search_text, replace_text, 1)
                file_modified = True
            if replace_text in line:
                file_modified = True
            sys.stdout.write(line)

        # 添加import语句
        if not file_modified:
            with open(filePath, 'r') as file:
                content = file.readlines()

            with open(filePath, 'w') as file:
                file.write(f"{replace_text}\n")
                file.writelines(content)

    @staticmethod
    def useCosumeWidget(filePath='modules/ui_main.py'):

        # 定义替换的内容
        search_text = "self.work_page = QWidget()"
        replace_text = "self.work_page = WorkPageWidget(self)"

        # 替换或添加import语句
        file_modified = False
        for line in fileinput.input(filePath, inplace=True):
            if search_text in line:
                line = line.replace(search_text, replace_text, 1)
                file_modified = True
            if replace_text in line:
                file_modified = True
            sys.stdout.write(line)
        if file_modified:
            print(f"成功将===={search_text}修改为：{replace_text}\n请手动引入模块")
        else:
            print(f"失败将===={search_text}修改为：{replace_text}\n图标可能无法显示")


# 链接ui和资源文件脚本
if __name__ == "__main__":
    UiResource.doConnect('../modules/framework/ui_main.py')
    # UiResource.useCosumeWidget('../modules/ui_main.py')
