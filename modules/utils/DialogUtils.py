from PySide6.QtWidgets import QVBoxLayout, QLabel, QSizePolicy, QHBoxLayout, QPushButton, QDialog

from modules.home.base.BaseService import BaseService
from modules.home.base.BaseServiceDialog import BaseServiceDialog
from modules.utils.SysUtils import SysUtils


class DialogUtils(BaseServiceDialog):

    def __init__(self, mContext):
        super().__init__(mContext=mContext)
        # 设置透明icon
        icon = SysUtils.getTransparentIcon()
        self.setWindowIcon(icon)
        # 设置对话框布局
        layout = QVBoxLayout()

        # 设置内容标签
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)  # 设置水平和垂直扩展策略
        layout.addWidget(self.label)

        # 设置按钮布局
        self.button_layout = QHBoxLayout()

        # 添加"是"按钮并设置点击回调事件
        self.yes_button = QPushButton("是")

        self.button_layout.addWidget(self.yes_button)

        # 添加"否"按钮并设置点击回调事件
        self.no_button = QPushButton("否")

        self.button_layout.addWidget(self.no_button)

        # 将按钮布局添加到主布局中
        layout.addLayout(self.button_layout)

        self.setLayout(layout)

    def shows(self, content=None, yes_callback=None, no_callback=None, title="提示") -> None:

        self.setWindowTitle(title)
        self.label.setText(content)
        self.yes_button.clicked.connect(yes_callback)
        if no_callback:
            self.no_button.clicked.connect(no_callback)
            self.no_button.show()
            self.yes_button.setText("是")
        else:
            self.no_button.hide()
            self.yes_button.setText("确定")
        self.show()
