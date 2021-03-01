from PySide2.QtWidgets import QWidget, QApplication

import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,1000,700)
        self.setStyleSheet("Background-color: rgb(7, 105, 114);")

def executa():

    myApp = QApplication.instance()

    if myApp is None:
        myApp = QApplication(sys.argv)

    janela = Window()
    janela.show()
    myApp.exec_()