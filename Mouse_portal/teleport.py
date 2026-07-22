import subprocess
from mouse import get_mouse_position
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

class Teleporter:
    def __init__(self, orange, blue):
        self.orange = orange
        self.blue = blue
        self.cooldown = False

    def move_mouse(self, x, y):
        subprocess.run(["hyprctl", "dispatch", f"hl.dsp.cursor.move({{ x = {x}, y = {y} }})"])
        
    def inside(self, mouse_x, mouse_y, portal):
        x, y = portal.center()
        return (abs(mouse_x - x) < portal.width() // 2 and abs(mouse_y - y) < portal.height() // 2)

    def check(self):
        if QApplication.keyboardModifiers() & Qt.MetaModifier:
            return

        mouse_x, mouse_y = get_mouse_position()
        
        if self.cooldown:
            if (not self.inside(mouse_x, mouse_y, self.orange) and not self.inside(mouse_x, mouse_y, self.blue)): self.cooldown = False
            return

        if self.inside(mouse_x, mouse_y, self.orange):
            x, y = self.blue.center()
            self.move_mouse(x + self.blue.width(), y)
            self.cooldown = True

        elif self.inside(mouse_x, mouse_y, self.blue):
            x, y = self.orange.center()
            self.move_mouse(x - self.orange.width(), y)
            self.cooldown = True
            