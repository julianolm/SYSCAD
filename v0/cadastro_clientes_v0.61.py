"""Versao 0.61 (Implementacao alternativa da versao 0.6)

    Implementa Operacao 5 - Editar - (editar_cliente)

    Referencia: https://www.youtube.com/watch?v=BoC55k0q05o (nao foi seguido nessa versao, so na 0.6)
    
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

def excluir_cliente(cpf):
    global Nomes, Enderecos, Cpfs

    limpar_tela()
    print("Relatorio >>>>>>")
    print("....")
    
    c = pesquisar_cliente(cpf)
    if c is not -1:
        print("Tem certeza que deseja excluir cliente?")
        print(f"{Nomes[c]} :: {Cpfs[c]}")
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
    global Nomes, Enderecos, Cpfs
    limpar_tela()
    c = pesquisar_cliente(cpf)
    if c is not -1:
        editar = True
        while (editar):
            limpar_tela()
            print(f"{Nomes[c]} :: {Cpfs[c]} :: {Enderecos[c]}")
            print("|============= EDICAO =============|")
            print("| [1]- Alterar Nome                |")
            print("| [2]- Alterar CPF                 |")
            print("| [3]- Alterar Endereco            |")
            print("| [0]- Concluir Edicao             |")
            op = input("> ")

            if op=="1":
                print(f"Nome atual: {Nomes[c]}")
                novo_nome = input("Novo nome: ")
                Nomes[c] = novo_nome
                limpar_tela()
                print("Editando...\n")
                print("Nome alterado com sucesso!")
            elif op=="2":
                print(f"CPF atual: {Cpfs[c]}")
                novo_cpf = input("Novo CPF: ")
                Cpfs[c] = novo_cpf
                limpar_tela()
                print("Editando...\n")
                print("CPF alterado com sucesso!")
            elif op=="3":
                print(f"Endereco atual: {Enderecos[c]}")
                novo_endereco = input("Novo endereco: ")
                Enderecos[c] = novo_endereco
                limpar_tela()
                print("Editando...\n")
                print("Endereco alterado com sucesso!")
            elif op=="0":
                editar = False
                limpar_tela()
                print("Edicao concluida!")
            else:
                print("Opcao invalida!")

            input("[ENTER] para continuar...")
    else:
        print("Cliente nao encontrado!")
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
            cpf = input("CPF do cliente: ")
            excluir_cliente(cpf)

        elif op == '5':
            cpf = input("CPF: ")
            editar_cliente(cpf)

        elif op == '0':
            print("Fim do sistema...")
            pode_continuar = False

        else:
            limpar_tela()
            print("Opcao invalida")
            input("[ENTER] para continuar...")
            limpar_tela()