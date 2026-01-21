import os
os.system("cls")
import random as rd

from PyQt5.QtWidgets import (QApplication, 
                             QWidget,
                             QLabel, 
                             QPushButton,
                             QLineEdit,
                             QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import QFont

app = QApplication([])

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # self.setFixedSize(360, 700)
        # self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        self.label1 = QLabel()
        self.label1.setText("Bugun havo yaxshi")
        self.label1.setStyleSheet("font-size:20px;color:red;")
        self.btn1 = QPushButton(self)
        self.btn1.setText("Press me")
        self.btn1.setStyleSheet("font-size:25px; border:2px solid black;")
        self.btn1.clicked.connect(self.press_btn)

        self.btn2 = QPushButton()
        self.btn2.setText("Press me")
        self.btn2.setStyleSheet("font-size:25px; border:2px solid black;")
        self.btn2.clicked.connect(self.press_btn)

        self.btn3 = QPushButton()
        self.btn3.setText("Press me")
        self.btn3.setStyleSheet("font-size:25px; border:2px solid black;")
        self.btn3.clicked.connect(self.press_btn)

        self.btn4 = QPushButton()
        self.btn4.setText("Press me")
        self.btn4.setStyleSheet("font-size:25px; border:2px solid black;")
        self.btn4.clicked.connect(self.press_btn)

        # self.v_layout.addWidget(self.label1)
        # self.v_layout.addWidget(self.btn1)
        # self.v_layout.addWidget(self.btn2)
        # self.v_layout.addWidget(self.btn3)
        # self.v_layout.addWidget(self.btn4)
        # self.setLayout(self.v_layout)
        self.h_layout.addWidget(self.label1)
        self.h_layout.addWidget(self.btn1)
        self.h_layout.addWidget(self.btn2)
        self.h_layout.addWidget(self.btn3)
        self.h_layout.addWidget(self.btn4)
        self.setLayout(self.h_layout)

    def press_btn(self):
        colors = ["red", "yellow", "black", "blue", "green"]
        rand_color = rd.choice(colors)
        self.label1.setStyleSheet(f"color:{rand_color};font-size:20px;")


win1 = Window()
win1.show()
app.exec_()