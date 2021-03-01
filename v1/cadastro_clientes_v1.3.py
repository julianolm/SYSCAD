"""Versao 1.1

    Implementa a barra de progresso e ocultando a senha do usuario

    Referencia: https://www.youtube.com/watch?v=0Skt6R9oDDk&list=PLbWheOnk6aV4CUBW0E-3aPhDO6V5Afyo4&index=20
                https://www.youtube.com/watch?v=3INbYdJwMyo&list=PLbWheOnk6aV4CUBW0E-3aPhDO6V5Afyo4&index=21

"""

import os

from termcolor import colored
from time import sleep
from prettytable import PrettyTable
from progressbar import ProgressBar
from getpass import getpass



def limpar_tela():
    os.system("clear")


def cadastrar_cliente(nome, endereco, cpf):
    global Nomes, Enderecos, Cpfs

    limpar_tela()

    Nomes.append(nome)
    Enderecos.append(endereco)
    Cpfs.append(cpf)

    print("CADASTRANDO >>>>>>\n")
    print(f"Cliente {nome} cadastrado com sucesso!")

    input("[ENTER] para continuar...")


def exibir_um_cliente(i):
    global Nomes, Enderecos, Cpfs

    print(f"Nome    : {Nomes[i]}")
    print(f"Endereco: {Enderecos[i]}")
    print(f"CPF     : {Cpfs[i]}")


def exibir_clientes():
    global Nomes, Enderecos, Cpfs

    limpar_tela()
    print("Relatorio >>>>>>\n")

    t = PrettyTable(["NOME", "ENDERECO", "CPF"])
    for i in range(len(Nomes)):
        t.add_row([Nomes[i], Enderecos[i], Cpfs[i]])

    print(t)
    input("[ENTER] para continuar...")

def pesquisar_cliente(cpf=None, nome=None, chamada_direta=True):
    global Cpfs

    limpar_tela()
    
    if chamada_direta:
        print("RELATORIO >>>>>>")
        print("....")

    if cpf in Cpfs:
        return Cpfs.index(cpf)
    return -1


def excluir_cliente(cpf):
    global Nomes, Enderecos, Cpfs
    c = pesquisar_cliente(cpf)

    if c is not -1:
        print(colored("EXCLUIR CLIENTE >>>>>>\n...", "red"))
        print(f"{Nomes[c]} :: {Cpfs[c]}")
        print(colored("Tem certeza que deseja excluir cliente?", "red", 'on_yellow'))
        r = input("([S] - Sim): ")
        if r.lower() == "s":
            del(Nomes[c])
            del(Enderecos[c])
            del(Cpfs[c])
            print("Cliente excluido com sucesso!")
        else:
            print("Operacao cancelada!")
    else:
        print("Cliente nao encontrado!")
    
    input("[ENTER] para continuar...")


def editar_cliente(cpf):
    limpar_tela()
    global Nomes, Enderecos, Cpfs

    c = pesquisar_cliente(cpf)

    if c is not -1:
        print(f"{Nomes[c]}")
        print(f"{Enderecos[c]}")
        print(f"{Cpfs[c]}")
        print("___________")
        print("Digite o novo valor ou [ENTER] para manter o atual.")
        novo_n = input("Novo nome     : ")
        novo_e = input("Novo endereco : ")
        novo_c = input("Novo CPF     : ")

        if novo_n != "":
            Nomes[c] = novo_n
        if novo_e != "":
            Enderecos[c] = novo_e
        if novo_c != "":
            Cpfs[c] = novo_c

        print("Dados alterados com sucesso!")

    else:
        print("Cliente nao encontrado!")

    input("[ENTER] para continuar...")


def validar_usuario(us, pw):
    if us=='cad01' and pw==('1010'):
        return True
    return False


def exibir_menu():
    print("|============== MENU ==============|")
    menu = PrettyTable(["OPCAO", "ITEM"])
    menu.align["ITEM"] = 'l'
    menu.add_row(["[1]","CADASTRAR               "])
    menu.add_row(["[2]","RELATORIO"])
    menu.add_row(["[3]","PESQUISAR"])
    menu.add_row(["[4]","EXCLUIR"])
    menu.add_row(["[5]","EDITAR"])
    menu.add_row(["[0]","SAIR"])
    print(menu)


def loading():
    limpar_tela()
    print("Carregando modulos\nPor favor, aguarde!\n")
    barra = ProgressBar()
    for i in barra(range(25)):
        sleep(0.1)


#=================================================================================

Nomes = []
Enderecos = []
Cpfs = []

loading()

print(colored("==================>> SYSCAD <<================== [V: 0.2]", "green"))
login = input("Usuario  : ")
senha = getpass("Senha    : ")

if validar_usuario(login, senha):
    pode_continuar = True
    
    while pode_continuar:
        limpar_tela()
        exibir_menu()
        op = input("> ")

        if op == '1':
            n = input("Nome do cliente      : ")
            e = input("Endereco do cliente  : ")
            c = input("CPF do cliente       : ")
            cadastrar_cliente(n, e, c)

        elif op == '2':
            exibir_clientes()

        elif op == '3':
            c = input("CPF: ")
            p = pesquisar_cliente(c)
            
            if p is not -1:
                exibir_um_cliente(p)
            else:
                print("Cliente nao encontrado!")
                
            input("[ENTER] para continuar...")

        elif op == '4':
            cpf = input("CPF do cliente: ")
            excluir_cliente(cpf)

        elif op == '5':
            cpf = input("CPF do cliente: ")
            editar_cliente(cpf)

        elif op == '0':
            print("Fim do sistema...")
            pode_continuar = False

        else:
            limpar_tela()
            print("Opcao invalida")
            input("[ENTER] para continuar...")
            limpar_tela()


"""
Pesquisar tanto por nome quanto por cpf
Adicionar o 'deseja cadastrar outro cliente' em cadastrar
Criar um cadastro de novos usuarios
"""