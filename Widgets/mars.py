from PyQt5.QtWidgets import QMainWindow, QApplication
from Widgets.March import Ui_MainWindow

class AccountPage_web(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)