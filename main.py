import os
os.system("cls")

from PyQt5.QtWidgets import (QApplication, 
                             QWidget,
                             QLabel, 
                             QPushButton,
                             QLineEdit)
from PyQt5.QtGui import QFont

app = QApplication([])

oyna = QWidget()
oyna.setWindowTitle("Couter dasturi")
oyna.setGeometry(1400, 100, 360, 720)
oyna.setStyleSheet("background-color: #4bba47;")

in1 = QLineEdit(oyna)
in1.setGeometry(10,20, 250,50)
in1.setStyleSheet("background-color:white; color:black;font-size:20px;border:2px solid black;")
in1.setPlaceholderText("nimadir kiriting...")

btn1 = QPushButton(oyna)
btn1.setGeometry(270,20, 50,50)
btn1.setStyleSheet("background-color:white;color:black; font-size:25px; border: 2px solid black;")
btn1.setText("🔍")

oyna.show()
app.exec_()