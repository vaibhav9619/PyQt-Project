import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QTextEdit,QFontDialog,QColorDialog,QFileDialog
from PyQt5.QtPrintSupport import QPrintDialog,QPrinter
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
        self.push=QPushButton("open file  ",self)
        self.push.move(200,400)
        self.text = QTextEdit(self)
        self.text.setGeometry(60, 50, 400, 300)
        self.push.clicked.connect(self.oko)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
    def oko(self):
        type=QFileDialog.getOpenFileName(self,"open file","/home")
        if type[0]:
            g=open(type[0],'r')
            with g:
                data=g.read()
                self.text.setText(data)




app=QApplication([])
win=window()
app.exec_()