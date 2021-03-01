from PySide2.QtWidgets import QWidget, QApplication, QLabel, QLineEdit
from PySide2.QtGui import QFont

import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(550,200,250,300)
        # self.setAutoFillBackground(True)
        # self.setStyleSheet("background-color: #00bfff;")

        self.cria_campos()

    def cria_campos(self):
        fonte = QFont("fonts/Open_Sans/OpenSans-Regular.ttf")
        fonte.setPointSize(11)

        lbl_nome = QLabel("Nome", self)
        lbl_nome.move(20,20)
        lbl_nome.setFont(fonte)

        campo1 = QLineEdit(self)
        campo1.move(20, 50)
        campo1.setFont(fonte)
        # campo1.setAutoFillBackground(True)
        # campo1.setStyleSheet("background-color: white;")

        campo2 = QLineEdit(self)
        campo2.move(20, 90)
        campo2.setFont(fonte)
        campo2.setPlaceholderText("Digite sua senha")
        campo2.setEchoMode(QLineEdit.EchoMode.Password)




myApp = QApplication(sys.argv)

janela = Window()
janela.show()

myApp.exec_()
sys.exit()