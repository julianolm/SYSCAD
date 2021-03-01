from PySide2.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel, QMessageBox
from PySide2.QtGui import QFont, QIcon, QPixmap

import controle as c

import sys

class Window(QWidget):
    global logou, tentativas
    logou = False
    tentativas = 0
    def __init__(self):
        super().__init__()

        self.setFixedSize(400,600)
        self.setWindowTitle("SysCad :: Login")
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color:white;")

        self.definir_formulario()
        self.definir_imagens()


    def definir_formulario(self):
        global txt_usuario, txt_senha
        
        fonte = QFont("fonts/Open_Sans/OpenSans-Regular.ttf")
        fonte.setPointSize(11)

        txt_usuario = QLineEdit(self)
        txt_usuario.setPlaceholderText("Login")
        txt_usuario.setFont(fonte)
        txt_usuario.setGeometry(10,240,381,41)

        txt_senha = QLineEdit(self)
        txt_senha.setPlaceholderText("Senha")
        txt_senha.setFont(fonte)
        txt_senha.setGeometry(10,320,381,41)
        txt_senha.setEchoMode(QLineEdit.EchoMode.Password)

        btn_logar = QPushButton("Ok", self)
        btn_logar.setFont(fonte)
        btn_logar.setGeometry(10,390,381,41)
        btn_logar.setAutoFillBackground(True)
        btn_logar.setStyleSheet("background-color:rgb(7,105,114);color:white;")
        btn_logar.clicked.connect(self.validar_login)
        

    def definir_imagens(self):
        appIcon = QIcon("/home/juliandev/projects/SYSCAD/v3/images/fav_icon.png")
        img_login = QIcon("/home/juliandev/projects/SYSCAD/v3/images/icon_login.png")
        img_base = QIcon("/home/juliandev/projects/SYSCAD/v3/images/icon_login_base.png")

        pixmap_login = img_login.pixmap(191,191)
        pixmap_base = img_base.pixmap(400,220)

        lbl_login = QLabel('login', self)
        lbl_login.setPixmap(pixmap_login)
        lbl_login.move(100,10)

        lbl_base = QLabel('Base', self)
        lbl_base.setPixmap(pixmap_base)
        lbl_base.setGeometry(0,440, 411, 161)

        self.setWindowIcon(appIcon)

    def validar_login(self):
        global tentativas, logou

        usr = txt_usuario.text()
        psw = txt_senha.text()

        if c.validar_usuario(usr, psw):
            logou = True
            self.close()
        else:
            if tentativas<3:
                msg = QMessageBox()
                msg.setText("Usuario ou senha incorretos")
                msg.exec()
                tentativas += 1
                if tentativas == 3:
                    sys.exit(0)



def executa():
    global logou

    myApp = QApplication.instance()

    if myApp is None:
        myApp = QApplication(sys.argv)

    janela = Window()
    janela.show()
    
    myApp.exec_()
    return logou