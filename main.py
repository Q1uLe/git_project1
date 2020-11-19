import sys

from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.btn_clicked = False
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.btn_click)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.btn_clicked:
            self.draw_circle(qp)
        qp.end()

    def btn_click(self):
        self.btn_clicked = True
        self.update()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        r = randint(0, 300)
        x = int(randint(r, 1014 - r) - r / 2)
        y = int(randint(r, 618 - r) - r / 2)
        qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
