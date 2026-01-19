import os
os.system("cls")

from PyQt5.QtWidgets import (QApplication, QWidget,
                             QLabel, QPushButton)
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
label2.setGeometry(160, 150, 100,50)

def func1():
    son = int(label2.text())
    son += 1
    label2.setText(str(son))
    # print("Tugmacha bosildi...")
    

btn1 = QPushButton(oyna)
btn1.setText("Count")
btn1.setStyleSheet("background-color: #c9eb0c; color:black; font-size:25px; width:150px;height:50px;border-radius:25px;")
btn1.move(180,250)
btn1.clicked.connect(func1)

def reset():
    label2.setText("0")

btn2 = QPushButton(oyna)
btn2.setText("Reset")
btn2.setStyleSheet("background-color: red; color:black; font-size:25px; width:110px;height:50px;border-radius:25px;")
btn2.move(40,250)
btn2.clicked.connect(reset)


oyna.show()
app.exec_()