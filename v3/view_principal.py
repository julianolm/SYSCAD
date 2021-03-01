from PySide2.QtWidgets import QWidget, QApplication, QPushButton
from PySide2.QtGui import QFont

import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,1000,700)

        self.setStyleSheet("Background-color: rgb(7, 105, 114);")

        self.carregar_formulario()

    
    def carregar_formulario(self):
        fonte = QFont("/home/juliandev/projects/SYSCAD/v3/fonts/Open_Sans/OpenSans-Regular.ttf")

        self.btn_cadastrar = QPushButton("CADASTRAR", self)
        self.btn_cadastrar.setGeometry(0, 0, 170, 50)
        self.btn_cadastrar.setFont(fonte)
        self.btn_cadastrar.setStyleSheet("color:white")
        self.btn_cadastrar.clicked.connect(self.executa_btn_cadastrar)

        self.btn_pesquisar = QPushButton("PESQUISAR", self)
        self.btn_pesquisar.setGeometry(0, 50, 170, 50)
        self.btn_pesquisar.setFont(fonte)
        self.btn_pesquisar.setStyleSheet("color:white")
        self.btn_pesquisar.clicked.connect(self.executa_btn_pesquisar)

        self.btn_relatorio = QPushButton("RELATORIO", self)
        self.btn_relatorio.setGeometry(0, 100, 170, 50)
        self.btn_relatorio.setFont(fonte)
        self.btn_relatorio.setStyleSheet("color:white")
        self.btn_relatorio.clicked.connect(self.executa_btn_relatorio)

        self.btn_editar = QPushButton("EDITAR", self)
        self.btn_editar.setGeometry(0, 150, 170, 50)
        self.btn_editar.setFont(fonte)
        self.btn_editar.setStyleSheet("color:white")
        self.btn_editar.clicked.connect(self.executa_btn_editar)


    def executa_btn_cadastrar(self):
        print("Executando cadastrar")
    def executa_btn_pesquisar(self):
        print("Executando pesquisar")
    def executa_btn_relatorio(self):
        print("Executando relatorio")
    def executa_btn_editar(self):
        print("Executando editar")


def executa():

    myApp = QApplication.instance()

    if myApp is None:
        myApp = QApplication(sys.argv)

    janela = Window()
    janela.show()
    myApp.exec_()