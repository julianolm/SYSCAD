from PySide2.QtWidgets import QWidget, QApplication

import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,800,600)

def executa():

    myApp = QApplication.instance()

    if myApp is None:
        myApp = QApplication(sys.agv)

    janela = Window()
    janela.show()
    myApp.exec_()