from urllib.request import urlopen

from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QTableWidget


class ImageLoader(QObject):
    signal = Signal(QTableWidget, int, int, QPixmap)

    def __init__(self, table, image_url, row, column, parent=None):
        super().__init__(parent)
        self.table = table
        self.image_url = image_url
        self.row = row
        self.column = column

    def load(self):
        try:


            image_data = urlopen(self.image_url).read()

            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            self.signal.emit(self.table, self.row, self.column, pixmap)
        except Exception as e:
            print(f"Error loading image: {e}")


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
