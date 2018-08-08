from PyQt5.QtWidgets import QApplication,QMessageBox,QPushButton,QMainWindow
class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title="My new Window"
        self.top=100
        self.bot=100
        self.wid=680
        self.hei=540

        but=QPushButton("MsgBox",self)
        but1=QPushButton("Subscribe",self)
        but1.move(200,400)
        but1.clicked.connect(self.ques)
        but.move(300,400)
        but.clicked.connect(self.msgbox)
        but2=QPushButton("Cancel",self)
        but2.move(400,400)
        but2.clicked.connect(self.clo)
        self.meg()
    def meg(self):
        self.statusBar().showMessage("This is simple status bar bar")
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.bot,self.wid,self.hei)
        self.show()
    def msgbox(self):
        QMessageBox.about(self,"About Box","This is about msg box")
    def ques(self):
        msg=QMessageBox.question(self,"Question","Have u subscribed my channel or not",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if msg==QMessageBox.Yes:
            QMessageBox.about(self,"Subscribe","Subscribed already")
            # print("Subscribed already")
        else:
            QMessageBox.about(self, "Subscribe", " Not Subscribed")
    def clo(self):
        msg=QMessageBox.question(self,"Cancel","Sure want to close",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if msg == QMessageBox.Yes:
            self.close()
            # print("Not subscribed")
app=QApplication([])
wi=window()
app.exec_()