"""
1 - Instalar o driver de conexao

Python - Linguagem de programacao
SQL - Linguagem do Banco de Dados

pip install mysql-connector

host    -> Onde esta o banco de dados 
user    -> O usuario que tem permissao de manipular o banco
passwd  -> Senha do user
db      -> Qual eh o banco que eu vou acessar

"""
import mysql.connector

# ============== Conectar ao Banco ==============

conexao = mysql.connector.connect(
    host='localhost',
    user='admin',
    passwd='admin1234',
    db='meu_banco'
)
# print(conexao)
# conexao.close()
cursor = conexao.cursor()

# ============== Inserir dados ==============

def inserir_um():
    nome = input("Nome do cliente: ")
    endereco = input("Endereco: ")
    cpf = input("CPF: ")

    sql = "INSERT INTO clientes (nomes, enderecos, cpfs) VALUES (%s, %s, %s);" # Esse ';' faz diferenca?
    val = (nome,endereco,cpf)

    cursor.execute(sql, val)
    conexao.commit()

    print(f"Foram adicionados {cursor.rowcount} registros.")
    print(f"O derradeiro cliente tem id {cursor.lastrowid}.")

# inserir_um()


# ============== Visualizar ==============

def mostra_todos():
    sql = 'SELECT * FROM clientes'

    cursor.execute(sql)

    # res1 = cursor.fetchmany(size=3)
    resultados = cursor.fetchall()

    """You must fetch all rows for the current query 
        before executing new statements using the 
        same connection.""" 

    for reg in resultados:
        print(reg)
    
# mostra_todos()
# print()


# ============== Excluir ==============

def excluir_um():
    apagar = input("Digite o id a apagar: ")

    sql = "DELETE FROM clientes WHERE id = " + apagar

    cursor.execute(sql)

    conexao.commit()

    print(f"{cursor.rowcount} registros apagados.")

# excluir_um()


# ============== Editar ==============

def editar():
    novo_cpf = "132.132.132.22"

    mudar = input("ID a mudar o CPF: ")

    # sql = f"UPDATE clientes SET cpfs='{novo_cpf}' WHERE id='{mudar}'"
    sql = "UPDATE clientes SET cpfs='%s' WHERE id='%s'"
    val = (novo_cpf, mudar)

    cursor.execute(sql, val)
    
    conexao.commit()

# editar()
# mostra_todos()

sql = "SELECT * FROM clientes WHERE cpfs='3'"
r = cursor.execute(sql)
if r==None:
    print("NONE")
else:
    print(r)