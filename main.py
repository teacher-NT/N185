import os
os.system("cls")
import random as rd

from PyQt5.QtWidgets import (QApplication, 
                             QWidget,
                             QLabel, 
                             QPushButton,
                             QLineEdit,
                             QHBoxLayout, QVBoxLayout,
                             QComboBox,
                             QCheckBox,
                             QMessageBox)
from PyQt5.QtGui import QFont

app = QApplication([])

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # self.setFixedSize(360, 700)
        self.v_layout = QVBoxLayout()
        # self.h_layout = QHBoxLayout()
        self.label1 = QLabel()
        self.label1.setText("Bugun havo yaxshi")
        self.label1.setStyleSheet("font-size:20px;color:red;")
        self.btn1 = QPushButton("Qizil")
        self.btn1.setStyleSheet("font-size:25px; border:2px solid black;")
        self.btn1.clicked.connect(self.qizil_tugma)

        self.btn2 = QPushButton("Yashil")
        self.btn2.setStyleSheet("font-size:25px; border:2px solid black;")
        self.btn2.clicked.connect(self.yashil_tugma)

        self.btn3 = QPushButton("Sariq")
        self.btn3.setStyleSheet("font-size:25px; border:2px solid black;")
        self.btn3.clicked.connect(self.sariq_tugma)

        self.btn4 = QPushButton("Ko'k")
        self.btn4.setStyleSheet("font-size:25px; border:2px solid black;")
        self.btn4.clicked.connect(self.press_btn)


        self.menyu = QComboBox()
        self.menyu.addItems(["Gamburger", "Lavash", "Chizburger", "HotDog", "Pizza"])
        self.menyu.setStyleSheet("QComboBox {font-size:20px;background-color:#80dbf2;}QComboBox::hover {background-color:#43c7e8}")
        self.menyu.currentTextChanged.connect(self.on_change)
        self.v_layout.addWidget(self.menyu)

        self.check1 = QCheckBox("Choy")
        self.check1.stateChanged.connect(self.on_update)
        self.check2 = QCheckBox("Kofe")
        self.check2.stateChanged.connect(self.on_update)
        self.check3 = QCheckBox("Kola")
        self.check3.stateChanged.connect(self.on_update)
        self.check4 = QCheckBox("Suv")
        self.check4.stateChanged.connect(self.on_update)
        self.check5 = QCheckBox("Sharbat")
        self.check5.stateChanged.connect(self.on_update)
        self.v_layout.addWidget(self.check1)
        self.v_layout.addWidget(self.check2)
        self.v_layout.addWidget(self.check3)
        self.v_layout.addWidget(self.check4)
        self.v_layout.addWidget(self.check5)

        self.v_layout.addWidget(self.label1)
        self.v_layout.addWidget(self.btn1)
        self.v_layout.addWidget(self.btn2)
        self.v_layout.addWidget(self.btn3)
        self.v_layout.addWidget(self.btn4)
        self.setLayout(self.v_layout)
        # self.h_layout.addWidget(self.label1)
        # self.h_layout.addWidget(self.btn1)
        # self.h_layout.addWidget(self.btn2)
        # self.h_layout.addWidget(self.btn3)
        # self.h_layout.addWidget(self.btn4)
        # self.setLayout(self.h_layout)

    def press_btn(self):
        colors = ["red", "yellow", "black", "blue", "green"]
        rand_color = rd.choice(colors)
        self.label1.setStyleSheet(f"color:{rand_color};font-size:20px;")

    def on_change(self):
        print(self.menyu.currentText())

    def on_update(self):
        lst = []
        if self.check1.isChecked():
            lst.append(self.check1.text())
        if self.check2.isChecked():
            lst.append(self.check2.text())
        if self.check3.isChecked():
            lst.append(self.check3.text())
        if self.check4.isChecked():
            lst.append(self.check4.text())
        if self.check5.isChecked():
            lst.append(self.check5.text())
        print(lst)
        
    def sariq_tugma(self):
        QMessageBox.information(self, "Ma'lumot", "Bu shuncha xabar!")

    def qizil_tugma(self):
        QMessageBox.warning(self, "Ogohlantirish", "Sizni ogohlantiramiz!")

    def yashil_tugma(self):
        QMessageBox.question(self, "Savol", "Tovuq birinchi yoki tuhum?")
win1 = Window()
win1.show()
app.exec_()