from PySide2.QtCore import QUrl
from PySide2.QtMultimedia import QMediaContent, QMediaPlayer
from PySide2.QtMultimediaWidgets import QVideoWidget
from PySide2.QtWidgets import (QMainWindow, QWidget, QPushButton, QApplication, QVBoxLayout)
from PySide2 import QtGui
import sys, os

# -----------SETTINGS---------
VIDEOFILE = 'video.mp4'
VOL = 100

# path to working folder
current_dir = os.path.dirname(os.path.realpath(__file__))

# Window class
class Reminder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Глаза!!!")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{current_dir}/eye.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(f'{current_dir}/{VIDEOFILE}')))
        self.mediaPlayer.setVolume(VOL)
        self.mediaPlayer.stateChanged.connect(self.pl)

        # cancel button
        self.okButton = QPushButton("Хорошо-хорошо")
        self.okButton.clicked.connect(self.ok)

        widget = QWidget(self)
        self.setCentralWidget(widget)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addWidget(self.okButton)

        widget.setLayout(layout)
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.play()

    def ok(self):
        self.mediaPlayer.stop()
        self.close()

    def pl(self):
        if self.mediaPlayer.position() >= self.mediaPlayer.duration():
            self.mediaPlayer.play()

app = QApplication(sys.argv)
reminder = Reminder()
# window size
reminder.resize(640, 400)
reminder.show()
sys.exit(app.exec_())

