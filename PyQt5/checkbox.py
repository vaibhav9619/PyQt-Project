import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QCheckBox,QLabel
from PyQt5.QtCore import Qt
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
        ch=QCheckBox("Football",self)
        ch.move(100,100)
        ch.toggle()
        self.label = QLabel("",self)
        self.label.move(100,150)
        ch.stateChanged.connect(self.cli)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)

        self.show()
    def cli(self,state):
        if state == Qt.Checked:
            self.label.setText("Yes  i liked it")
        else:
            self.label.setText("No")

app=QApplication([])
win=window()
app.exec_()