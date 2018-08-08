from PyQt5.QtWidgets import QApplication,QMessageBox,QMainWindow,QAction
class win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tit="Menu bar"
        self.top=100
        self.bot=100
        self.wid = 680
        self.hei = 560
        self.men()
    def men(self):
        menu=self.menuBar()
        filename=menu.addMenu("File")
        save=filename.addMenu("Save")
        saveas=filename.addMenu("Save As")
        # exi=filename.addMenu("Exit")
        view=menu.addMenu("View")
        edit=menu.addMenu("Edit")
        search=menu.addMenu("Search")
 
        exi=QAction('Exit',self)
        exi.setShortcut("Ctrl+F")
        exi.triggered.connect(self.close)
        filename.addAction(exi)

        self.setWindowTitle(self.tit)
        self.setGeometry(self.top,self.bot,self.wid,self.hei)
        self.show()
app=QApplication([])
qw=win()
app.exec_()
