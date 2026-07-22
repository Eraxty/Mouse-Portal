import json
import subprocess

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPixmap

class Portal(QWidget):
    def __init__(self, image, name):
        super().__init__()
        self.name = name
        self.setWindowTitle(name)
        self.image = QPixmap(image)
        self.setFixedSize(50, 100)
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.WindowTransparentForInput
        )

        self.setAttribute(Qt.WA_TranslucentBackground)

    def place(self, x, y):
        self.move(x - self.width() // 2, y - self.height() // 2)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.width(), self.height(), self.image)

    def center(self):
        result = subprocess.check_output(["hyprctl", "clients", "-j"], text=True)
        clients = json.loads(result)
        for client in clients:
            if client.get("title") == self.name:
                x, y = client["at"]
                width, height = client["size"]
                return (x + width // 2, y + height // 2)

        return (self.x() + self.width() // 2, self.y() + self.height() // 2)