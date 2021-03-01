from PySide2.QtWidgets import QApplication, QWidget, QLabel
from PySide2.QtGui import QIcon, QPixmap

import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Primeira View PySide")
        self.setGeometry(350,150,700,525) # x(esq), y(topo), width, height
        self.setMinimumWidth(700)
        self.setMinimumHeight(500)
        self.setMaximumWidth(800)
        self.setMaximumHeight(600)
        self.setToolTip("Janela Login")

        self.setAutoFillBackground(True)
        self.setStyleSheet('background-color: #00bfff;')

        appIcon = QIcon("imagens/icone.png")
        self.setWindowIcon(appIcon)

        self.set_img()

    def set_img(self):
        #icone 1
        icone1 = QIcon('imagens/icon_check.png')
        label1 = QLabel('Palavra', self)
        pixmap1 = icone1.pixmap(100, 100, QIcon.Active)

        # label1.setPixmap(pixmap1)

        #icone 2
        icone2 = QIcon('imagens/icon_check.png')
        label2 = QLabel('Palavra', self)
        label2.move(100,0)
        pixmap2 = icone2.pixmap(100, 100, QIcon.Disabled)

        # label2.setPixmap(pixmap2)

        #icone 3
        icone3 = QIcon('imagens/icon_check.png')
        label3 = QLabel('Palavra', self)
        label3.move(200,0)
        pixmap3 = icone3.pixmap(100, 100, QIcon.Selected)

        # label3.setPixmap(pixmap3)      

myApp = QApplication(sys.argv)

janela = Window()
janela.show()

myApp.exec_()
sys.exit(0)