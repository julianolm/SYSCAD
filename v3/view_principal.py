from PySide2.QtWidgets import QWidget, QApplication, QPushButton, QFrame, QLabel, QLineEdit
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


        '''
        Frame Cadastrar ==============================================================
        Invisivel ate que seu botao seja clicado
        '''
        global frm_cadastrar
        self.frm_cadastrar = QFrame(self)
        self.frm_cadastrar.setGeometry(170, 0, 830, 700)
        self.frm_cadastrar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frm_cadastrar.setVisible(False)

        self.lbl_nome = QLabel("Nome", self.frm_cadastrar)
        self.lbl_nome.setGeometry(20, 50, 55, 16)
        
        self.lbl_endereco = QLabel("Endereco", self.frm_cadastrar)
        self.lbl_endereco.setGeometry(20, 90, 55, 16)

        self.lbl_cpf = QLabel("CPF", self.frm_cadastrar)
        self.lbl_cpf.setGeometry(20, 130, 55, 16)

        self.txt_nome = QLineEdit(self.frm_cadastrar)
        self.txt_nome.setGeometry(80, 50, 721, 22)

        self.txt_endereco = QLineEdit(self.frm_cadastrar)
        self.txt_endereco.setGeometry(80, 90, 721, 22)

        self.txt_cpf = QLineEdit(self.frm_cadastrar)
        self.txt_cpf.setGeometry(80, 130, 721, 22)

        self.btn_limpar = QPushButton('Limpar', self.frm_cadastrar)
        self.btn_limpar.setGeometry(20, 650, 115, 22)

        self.btn_gravar = QPushButton('Gravar', self.frm_cadastrar)
        self.btn_gravar.setGeometry(700, 650, 115, 22)


        '''
        Frame Pesquisar ==============================================================
        Invisivel ate que seu botao seja clicado
        '''
        global frm_pesquisar
        self.frm_pesquisar = QFrame(self)
        self.frm_pesquisar.setGeometry(170, 0, 830, 700)
        self.frm_pesquisar.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.frm_pesquisar.setVisible(False)

        '''
        Frame Relatorio ==============================================================
        Invisivel ate que seu botao seja clicado
        '''
        global frm_relatorio
        self.frm_relatorio = QFrame(self)
        self.frm_relatorio.setGeometry(170, 0, 830, 700)
        self.frm_relatorio.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.frm_relatorio.setVisible(False)

        '''
        Frame Editar ==============================================================
        Invisivel ate que seu botao seja clicado
        '''
        global frm_editar
        self.frm_editar = QFrame(self)
        self.frm_editar.setGeometry(170, 0, 830, 700)
        self.frm_editar.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.frm_editar.setVisible(False)

        global all_frames
        all_frames = (self.frm_cadastrar, self.frm_pesquisar, 
                      self.frm_relatorio, self.frm_editar)
    
    
    def ocultar_frames(self):
        global all_frames
        for frame in all_frames: ### AQUI ELE USOU SELF.ALL_FRAMES E NO MEU ISSO DEU ERRO, PQ ?????????????
            if frame.isVisible() == True:
                frame.setVisible(False)


    def executa_btn_cadastrar(self):
        global frm_cadastrar
        self.ocultar_frames()
        self.frm_cadastrar.setVisible(True)

    def executa_btn_pesquisar(self):
        global frm_pedquisar
        self.ocultar_frames()
        self.frm_pesquisar.setVisible(True)

    def executa_btn_relatorio(self):
        global frm_relatorio
        self.ocultar_frames()
        self.frm_relatorio.setVisible(True)
        
    def executa_btn_editar(self):
        global frm_editar
        self.ocultar_frames()
        self.frm_editar.setVisible(True)
        

def executa():

    myApp = QApplication.instance()

    if myApp is None:
        myApp = QApplication(sys.argv)

    janela = Window()
    janela.show()
    myApp.exec_()

executa()