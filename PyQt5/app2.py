import os
# import peewee
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtGui import QFont, QDesktopServices
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QToolBar



class MainWindow(QMainWindow):
    def link(self, linkStr):
        QDesktopServices.openUrl(QUrl(linkStr))
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        dia = QtWidgets.QDialog()
        layout = QtWidgets.QVBoxLayout()
        # self.browser = QWebEngineView()
        # self.setStyleSheet("background-color : white;")
        # self.showFullScreen()
        # layout1=QtWidgets.QHBoxLayout()

        self.setWindowTitle("My Awesome App")
        self.setWindowIcon(QtGui.QIcon(os.path.join('ges12.jpg')))

        self.label4=QLabel("ok")
        self.label4.setAlignment(Qt.AlignTop)
        self.label4.linkActivated.connect(self.link)
        self.label4.setText('<a href="http://google.com/">Google</a>')

        self.label = QLabel("Welcome To My New Desktop Application")
        self.label.setAlignment(Qt.AlignCenter)
        self.label2=QLabel("LOGIN / REGISTER")
        self.label2.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial",20))
        self.label2.setFont(QFont("Arial",20))
        self.line=QLineEdit()
        self.line1 = QLineEdit()

        # self.setCentralWidget(self.browser)
        navtb = QToolBar("Navigation")
        navtb.setIconSize(QSize(20, 20))
        self.addToolBar(navtb)


        self.urlbar = QLineEdit()
        navtb.addSeparator()
        navtb.addWidget(self.urlbar)



        # self.label.setAlignment(Qt.AlignCenter)

        self.button = QPushButton("Login")
        self.button.setStatusTip("Next Page")
        # self.button.clicked.connect(self.do)#
        self.b1 = QPushButton("Cancel")
        layout.addWidget(self.label4)





        layout.addWidget(self.label)
        layout.addWidget(self.label2)
        layout.addWidget(self.line)
        layout.addWidget(self.line1)
        layout.addWidget(self.button)
        layout.addWidget(self.b1)

        # self.setCentralWidget(label)
        dia.setLayout(layout)

        self.setCentralWidget(dia)

app = QtWidgets.QApplication([])
window = MainWindow()
window.setGeometry(300,100,800,600)
window.show()
app.exec_()

