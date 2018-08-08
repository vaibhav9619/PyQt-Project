import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QMessageBox
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
        copy=QAction(QIcon("copy.png"),"Copy",self)
        copy.setShortcut("Ctrl+C")
        paste=QAction(QIcon("paste.png"),"Paste",self)
        paste.setShortcut("Ctrl+V")
        delete=QAction(QIcon("delete.png"),"Delete",self)
        delete.setShortcut("Ctrl+D")
        save=QAction(QIcon("save.png"),'Save',self)
        save.setShortcut("Ctrl+S")
        ex=QAction(QIcon("exit.jpg"),"Exit",self)
        ex.setShortcut("Ctrl+E")
        ex.triggered.connect(self.cl)
        self.toolbar=self.addToolBar('Toolbar')

        self.toolbar.addAction(ex)
        self.toolbar.addAction(copy)
        self.toolbar.addAction(paste)
        self.toolbar.addAction(delete)
        self.toolbar.addAction(save)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)

        self.show()
    def cl(self):
        mes=QMessageBox.question(self,"Exit","Want to exit ?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if mes == QMessageBox.Yes:
            self.close()
app=QApplication([])
win=window()
app.exec_()