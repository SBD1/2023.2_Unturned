import psycopg2

import sys
sys.path.append('..')

from Database import DataBase

conn = psycopg2.connect(
    host="172.20.0.2",           
    database="unturned",     
    user="postgres",             
    password="postgres"
)

cursor = conn.cursor()

# DataBase.drop_all_tables(conn)



# DataBase.inserir_arma_branca(conn, cursor, 1, sala=1, inventario=1, nome="faca", dano="100", material="aço")

# DataBase.inserir_arma_fogo()

# DataBase.create_new_animal()

# Fechar o cursor e a conexão
cursor.close()
conn.close()
