import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple GitHub Drawing")
        self.cat = QPixmap("images\cat.webp")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.drawPixmap(QRect(200, 100, 320, 320), self.cat)

        p.setPen(QColor(128, 128, 128))  
        p.setBrush(QColor(128, 128, 128))  
        p.drawRect(50, 50, 100, 100)  

        p.end()

def main():
    app = QApplication(sys.argv)

    w2 = Simple_drawing_window2()
    w2.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
