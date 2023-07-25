from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QProgressBar, QPushButton, QVBoxLayout, QLabel


from modules.home.base.BaseServiceDialog import BaseServiceDialog


class BaseProgressDialog(BaseServiceDialog):
    def __init__(self, mContext, title="", content=""):
        super().__init__(mContext=mContext)

        self.setWindowTitle(title)
        self.contentLabel = QLabel(content)
        self.contentLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar = QProgressBar()
        self.progressBar.setValue(0)
        self.progressBar.valueChanged.connect(self.handleValueChanged)
        self.cancelBtn = QPushButton("取消")
        self.cancelBtn.clicked.connect(self.cancel)

        layout = QVBoxLayout()
        layout.addWidget(self.contentLabel)
        layout.addWidget(self.progressBar)
        layout.addWidget(self.cancelBtn)
        self.setLayout(layout)

        self.cancelled = False

    def handleValueChanged(self, value):
        if value == 100:
            self.cancelBtn.setText("关闭")
        pass

    def setContent(self, value):
        self.contentLabel.setText(value)

    def setProgress(self, value):
        self.progressBar.setValue(value)

    def cancel(self):
        if self.cancelBtn.text() == "取消":
            self.cancelled = True
        else:
            self.close()

    # 关闭之前调用
    def closeEvent(self, event):
        # 在窗口关闭之前执行自定义方法
        self.reset()
        # 调用父类的closeEvent方法，实现正常的窗口关闭行为
        super().closeEvent(event)

    def reset(self):
        self.setWindowTitle("")
        self.contentLabel.setText("")
        self.progressBar.setValue(0)
        self.cancelBtn.setText("取消")
