import mysql.connector

def conecta_ao_banco(banco):
    conexao = mysql.connector.connect(
        host='localhost',
        user='syscad',
        passwd='101010',
        db=banco
    )

    return conexao

def insere_dados(conexao, nome, endereco, cpf):
    sql = "INSERT INTO clientes (nomes, enderecos, cpfs) VALUES (%s, %s, %s)"
    valores = (nome, endereco, cpf)

    try: # eh sujeito a ocorrencia de um erro ao tentar adicionar
        cursor = conexao.cursor()
        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()
    
    except mysql.connector.Error as erro:
        if erro.errno == 1062: #CPF repetido
            print("Erro: o CPF inserido ja esta em uso!")

def exibir_relatorio(conexao):
    sql = 'SELECT * FROM clientes'
    
    cursor = conexao.cursor()
    cursor.execute(sql)

    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultados

def excluir_dados(conexao, id):
    sql = f"DELETE FROM clientes WHERE id='{id}';"
    
    cursor = conexao.cursor()
    cursor.execute(sql)

    conexao.commit()
    
    cursor.close()
    conexao.close()

def pesquisar_cliente(conexao, cpf=None, nome=None):
    sql = f"SELECT * FROM clientes WHERE cpfs LIKE '%{cpf}%'"

    cursor = conexao.cursor()
    cursor.execute(sql)
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultados
