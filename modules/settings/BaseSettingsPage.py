from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog, QLabel, \
    QLineEdit, QSpacerItem, QSizePolicy, QComboBox
# 基础设置页面

from modules.home.base.BaseServiceWidget import BaseServiceWidget
from modules.utils.SysUtils import SysUtils


class BaseSettingsPage(BaseServiceWidget):
    def __init__(self, mContext):
        super().__init__(mContext=mContext)
        # super(QWidget).__init__()

        # QWidget.__init__(self)
        # BaseService.__init__(self, mContext=mContext)

        # BaseService.__init__(self, mContext=mContext)

        self.resize(600, 500)
        self.setWindowTitle("设置")
        # 设置透明icon
        icon = SysUtils.getTransparentIcon()
        self.setWindowIcon(icon)

        self.total_layout = QVBoxLayout()

        # 初始化主布局和底部布局
        self.main_layout = QHBoxLayout()
        self.bottom_layout = QHBoxLayout()

        # 创建标签、编辑框和选择路径按钮
        self.label = QLabel("完成路径(输出路径)：")
        self.edit_line = QLineEdit()
        self.edit_line.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.edit_line.setMinimumSize(0, 30)
        self.select_path_btn = QPushButton("选择路径")
        self.select_path_btn.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.select_path_btn.setMinimumSize(120, 30)
        complete_path = mContext.getCompletePath()
        self.edit_line.setText(complete_path)

        # 将标签、编辑框和选择路径按钮添加到主布局
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.edit_line)
        self.main_layout.addWidget(self.select_path_btn)
        self.total_layout.addLayout(self.main_layout)

        #解密方式选择
        decryptionOptionsLayout = QHBoxLayout()

        decryptionOptionslabel = QLabel("B站电脑客户端缓存解密：")
        decryptionOptionsLayout.addWidget(decryptionOptionslabel)

        self.decryptionOptionsCombobox = QComboBox()
        self.decryptionOptionsCombobox.addItem("方式1")
        self.decryptionOptionsCombobox.addItem("方式2")
        decryptM4sType = mContext.getDecryptM4sType()
        self.decryptionOptionsCombobox.setCurrentText(decryptM4sType)
        self.decryptionOptionsCombobox.setStyleSheet("background-color: rgb(33, 37, 43);")

        self.decryptionOptionsCombobox.currentIndexChanged.connect(self.saveConfigData)
        decryptionOptionsLayout.addWidget(self.decryptionOptionsCombobox)

        central_widget = QWidget()
        central_widget.setLayout(decryptionOptionsLayout)
        self.total_layout.addWidget(central_widget)


        # 创建保存和关闭按钮
        self.save_btn = QPushButton("保存")

        self.save_btn.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.save_btn.setMinimumSize(120, 30)

        self.reset_btn = QPushButton("重置")
        self.reset_btn.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.reset_btn.setMinimumSize(120, 30)
        # 将保存和关闭按钮添加到底部布局
        self.bottom_layout.addStretch(1)
        self.bottom_layout.addWidget(self.reset_btn)
        self.bottom_layout.addWidget(self.save_btn)

        # 创建总布局并添加主布局和底部布局


        self.total_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.total_layout.addLayout(self.bottom_layout)

        # 设置窗口布局
        self.setLayout(self.total_layout)

        # 绑定按钮点击事件
        self.select_path_btn.clicked.connect(self.open_file_dialog)
        # self.close_btn.clicked.connect(self.close)
        self.save_btn.clicked.connect(self.saveConfigData)

    def open_file_dialog(self):
        # 打开文件对话框，选择文件夹
        directory = QFileDialog.getExistingDirectory()

        # 将选中的路径设置到编辑框中
        self.edit_line.setText(directory)

    def saveConfigData(self):
        context = self.getContext()
        context.setCompletePath(self.edit_line.text())
        context.setDecryptM4sType(self.decryptionOptionsCombobox.currentText())
        context.saveConfigData()
        context.Toast.shows("保存成功")

    def ttt(self):
        pass
