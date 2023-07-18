from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class MImageLabel(QWidget):
    def __init__(self, pixmap: QPixmap, text: str):
        super().__init__()
        layout = QVBoxLayout(self)

        pixmap = pixmap.scaled(200, 100)  # 使用scaled方法调整大小
        image = QLabel()
        image.setPixmap(pixmap)
        image.setFixedSize(200, 100)

        title = QLabel(text)

        layout.addWidget(image)
        layout.addWidget(title)

        self.setLayout(layout)
