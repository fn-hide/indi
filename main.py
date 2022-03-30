import sys

from PyQt5.QtWidgets import QApplication
from controller import Controller
from view import View
from model import Model



app = QApplication(sys.argv)

view = View()
view.show()

model = Model()

Controller(model, view)

sys.exit(app.exec_())





