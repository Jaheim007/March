import sys 
from PyQt5.QtWidgets import QMainWindow, QApplication
from Widgets.mars import AccountPage_web

def main():
    app = QApplication(sys.argv)
    home = AccountPage_web()
    home.show()
    app.exec_()


if __name__ == '__main__':
    main()