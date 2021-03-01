"""Versao 0.1

    Referencia: https://www.youtube.com/watch?v=8MuKwAGsx4Q

"""

import os

def limpar_tela():
    os.system("cls")

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


print("==================>> SYSCAD <<================== [V: 0.1]")

login = input("Usuario: ")
senha = input("Senha: ")

if validar_usuario(login, senha):
    print("MENU")