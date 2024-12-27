import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple GitHub Drawing")
        self.snoopy = QPixmap("lab5_1/images/snoopy.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
    
        p.drawPixmap(QRect(200, 100, 320, 320), self.snoopy)
        p.setPen(QColor(0, 0, 255))
        p.setBrush(QColor(0, 0, 255))
        p.drawEllipse(500, 300, 100, 100)
        p.end()

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window1()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())