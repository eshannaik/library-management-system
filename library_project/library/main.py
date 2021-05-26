import sys

from PyQt5.QtWidgets import QApplication

from .views import window
from .database import createConnection

def main():
	app = QApplication(sys.argv)

	if not createConnection("library.sqlite"):
		sys.exit(1)

	win = window()
	win.show()

	sys.exit(app.exec())
