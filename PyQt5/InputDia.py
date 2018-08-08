import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QInputDialog,QPushButton,QLabel
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
        self.label=QLabel(self)
        self.label.move(200,200)
        self.push=QPushButton("click here",self)
        self.push.move(300,400)
        self.push.clicked.connect(self.click)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
    def click(self):
        test,ok=QInputDialog.getText(self,"input dialog","ENter your name")
        if ok:
            self.label.setText(str(test))
app=QApplication([])
win=window()
app.exec_()