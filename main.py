from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from random import randint
app = QApplication([])
okoshko = QWidget()
okoshko.setWindowTitle("Рандомізатор")
okoshko.move(200, 100)
okoshko.resize(400, 400)

OKUN = QPushButton(okoshko)
OKUN.setText("Згенерувати")
OKUN.move(140, 130)

text = QLabel(okoshko)
text.setText("Натисніть, щоб згенерувати число")
text.move(100, 10)

rand = QLabel(okoshko)
rand.move(190, 70)

def Sigma():
    number = randint(1, 100)
    rand.setText(str(number))
    text.setText("Число:")

OKUN.clicked.connect(Sigma)

okoshko.show()
app.exec_()