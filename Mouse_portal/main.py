import sys
from PySide6.QtWidgets import QApplication
from portal import PortalOverlay

app = QApplication(sys.argv)

overlay = PortalOverlay()
overlay.show()

#temp test portal
overlay.set_orange(500, 500)
overlay.set_blue(900, 500)

sys.exit(app.exec())