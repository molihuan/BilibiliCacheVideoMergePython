from PySide6.QtWidgets import QDialog, QProgressBar, QPushButton, QVBoxLayout

from service.base.BaseService import BaseService


class FFmpegProgressDialog(QDialog, BaseService):
    def __init__(self, context):
        super().__init__(context=context)

        self.setWindowTitle("Progress")

        self.progress_bar = QProgressBar()
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.cancel)

        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.cancel_button)
        self.setLayout(layout)

        self.cancelled = False

    def setProgress(self, value):
        self.progress_bar.setValue(value)

    def cancel(self):
        self.cancelled = True
