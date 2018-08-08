import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QTextEdit,QFontDialog,QColorDialog,QFileDialog
from PyQt5.QtPrintSupport import QPrintDialog,QPrinter
from PyQt5.QtCore import QFileInfo
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
        self.push.clicked.connect(self.pdf)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
    def pdf(self):
        fn,_=QFileDialog.getSaveFileName(self,'Export PDF',None,'PDF files(.pdf);; All files')
        if fn !='':
            if QFileInfo(fn).suffix()== "" : fn +='.pdf'
            printer=QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.text.document().print_(printer)








app=QApplication([])
win=window()
app.exec_()