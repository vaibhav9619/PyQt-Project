import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QTextEdit,QFontDialog,QColorDialog
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
        self.push=QPushButton("click here to print  ",self)
        self.push.move(200,400)
        self.text = QTextEdit(self)
        self.text.setGeometry(60, 50, 400, 300)
        self.push.clicked.connect(self.print1)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
    def print1(self):
        printer=QPrinter(QPrinter.HighResolution)
        dia=QPrintDialog(printer,self)

        if dia.exec_() == QPrintDialog.Accepted:
            self.text.print_(printer)




app=QApplication([])
win=window()
app.exec_()