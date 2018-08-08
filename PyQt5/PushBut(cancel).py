from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton
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
        button1.clicked.connect(self.close)
        self.set()
    def set(self):
        self.setWindowTitle(self.tit)
        self.setGeometry(self.top,self.bo,self.wid,self.he)
        self.show()
    def close(self):
        QCoreApplication.instance().quit()
app=QApplication([])
w1=win()
app.exec_()

