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

    def insert_veiculo_terrestre(connection,id, sala, nome, vida, combustivel, numRodas):
        cursor = connection.cursor()

        querry = "CALL insere_veiculo(id, sala, nome, vida, combustivel, numRodas::smallint, NULL::int, NULL::int)" % (
            id, sala, nome, vida, combustivel, numRodas)

        cursor.execute(querry)

        connection.commit()
        cursor.close()

    def insert_veiculo_aquatico(connection,id, sala, nome, vida, combustivel, propulsao):
        cursor = connection.cursor()

        querry = "CALL insere_veiculo(id, sala, nome, vida, combustivel, NULL::smallint, propulsao, NULL::int)" % (
            id, sala, nome, vida, combustivel, propulsao)

        cursor.execute(querry)

        connection.commit()
        cursor.close()

    def insert_veiculo_aereo(connection,id, sala, nome, vida, combustivel, maxAltitude):
        cursor = connection.cursor()

        querry = "CALL insere_veiculo(id, sala, nome, vida, combustivel, NULL::smallint, NULL::int, maxAltitude);" % (
            id, sala, nome, vida, combustivel, maxAltitude)

        cursor.execute(querry)

        connection.commit()
        cursor.close()

    def update_veiculo_terrestre(connection,id, sala, nome, vida, combustivel, numRodas):
        cursor = connection.cursor()

        querry = "CALL update_veiculo(id, sala, nome, vida, combustivel, numRodas::smallint, NULL::int, NULL::int)" % (
            id, sala, nome, vida, combustivel, numRodas)

        cursor.execute(querry)

        connection.commit()
        cursor.close()

    def update_veiculo_aquatico(connection,id, sala, nome, vida, combustivel, propulsao):
        cursor = connection.cursor()

        querry = "CALL update_veiculo(id, sala, nome, vida, combustivel, NULL::smallint, propulsao::int, NULL::int)" % (
            id, sala, nome, vida, combustivel, propulsao)

        cursor.execute(querry)

        connection.commit()
        cursor.close()
    
    def update_veiculo_aereo(connection,id, sala, nome, vida, combustivel, maxAltitude):
        cursor = connection.cursor()

        querry = "CALL update_veiculo(id, sala, nome, vida, combustivel, NULL::smallint, NULL::int, maxAltitude::int)" % (
            id, sala, nome, vida, combustivel, maxAltitude)

        cursor.execute(querry)

        connection.commit()
        cursor.close()

    def remover_veiculo(connection,id):
        cursor = connection.cursor()

        querry = "CALL removerVeiculo(id)" % (
            id)

        cursor.execute(querry)

        connection.commit()
        cursor.close()
    
    def inserir_arma_branca(connection,id, sala, inventario, nome, dano, material):
        cursor = connection.cursor()

        querry = "CALL inserirBranca(id, sala, inventario, nome, dano, material)" % (
            id, sala, inventario, nome, dano, material)

        cursor.execute(querry)

        connection.commit()
        cursor.close()
    
    def inserir_arma_fogo(connection,id, sala, inventario, nome, dano, distancia, capacidadeMunicao):
        cursor = connection.cursor()

        querry = "CALL inserirFogo(id, sala, inventario, nome, dano, distancia, capacidadeMunicao)" % (
            id, sala, inventario, nome, dano, distancia, capacidadeMunicao)

        cursor.execute(querry)

        connection.commit()
        cursor.close()
    
    def inserir_alimento(connection,id, sala, inventario, status, nome):
        cursor = connection.cursor()

        querry = "CALL inserirBranca(id, sala, inventario, status, nome)" % (
            connection,id, sala, inventario, status, nome)

        cursor.execute(querry)

        connection.commit()
        cursor.close()

    def inserir_ferramenta(connection,id, sala, inventario, durabilidade, nome):
        cursor = connection.cursor()

        querry = "CALL inserirFerramenta(id, sala, inventario, durabilidade, nome)" % (
            connection,id, sala, inventario, durabilidade, nome)

        cursor.execute(querry)

        connection.commit()
        cursor.close()

    def update_ferramenta(connection,id, sala, inventario, durabilidade, nome):
        cursor = connection.cursor()

        querry = "CALL atualizarFerramenta(id, sala, inventario, durabilidade, nome)" % (
            connection,id, sala, inventario, durabilidade, nome)

        cursor.execute(querry)

        connection.commit()
        cursor.close()

    def update_alimento(connection,id, sala, inventario, status, nome):
        cursor = connection.cursor()

        querry = "CALL atualizarAlimento(id, sala, inventario, status, nome)" % (
            connection,id, sala, inventario, status, nome)

        cursor.execute(querry)

        connection.commit()
        cursor.close()
    
    def update_arma_branca(connection,id, sala, inventario, nome, dano, material):
        cursor = connection.cursor()

        querry = "CALL atualizarBranca(id, sala, inventario, nome, dano, material)" % (
            id, sala, inventario, nome, dano, material)

        cursor.execute(querry)

        connection.commit()
        cursor.close()

    def update_arma_fogo(connection,id, sala, inventario, nome, dano, distancia, capacidadeMunicao):
        cursor = connection.cursor()

        querry = "CALL atualizarFogo(id, sala, inventario, nome, dano, distancia, capacidadeMunicao)" % (
            id, sala, inventario, nome, dano, distancia, capacidadeMunicao)

        cursor.execute(querry)

        connection.commit()
        cursor.close()

    def delete_arma_fogo(connection,id):
        cursor = connection.cursor()

        querry = "CALL deletarFogo(id)" % (
            id)

        cursor.execute(querry)

        connection.commit()
        cursor.close()
    
    def delete_arma_branca(connection,id):
        cursor = connection.cursor()

        querry = "CALL deletarBranca(id)" % (
            id)

        cursor.execute(querry)

        connection.commit()
        cursor.close()
    
    def delete_alimento(connection,id):
        cursor = connection.cursor()

        querry = "CALL deletarAlimento(id)" % (
            id)

        cursor.execute(querry)

        connection.commit()
        cursor.close()
    
    def delete_ferramenta(connection,id):
        cursor = connection.cursor()

        querry = "CALL deletarFerramenta(id)" % (
            id)

        cursor.execute(querry)

        connection.commit()
        cursor.close()
