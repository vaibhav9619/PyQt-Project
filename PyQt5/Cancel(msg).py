from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QMessageBox
from PyQt5 import QtGui
from PyQt5.QtCore import QCoreApplication
class win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tit="New WINDOW"
        self.top=100
        self.bo=100
        self.wid=680
        self.he=540
        button=QPushButton("LOGIN",self)
        button1 = QPushButton("Cancel", self)
        button.move(290,400)
        button1.move(290,440)
        button1.setToolTip("Cancel")
        button.setToolTip("Login")
        button1.clicked.connect(self.mes)

        self.set()
    def set(self):
        self.setWindowTitle(self.tit)
        self.setGeometry(self.top,self.bo,self.wid,self.he)
        self.show()
    def mes(self):
        reply=QMessageBox.question(self,"Close","Do u Really want to quit",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if reply==QMessageBox.Yes:
            self.close()

app=QApplication([])
w1=win()
app.exec_()

