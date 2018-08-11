from PyQt5 import QtGui
from PIL import Image
import numpy as np
from PyQt5.QtCore import *
from urllib import request
from PyQt5.QtGui import QPixmap, QDesktopServices
from threading import Thread
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog,QTextEdit,QAction,QMessageBox,QLabel,QPushButton,QToolBar,QLineEdit
import cv2
from peewee import SqliteDatabase,Model,CharField,PrimaryKeyField
# db=SqliteDatabase("login.db")
class win(QMainWindow):
    def link(self, linkStr):
        QDesktopServices.openUrl(QUrl(linkStr))
    def __init__(self,parent=None):
        super().__init__(parent)
        self.tit="VS- The MASTER MIND"
        self.top=100
        self.bot=80
        self.wid=1000
        self.hei=650
        self.hello()

    def  hello(self):
        self.push1=QPushButton("-> Download <-",self)
        self.push1.setGeometry(515,300,110,30)
        self.push1.clicked.connect(self.down)
        self.push2 = QPushButton("-> Thug Life <-",self)
        self.push2.setGeometry(515,350,100,30)
        self.push2.clicked.connect(self.thug)
        self.push3 = QPushButton("-> Chat Bot <-",self)
        self.push3.setGeometry(515,400,110,30)
        self.push4 = QPushButton("-> Calculator <-",self)
        self.push4.setGeometry(515,450,110,30)
        self.push4.clicked.connect(self.calc)
        self.dia2=calcu(self)
        # self.push4.clicked.connect(self.but)



        self.push4 = QPushButton("-> SnapShot <-", self)
        self.push4.move(520, 500)
        self.push4.clicked.connect(self.capture)
        self.push5 = QPushButton("-> Camera <-", self)
        self.push5.move(520, 550)
        self.push5.clicked.connect(self.cam)

        self.push6 = QPushButton("-> Face and Eye detector <-", self)
        self.push6.setGeometry(470,600,200,30)
        self.push6.clicked.connect(self.detect)
        self.push7 = QPushButton("Login", self)
        self.push7.move(900, 60)
        self.push7.clicked.connect(self.but)
        self.dialog = second(self)

        self.push8 = QPushButton("Sign Up", self)
        self.push8.move(800, 60)
        self.push8.clicked.connect(self.jojo)
        self.d1=third(self)

        self.label4 = QLabel("ok",self)
        self.label4.setGeometry(10,15,100,100)
        self.label4.linkActivated.connect(self.li)
        self.label4.setText('<a href="http://google.com/">Google</a>')

        self.label5 = QLabel("ok", self)
        self.label5.setGeometry(75, 15, 100, 100)
        self.label5.linkActivated.connect(self.li2)
        self.label5.setText('<a href="http://facebook.com/">Facebook</a>')

        self.label6 = QLabel("ok", self)
        self.label6.setGeometry(150, 15, 100, 100)
        self.label6.linkActivated.connect(self.li3)
        self.label6.setText('<a href="http://gmail.com/">Gmail</a>')

        self.label51 = QLabel("ok", self)
        self.label51.setGeometry(200, 15, 100, 100)
        self.label51.linkActivated.connect(self.li4)
        self.label51.setText('<a href="https://www.wikipedia.org/">Wiki</a>')

        self.labeel=QLabel("Contact Us : +91 8800338836",self)
        self.labeel.setGeometry(15,620,200,20)

        self.label51 = QLabel("ok", self)
        self.label51.setGeometry(750, 580, 200, 100)
        self.label51.linkActivated.connect(self.li5)
        self.label51.setText('<a href="https://www.gmail.com/">sadana.vaibhav@gmail.com</a>')
        self.la=QLabel("EMail-",self)
        self.la.move(693,615)

        self.lk=QLabel(self)
        self.lk.setPixmap(QPixmap("vai.png"))
        self.lk.setGeometry(250,50,600,200)

        self.lk1 = QLabel(self)
        self.lk1.setPixmap(QPixmap("robo.png"))
        self.lk1.setGeometry(50, 200, 250, 400)

        self.lk2 = QLabel(self)
        self.lk2.setPixmap(QPixmap("robo.png"))
        self.lk2.setGeometry(680, 200, 600, 400)

        # toolbar
        self.nav=QToolBar("Navigation")
        self.nav.setIconSize(QSize(50,50))
        self.addToolBar(self.nav)
        self.url=QLineEdit(self)
        self.nav.addSeparator()
        self.nav.addWidget(self.url)

        





        label=QLabel("<h1>THE MASTER MIND</h1>",self)
        label.setGeometry(380,180,350,150)
        self.setWindowIcon(QtGui.QIcon('save.png'))
        menu=self.menuBar()
        # self.lab=QLabel(self)
        # self.lab.setPixmap(QPixmap('images.jpeg'))
        # self.lab.setGeometry(300,80,600,100)
        file=menu.addMenu("File")
        # file1=file.addMenu("Open files")
        edit = menu.addMenu("Edit")
        View = menu.addMenu("View")
        nav = menu.addMenu("Navigate")
        tools = menu.addMenu("Tools")
        helpo = menu.addMenu("Help")
        add=QAction('Open Files',self)
        add.triggered.connect(self.oko)
        file.addAction(add)
        close=QAction("Close Window",self)
        close.triggered.connect(self.sure)
        file.addAction(close)
        self.setWindowTitle(self.tit)
        self.setGeometry(self.top, self.bot, self.wid, self.hei)
        self.show()
    def oko(self):
        type=QFileDialog.getOpenFileName(self,"Open","/home")
        if type[0]:
            g=open(type[0],'r')
            with g:
                data=g.read()
                # self.text.setText(data)
    def sure(self):
        msg=QMessageBox.question(self,"close","DO u want to close",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if msg == QMessageBox.Yes:
            self.close()
    def cam(self):
        img = cv2.VideoCapture(0)
        four = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi', four, 20.0, (640, 480))
        while True:
            ret, cap = img.read()
            grey = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
            cv2.imshow("dfd", cap)
            cv2.imshow("asa", grey)
            if cv2.waitKey(1)==27:
                break
        out.release()
        img.release()
        # img=cv2.VideoCapture(0)
        # while True:
        #     ret,cap=img.read()
        #     cv2.imshow("camera",cap)
        #     cv2.waitKey(1)
        # img.release()
    def capture(self):
        # count=0
        img1=cv2.VideoCapture(0)
        ret,cap=img1.read()
        cv2.imshow("Capture",cap)
        # date=QDateTime.currentDateTime()
        cv2.imwrite("Images/" + "images.jpeg" , cap)
        cv2.waitKey(0)
    def but(self):
        self.dialog.show()
    def jojo(self):
        self.d1.show()
    def down(self):
        url=""
        s=int(input("ENter how many  files u want to downloaded ? "))
        for i in range(s):
            fname="media/"+str(i)+url.split("/")[-1]
            Thread(target=lambda:request.urlretrieve(url,"abc.mp4")).start()
    def calc(self):
        self.dia2.show()
    def detect(self):
        eyes=cv2.CascadeClassifier("haarcascade_eye.xml")
        face=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
        img=cv2.VideoCapture(0)
        while True:
            ret,cap=img.read()
            grey=cv2.cvtColor(cap,cv2.COLOR_RGB2GRAY)
            faces=face.detectMultiScale(grey,2,5)
            for (x,y,w,h) in faces:
                cv2.rectangle(cap,(x,y),(x+w,y+h),(0,0,255),4)
                greyFace=grey[y:y+h,x:x+w]
                eye=eyes.detectMultiScale(greyFace,2,5)
                for (x1,y1,w1,h1) in eye:
                    cv2.rectangle(cap,(x+x1,y+y1),(x+x1+w1,y+y1+h1),(0,0,255),4)
            cv2.imshow("Image",cap)
            cv2.waitKey(1)
    def li(self):
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com/"))
        self.setCentralWidget(self.browser)
        nav=QToolBar("Navigation")
        nav.setIconSize(QSize(20,20))
        self.addToolBar(nav)
    def li2(self):
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl("https://www.facebook.com/"))
        self.setCentralWidget(self.browser)
        nav=QToolBar("Navigation")
        nav.setIconSize(QSize(20,20))
        self.addToolBar(nav)
    def li3(self):
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl("https://www.gmail.com/"))
        self.setCentralWidget(self.browser)
        nav=QToolBar("Navigation")
        nav.setIconSize(QSize(20,20))
        self.addToolBar(nav)

    def li4(self):
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.wikipedia.org/"))
        self.setCentralWidget(self.browser)
        nav = QToolBar("Navigation")
        nav.setIconSize(QSize(20, 20))
        self.addToolBar(nav)
    def li5(self):
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.gmail.com/"))
        self.setCentralWidget(self.browser)
        nav = QToolBar("Navigation")
        nav.setIconSize(QSize(20, 20))
        self.addToolBar(nav)
    def thug(self):
        maskPath = "mask.png"
        mask = Image.open(maskPath)
        detect = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

        def Thug_mask(image):
            grey = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            faces = detect.detectMultiScale(grey, 2, 5)
            back = Image.fromarray(image)
            for (x, y, w, h) in faces:
                resixe = mask.resize((w, h), Image.ANTIALIAS)
                offset = (x, y)
                back.paste(resixe, offset, mask=resixe)
            return np.asarray(back)

        cap = cv2.VideoCapture(cv2.CAP_ANY)
        while True:
            ret, img = cap.read()
            if ret:
                cv2.imshow("Live", Thug_mask(img))
                if cv2.waitKey(1) == 27:
                    break
        cap.release()
        cv2.destroyAllWindows()


class second(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.tit = "Login Page"
        self.top = 100
        self.bot = 80
        self.wid = 1000
        self.hei = 650
        self.new1()
    def new1(self):
        self.labeel=QLabel(self)
        self.labeel.setPixmap(QPixmap("login1.png"))
        self.labeel.setGeometry(350,120,200,200)
        self.labeel1 = QLabel(self)
        self.line1=QLineEdit(self)
        self.line1.setGeometry(380,380,220,25)
        self.line2 = QLineEdit(self)
        self.line2.setEchoMode(QLineEdit.Password)
        self.line2.setGeometry(380, 430, 220, 25)
        self.pushh1=QPushButton("Login",self)
        self.pushh1.setGeometry(380,475,220,25)
        self.labal=QLabel("Username / Email",self)
        self.labal.setGeometry(380,270,200,200)
        self.labal1 = QLabel("Password", self)
        self.labal1.setGeometry(380, 320, 200, 200)
        self.loble=QLabel("ok",self)
        self.loble.setGeometry(380,490,150,50)
        # self.loble.linkActivated.connect(self.nop)
        self.loble.setText('<a href="http://gmail.com/">Create an account</a>')


        # self.loble.setText()
        # self.di=third(self)

        self.setWindowTitle(self.tit)
        self.setGeometry(self.top, self.bot, self.wid, self.hei)
    # def nop(self):
        # self.di.show()


        # self.show()
class third(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.tit = "Sign-up Page"
        self.top = 100
        self.bot = 80
        self.wid = 1000
        self.hei = 650
        self.new2()

    def new2(self):
        self.lo1=QLabel(self)
        self.lo1.setPixmap(QPixmap('login1.png'))
        self.lo1.setGeometry(350, 90, 200, 200)
        self.line12 = QLineEdit(self)
        self.line12.setGeometry(380, 320, 220, 25)
        self.line12 = QLineEdit(self)
        self.line12.setGeometry(380, 370, 220, 25)
        self.line13 = QLineEdit(self)
        self.line13.setGeometry(380, 420, 220, 25)
        self.line13.setEchoMode(QLineEdit.Password)
        self.line14 = QLineEdit(self)
        self.line14.setGeometry(380, 470, 220, 25)
        self.line14.setEchoMode(QLineEdit.Password)

        self.labal = QLabel("Username", self)
        self.labal.setGeometry(380, 210, 200, 200)
        self.labal1 = QLabel("Email", self)
        self.labal1.setGeometry(380, 260, 200, 200)
        self.labal = QLabel("Password", self)
        self.labal.setGeometry(380, 310, 200, 200)
        self.labal1 = QLabel("Confirm Password", self)
        self.labal1.setGeometry(380, 360, 200, 200)
        self.pushh1 = QPushButton("Sign-Up", self)
        self.pushh1.setGeometry(380, 520, 220, 25)
        self.lh=QLabel("hurr",self)
        self.lh.setGeometry(380,530,170,50)
        self.lh.linkActivated.connect(self.jija)
        self.lh.setText('<a href="http://gmail.com/">Already have acccount??</a>')
        self.dogla=second(self)


        self.setWindowTitle(self.tit)
        self.setGeometry(self.top, self.bot, self.wid, self.hei)
    def jija(self):
        self.dogla.show()


class calcu(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.tit="Calculator"
        self.top = 100
        self.bot = 80
        self.wid = 1000
        self.hei = 650
        self.cal1()
    def cal1(self):
        self.num7=QPushButton("7",self)
        self.num7.setGeometry(250,250,100,50)
        self.num8=QPushButton("8",self)
        self.num8.setGeometry(350,250,100,50)
        self.num9=QPushButton("9",self)
        self.num9.setGeometry(450,250,100,50)
        self.num4=QPushButton("4",self)
        self.num4.setGeometry(250,300,100,50)
        self.num5 = QPushButton("5", self)
        self.num5.setGeometry(350, 300, 100, 50)
        self.num6 = QPushButton("6", self)
        self.num6.setGeometry(450, 300, 100, 50)
        self.num1 = QPushButton("1", self)
        self.num1.setGeometry(250, 350, 100, 50)
        self.num2 = QPushButton("2", self)
        self.num2.setGeometry(350, 350, 100, 50)
        self.num3 = QPushButton("3", self)
        self.num3.setGeometry(450, 350, 100, 50)
        self.num0 = QPushButton("0", self)
        self.num0.setGeometry(250, 400, 100, 50)
        self.numm1 = QPushButton("Pow", self)
        self.numm1.setGeometry(350, 400, 100, 50)
        self.numm2 = QPushButton(".", self)
        self.numm2.setGeometry(450, 400, 100, 50)
        self.numm3 = QPushButton("/", self)
        self.numm3.setGeometry(550, 250, 100, 50)
        self.numm4 = QPushButton("x", self)
        self.numm4.setGeometry(550, 300, 100, 50)
        self.numm5 = QPushButton("-", self)
        self.numm5.setGeometry(550, 350, 100, 50)
        self.numm6 = QPushButton("+", self)
        self.numm6.setGeometry(550, 400, 100, 50)

        self.numm7 = QPushButton("Clear", self)
        self.numm7.setGeometry(250, 450, 200, 50)
        self.line=QLineEdit(self)
        self.line.setGeometry(250,190,100,35)
        self.line1 = QLineEdit(self)
        self.line1.setGeometry(360, 190, 100, 35)
        self.line2 = QLineEdit(self)
        self.line2.setGeometry(500, 190, 150, 35)
        self.label=QLabel("=",self)
        self.label.move(480,190)
        self.numm8 = QPushButton("Mod", self)
        self.numm8.setGeometry(450, 450, 200, 50)

        self.setWindowTitle(self.tit)
        self.setGeometry(self.top,self.bot,self.wid,self.hei)
        if self.numm6.isEnabled():
            self.numm6.clicked.connect(self.addition)
        if self.numm5.isEnabled():
            self.numm5.clicked.connect(self.sub)
        if self.numm4.isEnabled():
            self.numm4.clicked.connect(self.mul)
        if self.numm3.isEnabled():
            self.numm3.clicked.connect(self.div)
        if self.numm1.isEnabled():
            self.numm1.clicked.connect(self.pow)
        if self.numm8.isEnabled():
            self.numm8.clicked.connect(self.mod)
        # if self.line.isEnabled():
        #     if self.num0.isEnabled():
        #         self.line.text()==0
    def addition(self):
        num1=int(self.line.text())
        num2=int(self.line1.text())
        self.line2.setText(str(num1+num2))
    def sub(self):
        num1=int(self.line.text())
        num2=int(self.line1.text())
        self.line2.setText(str(num1-num2))
    def mul(self):
        num1=int(self.line.text())
        num2=int(self.line1.text())
        self.line2.setText(str(num1*num2))
    def div(self):
        num1=int(self.line.text())
        num2=int(self.line1.text())
        self.line2.setText(str(num1/num2))
    def pow(self):
        num1=int(self.line.text())
        num2=int(self.line1.text())
        self.line2.setText(str(num1**num2))
    def mod(self):
        num1=int(self.line.text())
        num2=int(self.line1.text())
        self.line2.setText(str(num1%num2))

# class Base(Model):
#     class Meta:
#         database=db
# class Log(Base):
app=QApplication([])
wind=win()

app.exec()
