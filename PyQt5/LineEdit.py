import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit,QPushButton,QMessageBox
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
        self.lineedit=QLineEdit(self)
        self.lineedit.move(250,300)
        self.lineedit.resize(150,25)

        self.butt=QPushButton("Click",self)
        self.butt.move(270,350)
        self.butt.clicked.connect(self.onClick)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
    def onClick(self):
        textVAL=self.lineedit.text()
        QMessageBox.question(self,"open",textVAL,QMessageBox.Ok,QMessageBox.Ok)


app=QApplication([])
win=window()
app.exec_()