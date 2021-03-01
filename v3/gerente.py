import view_login as vl, view_principal as vp

import sys

def carrega_sistema():
    logou = vl.executa()
    if logou == True:
        print("Estas logado meu amigo")
        vp.executa()
    else:
        print("Ainda nao logou")
    
carrega_sistema()
sys.exit(0)