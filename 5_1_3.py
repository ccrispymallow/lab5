import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple GitHub Drawing")
        self.cat = QPixmap("images/catAI.jpg")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.drawPixmap(QRect(200,100,320,320), self.cat)
        p.end()

class Simple_drawing_window3(Simple_drawing_window):

    def paintEvent(self, e):
        super().paintEvent(e)
        p = QPainter(self)
        p.setPen(QColor(0,255,0))
        p.setBrush(QColor(0,255,0))

        p.drawPolygon([QPoint(300,20),QPoint(400,90),QPoint(200,90),])
        p.end()

def main():
    app = QApplication(sys.argv)
    w3 = Simple_drawing_window3()
    w3.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())