import psycopg2

# Parâmetros de conexão
dbname = 'test_db'
user = 'root'
password = 'root'
host = 'localhost'
port = '5432'

# Nome do arquivo SQL a ser executado
sql_file = 'DDL'

# Tentar conectar
try:
    connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

    cursor = connection.cursor()

    with open(sql_file, 'r') as file:
        cursor.execute(file.read())

    results = cursor.fetchall()
    for row in results:
        print(row)

    connection.commit()
    connection.close()

except psycopg2.Error as e:
    print('Erro ao conectar ao PostgreSQL:', e)
