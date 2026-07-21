import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

from portal import Portal
from mouse import get_mouse_position


class PortalApp(Portal):
    def keyPressEvent(self, event):
        x, y = get_mouse_position()

        if event.key() == Qt.Key_Z:
            orange.place(x, y)

        elif event.key() == Qt.Key_X:
            blue.place(x, y)


app = QApplication(sys.argv)

orange = PortalApp("assets/portal_orange.png")
blue = PortalApp("assets/portal_blue.png")

orange.place(500, 500)
blue.place(900, 500)

sys.exit(app.exec())