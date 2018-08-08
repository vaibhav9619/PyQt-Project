import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QSpinBox,QLabel
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
        self.label=QLabel("Value",self)
        self.label.move(200,200)
        self.spin=QSpinBox(self)
        self.spin.move(200,100)
        self.spin.setMaximum(20)
        self.spin.setMinimum(10)
        self.spin.valueChanged.connect(self.val)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)

        self.show()
    def val(self):
        self.label.setText("chnage"+str(self.spin.value()))
app=QApplication([])
win=window()
app.exec_()