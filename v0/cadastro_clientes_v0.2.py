"""Versao 0.2

    Referencia: https://www.youtube.com/watch?v=HpQtl6NVkhE

"""

import os

def limpar_tela():
    os.system("clear")

def cadastrar_cliente():
    limpar_tela()
    print("Cadastrando...")
    input("[ENTER] para continuar...")

def exibir_cliente():
    limpar_tela()
    print("Relatorio...")
    input("[ENTER] para continuar...")

def pesquisar_cliente():
    limpar_tela()
    print("Pesquisando...")
    input("[ENTER] para continuar...")

def excluir_cliente():
    limpar_tela()
    print("Excluindo...")
    input("[ENTER] para continuar...")

def editar_cliente():
    limpar_tela()
    print("Editando...")
    input("[ENTER] para continuar...")

def validar_usuario(us, pw):
    if us=='cad01' and pw==('1010'):
        return True
    return False


print("==================>> SYSCAD <<================== [V: 0.2]")

login = input("Usuario: ")
senha = input("Senha: ")

if validar_usuario(login, senha):
    pode_continuar = True
    while pode_continuar:
        print("|============== MENU ==============|")
        print("| [1]- CADASTRAR                   |")
        print("| [2]- RELATORIO                   |")
        print("| [3]- PESQUISAR                   |")
        print("| [4]- EXCLUIR                     |")
        print("| [5]- EDITAR                      |")
        print("| [0]- SAIR                        |")
        op = input("> ")

        if op == '1':
            cadastrar_cliente()
        elif op == '2':
            exibir_cliente()
        elif op == '3':
            pesquisar_cliente()
        elif op == '4':
            excluir_cliente()
        elif op == '5':
            editar_cliente()
        elif op == '0':
            print("Fim do sistema...")
            pode_continuar = False

        else:
            limpar_tela()
            print("Opcao invalida")
            input("[ENTER] para continuar...")
            limpar_tela()