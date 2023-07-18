from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog, QLabel, \
    QLineEdit, QSpacerItem, QSizePolicy

from service.base.BaseService import BaseService
from service.base.QDataMainWindow import QDataMainWindow
from utils.SysUtils import SysUtils


class SettingsView(QWidget, BaseService):
    def __init__(self, context):
        super().__init__(context=context)
        self.resize(600, 500)
        self.setWindowTitle("设置")
        # 设置透明icon
        icon = SysUtils.getTransparentIcon()
        self.setWindowIcon(icon)

        # 初始化主布局和底部布局
        self.main_layout = QHBoxLayout()
        self.bottom_layout = QHBoxLayout()

        # 创建标签、编辑框和选择路径按钮
        self.label = QLabel("完成路径(输出路径)：")
        self.edit_line = QLineEdit()
        self.select_path_btn = QPushButton("选择路径")

        complete_path = context.getCompletePath()
        self.edit_line.setText(complete_path)

        # 将标签、编辑框和选择路径按钮添加到主布局
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.edit_line)
        self.main_layout.addWidget(self.select_path_btn)

        # 创建保存和关闭按钮
        self.save_btn = QPushButton("保存")
        self.close_btn = QPushButton("关闭")

        # 将保存和关闭按钮添加到底部布局
        self.bottom_layout.addStretch(1)
        self.bottom_layout.addWidget(self.save_btn)
        self.bottom_layout.addWidget(self.close_btn)

        # 创建总布局并添加主布局和底部布局
        self.total_layout = QVBoxLayout()
        self.total_layout.addLayout(self.main_layout)
        self.total_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.total_layout.addLayout(self.bottom_layout)

        # 设置窗口布局
        self.setLayout(self.total_layout)

        # 绑定按钮点击事件
        self.select_path_btn.clicked.connect(self.open_file_dialog)
        self.close_btn.clicked.connect(self.close)
        self.save_btn.clicked.connect(self.saveConfigData)

    def open_file_dialog(self):
        # 打开文件对话框，选择文件夹
        directory = QFileDialog.getExistingDirectory()

        # 将选中的路径设置到编辑框中
        self.edit_line.setText(directory)

    def saveConfigData(self):
        context: QDataMainWindow = self.getContext()
        context.setCompletePath(self.edit_line.text())
        context.saveConfigData()
        context.Toast.shows("保存成功")
