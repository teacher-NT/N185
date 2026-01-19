import os
os.system("cls")

from PyQt5.QtWidgets import (QApplication, QWidget,QLabel)
from PyQt5.QtGui import QFont

font1 = QFont("Lobster", 20)


app = QApplication([])

oyna = QWidget()
oyna.setWindowTitle("Couter dasturi")
oyna.setGeometry(1400, 100, 360, 720)
oyna.setStyleSheet("background-color: #4bba47;")

label = QLabel(oyna)
label.setText("Qani boshladik")
label.setFont(font1)
label.setStyleSheet("color:white;")
label.move(90, 100)

label2 = QLabel(oyna)
label2.setText("0")
label2.setStyleSheet("font-size:60px;")
label2.move(160, 150)

oyna.show()
app.exec_()