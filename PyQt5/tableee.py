from PyQt5.QtWidgets import QApplication,QMainWindow,QTableWidgetItem,QTableWidget,QVBoxLayout,QLabel
class win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tit="tables"
        self.top=100
        self.bot=100
        self.wid=600
        self.hei=600
        self.init()
    def init(self):

        self.creating()
        self.vb=QVBoxLayout()
        self.vb.addWidget(self.tables)
        self.setLayout(self.vb)
        self.setWindowTitle(self.tit)
        self.setGeometry(self.top, self.bot, self.wid, self.hei)
        self.show()
    def creating(self):
        self.tables=QTableWidget(self)
        self.tables.setGeometry(20,20,450,200)
        self.tables.setRowCount(5)
        self.tables.setColumnCount(3)
        self.tables.setItem(0,0, QTableWidgetItem("Name"))
        self.tables.setItem(0, 1, QTableWidgetItem("Gender"))
        self.tables.setItem(0, 2, QTableWidgetItem("Email"))
        self.tables.setItem(1, 0, QTableWidgetItem("Vaibhav"))
        self.tables.setItem(1,1 , QTableWidgetItem("Male"))
        self.tables.setItem(1, 2, QTableWidgetItem("sadana.vaibhav@gmail.com"))

        self.tables.setItem(2, 0, QTableWidgetItem("Rishabh"))
        self.tables.setItem(2, 1, QTableWidgetItem("Female"))
        self.tables.setItem(2, 2, QTableWidgetItem("rishabhKumr@gmail.com"))

        self.tables.setColumnWidth(2,200)

app=QApplication([])
window=win()
app.exec_()