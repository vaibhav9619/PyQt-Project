import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
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
        self.label=QLabel("Please",self)
        self.label.move(50,50)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)

        self.show()
app=QApplication([])
win=window()
app.exec_()