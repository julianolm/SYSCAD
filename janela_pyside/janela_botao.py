from PySide2.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QMessageBox

import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.monta_formulario()

    def monta_formulario(self):
        btn = QPushButton("Ok", self)
        btn.move(50,100)
        btn.clicked.connect(self.acao_botao)

    def acao_botao(self):
        resposta = QMessageBox.question(self, "Confirmacao", 'Voce clicou no botao?', QMessageBox.Yes | QMessageBox.No)
        if resposta == QMessageBox.Yes:
            print('Clicou mesmo no botao!')
        else:
            print('Nao clicou nao!')

myApp = QApplication(sys.argv)

janela = Window()
janela.show()

myApp.exec_()
sys.exit()