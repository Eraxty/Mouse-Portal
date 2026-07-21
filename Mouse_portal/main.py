import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
from portal import Portal
from teleport import Teleporter

app = QApplication(sys.argv)

orange = Portal("assets/portal_orange.png", "MousePortalOrange")
blue = Portal("assets/portal_blue.png", "MousePortalBlue")

orange.show()
blue.show()

teleporter = Teleporter(orange, blue)

timer = QTimer()
timer.timeout.connect(teleporter.check)
timer.start(20)
sys.exit(app.exec())
