import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from portal import PortalOverlay
from mouse import get_mouse_position

class App(PortalOverlay):
    def keyPressEvent(self, event):
        x, y = get_mouse_position()

        if event.key() == Qt.Key_Z:
            self.set_orange(x, y)
            print("Orange:", x, y)

        elif event.key() == Qt.Key_X:
            self.set_blue(x, y)
            print("Blue:", x, y)

app = QApplication(sys.argv)
overlay = App()
overlay.show()
sys.exit(app.exec())