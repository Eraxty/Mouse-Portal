from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPen, QColor

class PortalOverlay(QWidget):
    def __init__(self):
        super().__init__()

        self.orange = None
        self.blue = None

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.WindowTransparentForInput
        )

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(QApplication.primaryScreen().geometry())

    def set_orange(self, x, y):
        self.orange = (x, y)
        self.update()

    def set_blue(self, x, y):
        self.blue = (x, y)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        if self.orange:
            painter.setPen(QPen(QColor("orange"), 5))
            x, y = self.orange
            painter.drawEllipse(x - 20, y - 40, 40, 80)

        if self.blue:
            painter.setPen(QPen(QColor("blue"), 5))
            x, y = self.blue
            painter.drawEllipse(x - 20, y - 40, 40, 80)