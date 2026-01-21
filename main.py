import os
os.system("cls")
import random as rd

from PyQt5.QtWidgets import (QApplication, 
                             QWidget,
                             QLabel, 
                             QPushButton,
                             QLineEdit)
from PyQt5.QtGui import QFont

app = QApplication([])

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(360, 700)
        self.label1 = QLabel(self)
        self.label1.setText("Bugun havo yaxshi")
        self.label1.setStyleSheet("font-size:20px;color:red;")
        self.label1.move(20,15)
        self.btn1 = QPushButton(self)
        self.btn1.setText("Press me")
        self.btn1.setStyleSheet("font-size:25px; border:2px solid black;")
        self.btn1.move(20, 55)
        self.btn1.clicked.connect(self.press_btn)

    def press_btn(self):
        colors = ["red", "yellow", "black", "blue", "green"]
        rand_color = rd.choice(colors)
        self.label1.setStyleSheet(f"color:{rand_color};font-size:20px;")


win1 = Window()
win1.show()
app.exec_()