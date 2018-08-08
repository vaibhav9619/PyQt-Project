import os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QLabel, QToolBar, QAction, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)

        self.setWindowTitle("My Awesome App")
        self.setWindowIcon(QtGui.QIcon(os.path.join('ges12.jpg')))




        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com/"))



        # self.setCentralWidget(label)
        self.setCentralWidget(self.browser)
        navtb=QToolBar("Navigation")
        navtb.setIconSize(QSize(20,20))
        self.addToolBar(navtb)

        # back_btn=QAction(QIcon(os.path.join('i1.jpg')),"Back",self)
        # back_btn.setStatusTip("Back to previous page")
        # back_btn.triggered.connect(self.browser.back)
        # navtb.addAction(back_btn)
        #
        # next_btn = QAction(QIcon(os.path.join('images.jpg')), "Next", self)
        # next_btn.setStatusTip("Forward to next Page")
        # next_btn.triggered.connect(self.browser.forward)
        # navtb.addAction(next_btn)
        #
        # reload_btn = QAction(QIcon(os.path.join('kl.jpg')), "Reload", self)
        # reload_btn.setStatusTip("Stop Loading current page")
        # reload_btn.triggered.connect(self.browser.reload)
        # navtb.addAction(reload_btn)

        # self.urlbar=QLineEdit()
        # navtb.addSeparator()
        #
        # navtb.addWidget(self.urlbar)

        # stop_btn = QAction(QIcon(os.path.join('hi.png')), "Stop", self)
        # stop_btn.setStatusTip("Stop Loading current page")
        # stop_btn.triggered.connect(self.browser.reload)
        # navtb.addAction(stop_btn)





        self.show()
app=QtWidgets.QApplication([])
app.setApplicationName("My new desktop app")
app.setOrganizationName("Desktop")
app.setOrganizationDomain("App.org")
window=MainWindow()
window.show()
app.exec_()