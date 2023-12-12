from adventures.russia import russia
import psycopg2

import sys
sys.path.append('..')

from Database import DataBase

conn = psycopg2.connect(
    host="172.25.0.2",           
    database="unturned",     
    user="postgres",             
    password="postgres"
)

cursor = conn.cursor()


try:
    while True:
        DataBase.drop_all_tables(conn)
        DataBase.create_tables(conn, cursor)
        DataBase.triggers_procedures(conn, cursor)
        DataBase.create_adventure(conn, cursor)
        russia()  

except KeyboardInterrupt:
    DataBase.drop_all_tables(conn)
    cursor.close()
    conn.close()
    print("\nCtrl+C detectado. Encerrando o programa.")
    
