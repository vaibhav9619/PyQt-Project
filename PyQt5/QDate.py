
from PyQt5.QtCore import QDateTime,Qt
date=QDateTime.currentDateTime()
print(date.toString())
print(date.toString(Qt.ISODate))
print(date.toString(Qt.DefaultLocaleLongDate))