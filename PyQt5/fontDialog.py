import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QTextEdit,QFontDialog,QColorDialog
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
        self.push=QPushButton("chnge font",self)
        self.push.move(200,400)
        self.push1 = QPushButton("chnge color", self)
        self.push1.move(300, 400)
        self.push1.clicked.connect(self.col)
        self.push.clicked.connect(self.ch)
        self.text=QTextEdit(self)
        self.text.setGeometry(60,50,400,300)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
    def ch(self):
        font,ok=QFontDialog.getFont()
        if ok:
            self.text.setFont(font)
    def col(self):
        color=QColorDialog.getColor()
        self.text.setTextColor(color)
app=QApplication([])
win=window()
app.exec_()