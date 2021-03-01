"""Versao 0.4

    Implementa Operacao 3 - Pesquisar (pesquisar_cliente)

    Referencia: https://www.youtube.com/watch?v=Qr70DHptlkA&t=4s
    
"""

import os

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

    for i in range(len(Nomes)):
        exibir_um_cliente(i)
        print("______________________________________________")

    input("[ENTER] para continuar...")

def pesquisar_cliente(cpf=None, nome=None):
    global Cpfs

    limpar_tela()

    print("Pesquisando >>>>>>")
    print("....")

    if cpf in Cpfs:
        return Cpfs.index(cpf)
    return -1

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

#=================================================================================

Nomes = []
Enderecos = []
Cpfs = []

print("==================>> SYSCAD <<================== [V: 0.2]")
# login = input("Usuario  : ")
# senha = input("Senha    : ")

if validar_usuario("cad01","1010"):#(login, senha):
    pode_continuar = True
    
    while pode_continuar:
        limpar_tela()
        print("|============== MENU ==============|")
        print("| [1]- CADASTRAR                   |")
        print("| [2]- RELATORIO                   |")
        print("| [3]- PESQUISAR                   |")
        print("| [4]- EXCLUIR                     |")
        print("| [5]- EDITAR                      |")
        print("| [0]- SAIR                        |")
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