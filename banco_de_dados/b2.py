'''
  No tut do Margeylson ele nao estava especificando o campo "nome do host", 
  estava ficando como "qualquer host" depois que eu alterei para "localhost" 
  a conexao funcionou.
'''

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin1234",
    db="banco1"
)
print(db)
