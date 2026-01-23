import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,QVBoxLayout
)
from PyQt5.QtCore import Qt

style1 = """
    font-size:32px;
    color:black;
"""

style2 = """
    font-size: 20px;
    border: 2px solid black;
    border-radius: 10px;
    background-color: #cf3acc;
    padding: 5px;
"""

style3 = """
    font-size:40px;
    color: blue;
"""

style4 = """
    font-size: 20px;
    border: 2px solid black;
    border-radius: 10px;
    background-color: #3acf64;
    padding: 5px;
"""


app = QApplication([])

class TranslatorWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setFixedSize(400,700)
        self.vbox = QVBoxLayout()
        self.label1 = QLabel("Tarjimon")
        self.label1.setStyleSheet(style3)
        self.btn1 = QPushButton("Tarjima qilish")
        # self.btn1.clicked.connect(self.open_translator)
        self.btn1.setStyleSheet(style4)

        self.btn2 = QPushButton("Bosh Oynaga qaytish")
        self.btn2.clicked.connect(self.back_main_window)
        self.btn2.setStyleSheet(style4)

        self.vbox.addWidget(self.label1,  alignment=Qt.AlignCenter | Qt.AlignTop)
        self.vbox.addWidget(self.btn1)
        self.vbox.addWidget(self.btn2)
        self.setLayout(self.vbox)

    def back_main_window(self):
        self.main_window.show()
        self.hide()

class WeatherWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setFixedSize(400,700)
        self.vbox = QVBoxLayout()
        self.label1 = QLabel("Ob havo ma'lumotlari")
        self.label1.setStyleSheet(style3)
        self.btn1 = QPushButton("Qidirish")
        # self.btn1.clicked.connect(self.open_translator)
        self.btn1.setStyleSheet(style4)

        self.btn2 = QPushButton("Bosh Oynaga qaytish")
        self.btn2.clicked.connect(self.back_main_window)
        self.btn2.setStyleSheet(style4)

        self.vbox.addWidget(self.label1,  alignment=Qt.AlignCenter | Qt.AlignTop)
        self.vbox.addWidget(self.btn1)
        self.vbox.addWidget(self.btn2)
        self.setLayout(self.vbox)

    def back_main_window(self):
        self.main_window.show()
        self.hide()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400,700)
        self.vbox = QVBoxLayout()
        self.label1 = QLabel("Telefon")
        self.label1.setStyleSheet(style1)
        self.btn1 = QPushButton("Tarjimon")
        self.btn1.clicked.connect(self.open_translator)
        self.btn1.setStyleSheet(style2)

        self.btn2 = QPushButton("Ob havo")
        self.btn2.clicked.connect(self.open_weather)
        self.btn2.setStyleSheet(style2)

        self.vbox.addWidget(self.label1,  alignment=Qt.AlignCenter | Qt.AlignTop)
        self.vbox.addWidget(self.btn1)
        self.vbox.addWidget(self.btn2)

        self.setLayout(self.vbox)

        self.show()

    def open_translator(self):
        self.window = TranslatorWindow(self)
        self.window.show()
        self.hide()

    def open_weather(self):
        self.window = WeatherWindow(self)
        self.window.show()
        self.hide()

Win1 = MainWindow()
app.exec_()