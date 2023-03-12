import PyQt5
# importing libraries 
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stopwatch')
        self.setGeometry(100,100,400,500)
        self.ui()
        self.show()
    def ui(self):
        self.count=0
        self.flag=False
        self.label=QLabel(self)
        self.label.setGeometry(75,100,250,70)
        self.label.setStyleSheet('border:4px solid black')
        self.label.setText(str(self.count))
        self.label.setFont(QFont('arial',25))
        self.label.setAlignment(Qt.AlignCenter)
        start=QPushButton('start',self)
        start.setGeometry(125,250,150,40)
        start.pressed.connect(self.start)
        pause=QPushButton('pause',self)
        pause.setGeometry(125,300,150,40)
        pause.pressed.connect(self.pause)
        reset=QPushButton('reset',self)
        reset.setGeometry(125,350,150,40)
        reset.pressed.connect(self.reset)
        timer=QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(100)
    def showtime(self):
        if self.flag==True:
            self.count +=1
        self.label.setText(str(self.count/10))
    def start(self):
        self.flag=True
    def pause(self):
        self.flag=False
    def reset(self):
        self.flag=False
        self.count=0
        self.label.setText(str(self.count))
app=QApplication(sys.argv)
window=Window()
sys.exit(app.exec())