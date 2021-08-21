#!/bin/python3
from PySide2.QtCore import QUrl, Qt
from PySide2.QtMultimedia import QMediaContent, QMediaPlayer
from PySide2.QtMultimediaWidgets import QVideoWidget
from PySide2.QtWidgets import (QMainWindow, QWidget, QPushButton, QApplication, QVBoxLayout)
from PySide2 import QtGui
from datetime import datetime, time, timedelta
import sys, os, time, configparser

# -----------SETTINGS---------
config = configparser.ConfigParser()
config.read("settings.ini")  # read config
VIDEOFILE = config['SETTINGS']['videofile'] #get video file
VOL = int(config['SETTINGS']['volume'])     #get volume
RESPONSE_PERIOD = int(config['SETTINGS']['response_period']) #get response period (time "+")

# path to working folder
current_dir = os.path.dirname(os.path.realpath(__file__))

app = QApplication(sys.argv)

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

def update_time():
    response_time = datetime.now() + timedelta(minutes=RESPONSE_PERIOD)
    mainloop(response_time)

def mainloop(rt):
    while True:
        if rt <= datetime.now():
            show_window()
            update_time()
        time.sleep(1)


def show_window():
    reminder = Reminder()
    reminder.setWindowFlag(Qt.WindowStaysOnTopHint)
    # window size
    reminder.resize(640, 400)
    reminder.show()
    app.exec_()

if __name__ == "__main__":
    update_time()

