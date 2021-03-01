import modelo as db

DB_CLIENTES = 'syscad'

def cadastrar_cliente(nome, endereco, cpf):
    con = db.conecta_ao_banco(DB_CLIENTES)
    db.insere_dados(con, nome, endereco, cpf)


def exibir_clientes():
    con = db.conecta_ao_banco(DB_CLIENTES)
    resultados = db.exibir_relatorio(con)

    return resultados


def pesquisar_cliente(cpf=None, nome=None):
    con = db.conecta_ao_banco(DB_CLIENTES)
    resultados = db.pesquisar_cliente(con, cpf)

    return resultados


def excuir_cliente(cpf):
    res = pesquisar_cliente(cpf)

    if res != None: # testar se a pesuisa realmente retorna "None" em algum caso
        linha = 0

        if len(res) > 1:
            print("Mais de um resultado encontrado!")
            print(res)
            id_apagar = int(input("Digite um id: "))

            while linha < len(res):
                if res[linha][0] == id_apagar:
                    break
                linha += 1

        print("Tem certeza que realmente deseja excluir?")
        print(f"Cliente: {res[linha][1]} :: CPF: {res[linha][3]}")
        op = input("[S] Sim > ")
        if op.lower() == 's':
            con = db.conecta_ao_banco(DB_CLIENTES)
            db.excluir_dados(con, res[linha][0])
            print("Dado excluido com sucesso!")