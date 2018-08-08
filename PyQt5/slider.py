import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QSlider,QLineEdit
from PyQt5.QtGui import QPixmap
class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title="PyQt Winndow"
        self.top=100
        self.left=100
        self.height=500
        self.width= 680
        self.setWindowIcon(QtGui.QIcon('coala.jpg'))
        self.Set()
    def Set(self):
        # self.line=QLineEdit(self)
        # self.line.move(200,200)
        self.sl=QSlider(Qt.Horizontal,self)
        self.sl.move(200,450)
        self.label=QLabel(self)
        self.label.setPixmap(QPixmap('vai.jpeg'))
        self.label.setGeometry(60,100,150,120)
        self.sl.valueChanged.connect(self.dsd)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
    def dsd(self,value):
        if value == 0:
            self.label.setPixmap(QPixmap('vai.jpeg'))
            self.label.setGeometry(60,100,150,120)
        elif value >30:
            self.label.setPixmap(QPixmap('save.png'))
            self.label.setGeometry(60, 100, 150, 120)
        elif value >60:
            self.label.setPixmap(QPixmap('delete.png'))
            self.label.setGeometry(60, 100, 150, 120)
        else:
            self.label.setPixmap(QPixmap('copy.png'))
            self.label.setGeometry(60, 100, 150, 120)
app=QApplication([])
win=window()
app.exec_()