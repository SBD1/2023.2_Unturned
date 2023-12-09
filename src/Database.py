import psycopg2
# import pandas as pd
# from classes import *
# import random


class DataBase():

    def create_connection():
        connect = psycopg2.connect(
            host="172.21.0.3",           
            database="mydatabase",     
            user="myuser",             
            password="mysecretpassword")
        return connect
    
    def create_new_pc(connection,id, sala,nome, vida, stamina):
        cursor = connection.cursor()

        querry = "CALL inserirPersonagem(id, sala, nome, vida, stamina, NULL, NULL, NULL)" % (
            id,sala,nome, vida, stamina)

        cursor.execute(querry)

        connection.commit()
        cursor.close()

    def create_new_zumbi(connection,id,vida, classe, dano):
        cursor = connection.cursor()

        querry = "CALL inserirPersonagem(id, NULL, NULL, vida, NULL, classe, dano, NULL)" % (
            id,vida, classe, dano)

        cursor.execute(querry)

        connection.commit()
        cursor.close()

    def create_new_animal(connection,id,vida, especie):
        cursor = connection.cursor()

        querry = "CALL inserirPersonagem(id, NULL, NULL, vida, NULL, NULL, NULL, especie)" % (
            id,vida, especie)

        cursor.execute(querry)

        connection.commit()
        cursor.close()

    def update_animal(connection,id,vida, especie):
        cursor = connection.cursor()

        querry = "CALL updateAnimal(id, vida, especie)" % (
            id,vida, especie)

        cursor.execute(querry)

        connection.commit()
        cursor.close()
    
    def update_zumbi(connection,id,vida, classe, dano):
        cursor = connection.cursor()

        querry = "CALL updateZumbi(id, vida, classe, dano)" % (
            id,vida, classe, dano)

        cursor.execute(querry)

        connection.commit()
        cursor.close()

    def update_pc(connection,id, sala,nome, vida, stamina):
        cursor = connection.cursor()

        querry = "CALL updatePC(id, sala,nome, vida, stamina)" % (
            id,sala,nome, vida, stamina)

        cursor.execute(querry)

        connection.commit()
        cursor.close()

    def delete_pc(connection,id):
        cursor = connection.cursor()

        querry = "CALL deletePC(id)" % (
            id)

        cursor.execute(querry)

        connection.commit()
        cursor.close()

    def delete_zumbi(connection,id):
        cursor = connection.cursor()

        querry = "CALL deleteZumbi(id)" % (
            id)

        cursor.execute(querry)

        connection.commit()
        cursor.close()
    
    def delete_animal(connection,id):
        cursor = connection.cursor()

        querry = "CALL deleteAnimal(id)" % (
            id)

        cursor.execute(querry)

        connection.commit()
        cursor.close()