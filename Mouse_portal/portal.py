from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter

class PortalOverlay(QWidget):
    def __init__(self):
        super().__init__()
        self.orange = None
        self.blue = None
        self.orange_img = QPixmap("assets/portal_orange.png")
        self.blue_img = QPixmap("assets/portal_blue.png")

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
        painter.setRenderHint(QPainter.Antialiasing)

        if self.orange:
            x, y = self.orange
            painter.drawPixmap(x - 20, y - 40, 40, 80, self.orange_img)

        if self.blue:
            x, y = self.blue
            painter.drawPixmap(x - 20, y - 40, 40, 80, self.blue_img)