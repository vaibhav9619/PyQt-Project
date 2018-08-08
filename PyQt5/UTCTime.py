from PyQt5.QtCore import QDateTime,Qt
dT=QDateTime.currentDateTime()
print("Local   " + dT.toString(Qt.DefaultLocaleLongDate))
print("universal  " +dT.toUTC().toString())