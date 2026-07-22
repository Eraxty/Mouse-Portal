import subprocess
from mouse import get_mouse_position
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

class Teleporter:
    def __init__(self, orange, blue):
        self.orange = orange
        self.blue = blue
        self.cooldown = False
        self.last_mouse = get_mouse_position()

    def move_mouse(self, x, y):
        subprocess.run(["hyprctl", "dispatch", f"hl.dsp.cursor.move({{ x = {x}, y = {y} }})"])
        
    def inside(self, mouse_x, mouse_y, portal):
        x, y = portal.center()
        return (abs(mouse_x - x) < portal.width() // 2 and abs(mouse_y - y) < portal.height() // 2)

    def check(self):
        if QApplication.keyboardModifiers() & Qt.MetaModifier:
            return

        mouse_x, mouse_y = get_mouse_position()
        last_x, last_y = self.last_mouse

        if self.cooldown:
            if (not self.inside(mouse_x, mouse_y, self.orange) and not self.inside(mouse_x, mouse_y, self.blue)):
                self.cooldown = False
            self.last_mouse = (mouse_x, mouse_y)
            return

        if self.inside(mouse_x, mouse_y, self.orange):
            x, y = self.blue.center()
            if mouse_x > last_x:
                self.move_mouse(x + self.blue.width(), y)
            else:
                self.move_mouse(x - self.blue.width(), y)
            self.cooldown = True

        elif self.inside(mouse_x, mouse_y, self.blue):
            x, y = self.orange.center()
            if mouse_x > last_x:
                self.move_mouse(x + self.orange.width(), y)
            else:
                self.move_mouse(x - self.orange.width(), y)
            self.cooldown = True

        self.last_mouse = (mouse_x, mouse_y)