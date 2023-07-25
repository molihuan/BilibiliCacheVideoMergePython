from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtWidgets import QWidget, QFileDialog

from modules.player.ui_player import Ui_PlayerWidget
from modules.utils.PathUtils import PathUtils


class PlayerPage(QWidget):
    def __init__(self, configManager):
        super().__init__()
        self.configManager = configManager
        self.ui = Ui_PlayerWidget()
        self.ui.setupUi(self)
        self.player = QMediaPlayer(self)
        self.audioOutput = QAudioOutput()
        self.player.setVideoOutput(self.ui.videoWidget)
        self.ui.btnPlay.clicked.connect(self.sel)

    def sel(self):
        PathUtils.openPathSelector(self.handle, 1, QFileDialog.FileMode.AnyFile)
        pass

    def handle(self, path, code):
        file = QUrl.fromLocalFile(path[0])
        self.player.setAudioOutput(self.audioOutput)
        self.player.setSource(file)
        self.player.play()
        pass
