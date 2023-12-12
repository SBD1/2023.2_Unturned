import psycopg2

class DataBase():
    
    def create_new_pc(connection, id, sala, nome, vida, stamina):
        cursor = connection.cursor()

        query = "CALL inserirPersonagem(%s, %s, %s, %s, %s, NULL, NULL, NULL)"

        parameters = (id, sala, nome, vida, stamina)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

        
    def update_pc(connection, id, sala, nome, vida, stamina):
        cursor = connection.cursor()

        # Usando espaços reservados (%s) para evitar injeção de SQL
        query = "CALL updatePC(%s, %s, %s, %s, %s)"
        
        # Passando os parâmetros como uma tupla
        parameters = (id, sala, nome, vida, stamina)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()


    def delete_pc(connection,id):
        cursor = connection.cursor()

        query = "CALL deletePC(%s)" 
        parameters = (id)


        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def create_new_zumbi(connection,id,vida, classe, dano):
        cursor = connection.cursor()

        query = "CALL inserirPersonagem(%s, NULL, NULL, %s, NULL, %s, %s, NULL)" 
        parameters = (id,vida, classe, dano)

        cursor.execute(query, parameters)
        cursor = connection.cursor()

        connection.commit()
        cursor.close()

    def create_new_animal(connection,id,vida, especie):
        cursor = connection.cursor()

        query = "CALL inserirPersonagem(%s, NULL, NULL, %s, NULL, NULL, NULL, %s)" 
        parameters = (id,vida, especie)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def update_animal(connection,id,vida, especie):
        cursor = connection.cursor()

        query = "CALL updateAnimal(%s, %s, %s)" 
        parameters =  (id,vida, especie)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()
    
    def update_zumbi(connection,id,vida, classe, dano):
        cursor = connection.cursor()

        query = "CALL updateZumbi(%s, %s, %s, %s)" 
        parameters = (id,vida, classe, dano)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def delete_zumbi(connection,id):
        cursor = connection.cursor()

        query = "CALL deleteZumbi(%s)" 
        parameters = (id)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()
    
    def delete_animal(connection,id):
        cursor = connection.cursor()

        query = "CALL deleteAnimal(%s)" 
        parameters = (id)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def insert_veiculo_terrestre(connection,id, sala, nome, vida, combustivel, numRodas):
        cursor = connection.cursor()

        query = "CALL insere_veiculo(%s, %s, %s, %s, %s, %s::smallint, NULL::int, NULL::int)" 
        parameters = (id, sala, nome, vida, combustivel, numRodas)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def insert_veiculo_aquatico(connection,id, sala, nome, vida, combustivel, propulsao):
        cursor = connection.cursor()

        query = "CALL insere_veiculo(%s, %s, %s, %s, %s, NULL::smallint, %s, NULL::int)" 
        parameters = (id, sala, nome, vida, combustivel, propulsao)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def insert_veiculo_aereo(connection,id, sala, nome, vida, combustivel, maxAltitude):
        cursor = connection.cursor()

        query = "CALL insere_veiculo(%s, %s, %s, %s, %s, NULL::smallint, NULL::int, %s)" 
        parameters = (id, sala, nome, vida, combustivel, maxAltitude)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def update_veiculo_terrestre(connection,id, sala, nome, vida, combustivel, numRodas):
        cursor = connection.cursor()

        query = "CALL update_veiculo(%s, %s, %s, %s, %s, %s::smallint, NULL::int, NULL::int)" 
        parameters = (id, sala, nome, vida, combustivel, numRodas)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def update_veiculo_aquatico(connection,id, sala, nome, vida, combustivel, propulsao):
        cursor = connection.cursor()

        query = "CALL update_veiculo(%s, %s, %s, %s, %s, NULL::smallint, %s::int, NULL::int)" 
        parameters = (id, sala, nome, vida, combustivel, propulsao)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()
    
    def update_veiculo_aereo(connection,id, sala, nome, vida, combustivel, maxAltitude):
        cursor = connection.cursor()

        query = "CALL update_veiculo(%s, %s, %s, %s, %s, NULL::smallint, NULL::int, %s::int)" 
        parameters = (id, sala, nome, vida, combustivel, maxAltitude)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def remover_veiculo(connection,id):
        cursor = connection.cursor()

        query = "CALL removerVeiculo(%s)" 
        parameters = (id)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()
    
    def inserir_arma_branca(connection, id, sala, nome, dano, material):
        cursor = connection.cursor()

        try:
            query = "CALL inserirBranca(%s, %s, NULL, %s, %s, %s)"

            parameters = (id, sala, nome, dano, material)

            cursor.execute(query, parameters)

            connection.commit()

        except Exception as e:
            print(f"Erro ao inserir arma branca: {e}")

        finally:
            cursor.close()

    
    def inserir_arma_fogo(connection,id, sala,  nome, dano, distancia, capacidadeMunicao):
        cursor = connection.cursor()

        query = "CALL inserirFogo(%s, %s, NULL, %s, %s, %s, %s)"

        parameters = (id, sala, nome, dano, distancia, capacidadeMunicao)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()
    
    def inserir_alimento(connection,id, sala, status, nome):
        cursor = connection.cursor()

        query = "CALL inserirAlimento(%s, %s, NULL, %s, %s)" 
        parameters = (id, sala, status, nome)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def inserir_ferramenta(connection,id, sala, durabilidade, nome):
        cursor = connection.cursor()

        query = "CALL inserirFerramenta(%s, %s, NULL, %s, %s)" 
        parameters = (id, sala, durabilidade, nome)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def update_ferramenta(connection,id, sala, inventario, durabilidade, nome):
        cursor = connection.cursor()

        query = "CALL atualizarFerramenta(%s, %s, %s, %s, %s)" 
        parameters = (id, sala, inventario, durabilidade, nome)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def update_alimento(connection,id, sala, inventario, status, nome):
        cursor = connection.cursor()

        query = "CALL atualizarAlimento(%s, %s, %s, %s, %s)" 
        parameters = (id, sala, inventario, status, nome)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()
    
    def update_arma_branca(connection, id, sala, inventario, nome, dano, material):
        cursor = connection.cursor()

        query = "CALL atualizarBranca(%s, %s, %s, %s, %s, %s)" 
        parameters = (sala, id, inventario, nome, dano, material)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def update_arma_fogo(connection,id, sala, inventario, nome, dano, distancia, capacidadeMunicao):
        cursor = connection.cursor()

        query = "CALL atualizarFogo(%s, %s, %s, %s, %s, %s, %s)" 
        parameters = (id, sala, inventario, nome, dano, distancia, capacidadeMunicao)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def delete_arma_fogo(connection,id):
        cursor = connection.cursor()

        query = "CALL deletarFogo(%s)" 
        parameters = (id)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()
    
    def delete_arma_branca(connection,id):
        cursor = connection.cursor()

        query = "CALL deletarBranca(%s)" 
        parameters = (id)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()
    
    def delete_alimento(connection,id):
        cursor = connection.cursor()

        query = "CALL deletarAlimento(%s)" 
        parameters = (id)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()
    
    def delete_ferramenta(connection,id):
        cursor = connection.cursor()

        query = "CALL deletarFerramenta(%s)" 
        parameters = (id)

        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def select_mapa_descricao(conn, cursor):
        cursor.execute("SELECT descricao FROM Mapa WHERE nomeMapa = 'Russia';")

        # Recuperar o resultado da consulta
        row = cursor.fetchone()

        # Imprimir a descrição se houver um resultado
        if row:
            print(f"{row[0]}")
        else:
            print("Não há descrição para Russia.")    

    def select_sala_descricao(conn, cursor, nome):
        cursor.execute(f"SELECT descricao FROM Sala WHERE nome = '{nome}';")

        # Recuperar o resultado da consulta
        row = cursor.fetchone()

        # Imprimir a descrição se houver um resultado
        if row:
            print(f"{row[0]}")
        else:
            print(f"Não há descrição para {nome}")
    
    def insert_mapa(connection, id, dimensao, nome, descricao):
        cursor = connection.cursor()

        query = "INSERT INTO Mapa (idMapa, dimensao, nomeMapa, descricao) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (id, dimensao, nome, descricao))

        connection.commit()
        cursor.close()


    def insert_cidade(connection, nome, mapa):
        cursor = connection.cursor()

        query = "INSERT INTO Cidade (nome, mapa, nroConstrucoes) VALUES (%s, %s, DEFAULT)"
        cursor.execute(query, (nome, mapa))

        connection.commit()
        cursor.close()


    def insert_sala(connection, id, nome, cidade, descricao):
        cursor = connection.cursor()

        query = "INSERT INTO Sala (idSala, nome, cidade, descricao) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (id, nome, cidade, descricao))

        connection.commit()
        cursor.close()


    def update_mapa(connection, id, dimensao, nome, descricao):
        cursor = connection.cursor()

        query = "UPDATE Mapa SET dimensao = %s, nomeMapa = %s, descricao = %s WHERE idMapa = %s"
        parameters = (dimensao, nome, descricao, id)
        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def update_cidade(connection, nome, mapa, nroConstrucoes):
        cursor = connection.cursor()

        query = "UPDATE Cidade SET mapa = %s, nroConstrucoes = %s WHERE nome = %s"
        parameters = (mapa, nroConstrucoes, nome)
        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def update_sala(connection, id, nome, cidade, descricao):
        cursor = connection.cursor()

        query = "UPDATE Sala SET nome = %s, cidade = %s, descricao = %s WHERE idSala = %s"
        parameters = (nome, cidade, descricao, id)
        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def delete_mapa(connection, id):
        cursor = connection.cursor()

        query = "DELETE FROM Mapa WHERE idMapa = %s"
        parameters = (id)
        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def delete_cidade(connection, nome):
        cursor = connection.cursor()

        query = "DELETE FROM Cidade WHERE nome = %s"
        parameters = (nome)
        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def delete_sala(connection, id):
        cursor = connection.cursor()

        query = "DELETE FROM Sala WHERE idSala = %s"
        parameters = (id)
        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def insert_instancia(connection, idInstancia, NPC, sala):
        cursor = connection.cursor()

        query = "INSERT INTO Instancia (idInstancia, NPC, sala) VALUES (%s, %s, %s)"
        parameters = (idInstancia, NPC, sala)
        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def update_instancia(connection, idInstancia, NPC, sala):
        cursor = connection.cursor()

        query = "UPDATE Instancia SET NPC = %s, sala = %s WHERE idInstancia = %s"
        parameters = (NPC, sala, idInstancia)
        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()
    
    def delete_instancia(conn, instance_id):
        query = "DELETE FROM Instancia WHERE idInstancia = %s;"
        parameters = (instance_id,)
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        conn.commit()
        cursor.close()


    def insert_missao(connection, idMissao, idPersonagem, descricao, recompensa, estado):
        cursor = connection.cursor()

        query = "INSERT INTO Missao (idMissao, idPersonagem, Descricao, Recompensa, Estado) VALUES (%s, %s, %s, %s, %s)"
        parameters = (idMissao, idPersonagem, descricao, recompensa, estado)
        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def update_missao(connection, idMissao, idPersonagem, descricao, recompensa, estado):
        cursor = connection.cursor()

        query = "UPDATE Missao SET idPersonagem = %s, Descricao = %s, Recompensa = %s, Estado = %s WHERE idMissao = %s"
        cursor.execute(query, (idPersonagem, descricao, recompensa, estado, idMissao))

        connection.commit()
        cursor.close()
    
    def delete_missao(connection, idMissao):
        cursor = connection.cursor()

        query = "DELETE FROM Missao WHERE idMissao = %s"
        cursor.execute(query, (idMissao,))

        connection.commit()
        cursor.close()
    
    def insert_criador(connection, idCriador, idPersonagem, nome):
        cursor = connection.cursor()

        query = "INSERT INTO Criador (idCriador, idPersonagem, nome) VALUES (%s, %s, %s)"
        parameters = (idCriador, idPersonagem, nome)
        cursor.execute(query, parameters)

        connection.commit()
        cursor.close()

    def update_criador(connection, idCriador, idPersonagem, nome):
        cursor = connection.cursor()

        query = "UPDATE Criador SET idPersonagem = %s, nome = %s WHERE idCriador = %s"
        cursor.execute(query, (idPersonagem, nome, idCriador))

        connection.commit()
        cursor.close()

    def delete_criador(connection, idCriador):
        cursor = connection.cursor()

        query = "DELETE FROM Criador WHERE idCriador = %s"
        cursor.execute(query, (idCriador,))

        connection.commit()
        cursor.close()

    def inserir_receita(connection,idReceita, idCriador, idItem, Resultado, Requisitos, TempoCriacao):
        cursor = connection.cursor()

        query = "INSERT INTO Receita (idReceita, idCriador, idItem, Resultado, Requisitos, TempoCriacao) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (idReceita, idCriador, idItem, Resultado, Requisitos, TempoCriacao))

        connection.commit()
        cursor.close()

    def update_receita(connection,idReceita, idCriador, idItem, Resultado, Requisitos, TempoCriacao):
        cursor = connection.cursor()

        query = "UPDATE Receita SET idReceita = %s, idCriador = %s,idItem = %s, Resultado = %s,Requisitos = %s, TempoCriacao = %s WHERE idCriador = %s"
        cursor.execute(query, (idReceita, idCriador, idItem, Resultado, Requisitos, TempoCriacao))

        connection.commit()
        cursor.close()

    def delete_receita(connection, idReceita):
        cursor = connection.cursor()

        query = "DELETE FROM Receita WHERE idReceita = %s"
        cursor.execute(query, (idReceita))

        connection.commit()
        cursor.close()

    
    def inserir_mapa(conn, cursor):
        dados_mapa = {
            "idMapa": 1,
            "dimensao": 5,
            "nomeMapa": "Russia",
            "descricao": """
                \n===== Início na Rússia - Terra Desolada =====
                Você acorda em uma cidade russa devastada, onde os edifícios estão em ruínas e as ruas estão vazias.
                O ar está impregnado com um silêncio tenso, quebrado apenas pelos gemidos distantes de zumbis.
                A temperatura está abaixo de zero, e a neve cobre o chão, tornando cada passo mais desafiador.
                Seu objetivo é sobreviver. Procure por abrigos, suprimentos e outros sobreviventes.
                Lembre-se, o inimigo não é apenas o frio, mas também os mortos-vivos que espreitam por toda parte.
                Boa sorte, sobrevivente. A Rússia tornou-se um campo de batalha, e sua habilidade de sobrevivência será testada.
            """
        }

        comando_sql_mapa = """
            INSERT INTO Mapa (idMapa, dimensao, nomeMapa, descricao)
            VALUES (%(idMapa)s, %(dimensao)s, %(nomeMapa)s, %(descricao)s)
            RETURNING idMapa;
        """

        cursor.execute(comando_sql_mapa, dados_mapa)
        id_mapa = cursor.fetchone()[0]

        conn.commit()

        return id_mapa
    
    def inserir_cidade(conn, cursor, nome_cidade, id_mapa):
        dados_cidade = {
            "nome": nome_cidade,
            "mapa": id_mapa,
            "nroConstrucoes": 0,
        }

        comando_sql_cidade = """
            INSERT INTO Cidade (nome, mapa, nroConstrucoes)
            VALUES (%(nome)s, %(mapa)s, %(nroConstrucoes)s);
        """

        cursor.execute(comando_sql_cidade, dados_cidade)

        conn.commit()

    def inserir_sala(conexao, cursor, nome_cidade, nome_sala, descricao_sala):
        dados_sala = {
            "cidade": nome_cidade,
            "nome": nome_sala,
            "descricao": descricao_sala,
        }

        # Comando SQL para inserção na tabela Sala
        comando_sql_sala = """
            INSERT INTO Sala (cidade, nome, descricao)
            VALUES (%(cidade)s, %(nome)s, %(descricao)s);
        """

        # Executar o comando SQL com os dados
        cursor.execute(comando_sql_sala, dados_sala)

        # Confirmar a transação
        conexao.commit()

    def inserir_inventario(conexao, cursor, idPersonagem=1, quantidadeItens=0, maxItens=100):
        dados_inventario = {
            "personagem": idPersonagem,
            "quantidadeItens": quantidadeItens,
            "maxItens": maxItens
        }

        comando_sql_inventario = """
            INSERT INTO Inventario (personagem, quantidadeItens, maxItens)
            VALUES (%(personagem)s, %(quantidadeItens)s, %(maxItens)s);
        """

        cursor.execute(comando_sql_inventario, dados_inventario)

        conexao.commit()


    def drop_personagem(connection, cursor):
        query = "DROP TABLE pc;"
    
        cursor.execute(query)

        connection.commit()
        cursor.close()


    def drop_all_tables(conn):
        cursor = conn.cursor()
        # Desativa as chaves estrangeiras temporariamente
        # Dropa as tabelas
        tables_to_drop = [
            'Branca', 'Fogo', 'Arma', 'Alimento', 'Ferramenta',
            'Inventario', 'Receita', 'Item', 'Criador', 'Missao',
            'Instancia', 'Animal', 'Zumbi', 'NPC', 'PC', 'Personagem',
            'Aereo', 'Aquatico', 'Terrestre', 'Veiculo', 'Sala',
            'Cidade', 'Mapa'
        ]
        for table in tables_to_drop:
            cursor.execute(f"DROP TABLE IF EXISTS {table};")
        # Ativa as chaves estrangeiras novamente
        # Commit para efetivar as alterações
        conn.commit()
        print("Todas as tabelas foram dropadas com sucesso.")

    def triggers_procedures(conn, cursor):

        sql_commands = [
            """
            CREATE OR REPLACE FUNCTION count_numero_salas() RETURNS TRIGGER AS $$
            BEGIN
                IF (TG_OP = 'INSERT') THEN
                    UPDATE Cidade SET nroConstrucoes = nroConstrucoes + 1 
                        WHERE Cidade.nome = NEW.cidade;
                ELSIF (TG_OP = 'UPDATE') THEN 
                    IF NEW.cidade <> OLD.cidade THEN
                        UPDATE Cidade SET nroConstrucoes = nroConstrucoes + 1 
                            WHERE Cidade.nome = NEW.cidade;
                        UPDATE Cidade SET nroConstrucoes = nroConstrucoes - 1 
                            WHERE Cidade.nome = OLD.cidade;
                    END IF;
                ELSIF (TG_OP = 'DELETE') THEN
                    UPDATE Cidade SET nroConstrucoes = nroConstrucoes - 1
                        WHERE Cidade.nome = OLD.cidade;
                END IF;
                RETURN NULL;
            END;
            $$ LANGUAGE plpgsql;

            CREATE TRIGGER count_numero_salas
            AFTER INSERT OR UPDATE OR DELETE ON Sala 
            FOR EACH ROW EXECUTE FUNCTION count_numero_salas();
            """,
            """
            CREATE OR REPLACE PROCEDURE insere_veiculo(_id INT, _sala INT, _nome VARCHAR(255), _vida INT, _combustivel INT, _numRodas SMALLINT, _propulsao INT, _maxAltitude INT)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _maxAltitude IS NULL AND _propulsao IS NULL AND _numRodas IS NULL THEN
                RAISE EXCEPTION 'Precisa ter uma variável específica NOT NULL';
            ELSIF _maxAltitude IS NOT NULL AND _propulsao IS NOT NULL AND _numRodas IS NOT NULL THEN
                RAISE EXCEPTION 'Precisa ter apenas uma variável específica NOT NULL';
            ELSIF _maxAltitude IS NOT NULL AND _propulsao IS NOT NULL THEN 
                RAISE EXCEPTION 'Precisa ter apenas uma variável específica NOT NULL';
            ELSIF _maxAltitude IS NOT NULL AND _numRodas IS NOT NULL THEN 
                RAISE EXCEPTION 'Precisa ter apenas uma variável específica NOT NULL';
            ELSIF _propulsao IS NOT NULL AND _numRodas IS NOT NULL THEN
                RAISE EXCEPTION 'Precisa ter apenas uma variável específica NOT NULL';
            ELSIF _maxAltitude IS NOT NULL THEN
                INSERT INTO Veiculo VALUES (_id, 'Aereo');
                INSERT INTO Aereo VALUES (_id, _sala, _nome, _vida, _combustivel, _maxAltitude);
            ELSIF _propulsao IS NOT NULL THEN
                INSERT INTO Veiculo VALUES (_id, 'Aquatico');
                INSERT INTO Aquatico VALUES (_id, _sala, _nome, _vida, _combustivel, _propulsao);
            ELSIF _numRodas IS NOT NULL THEN
                INSERT INTO Veiculo VALUES (_id, 'Terrestre');
                INSERT INTO Terrestre VALUES (_id, _sala, _nome, _vida, _numRodas, _combustivel);
            END IF;
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE update_veiculo(_id INT, _sala INT, _nome VARCHAR(255), _vida INT, _combustivel INT, _numRodas SMALLINT, _propulsao INT, _maxAltitude INT)
            LANGUAGE plpgsql AS $$
            BEGIN
                    IF _maxAltitude IS NULL AND _propulsao IS NULL AND _numRodas IS NULL THEN
                RAISE EXCEPTION 'Precisa ter uma variável específica NOT NULL';
            ELSIF _maxAltitude IS NOT NULL AND _propulsao IS NOT NULL AND _numRodas IS NOT NULL THEN
                RAISE EXCEPTION 'Precisa ter apenas uma variável específica NOT NULL';
            ELSIF _maxAltitude IS NOT NULL AND _propulsao IS NOT NULL THEN 
                RAISE EXCEPTION 'Precisa ter apenas uma variável específica NOT NULL';
            ELSIF _maxAltitude IS NOT NULL AND _numRodas IS NOT NULL THEN 
                RAISE EXCEPTION 'Precisa ter apenas uma variável específica NOT NULL';
            ELSIF _propulsao IS NOT NULL AND _numRodas IS NOT NULL THEN
                RAISE EXCEPTION 'Precisa ter apenas uma variável específica NOT NULL';

            ELSIF _maxAltitude IS NOT NULL THEN
                PERFORM * FROM Aquatico WHERE _id = Aquatico.idVeiculo;
                IF FOUND THEN
                    DELETE FROM Aquatico WHERE _id = Aquatico.idVeiculo;
                    INSERT INTO Aereo VALUES (_id, _sala, _nome, _vida, _combustivel, _maxAltitude);
                    UPDATE Veiculo SET tipo = 'Aereo' WHERE idVeiculo = _id;
                END IF;
                PERFORM * FROM Terrestre WHERE _id = Terrestre.idVeiculo;
                IF FOUND THEN
                    DELETE FROM Terrestre WHERE _id = Terrestre.idVeiculo;
                    INSERT INTO Aereo VALUES (_id, _sala, _nome, _vida, _combustivel, _maxAltitude);
                    UPDATE Veiculo SET tipo = 'Aereo' WHERE idVeiculo = _id;
                END IF;
                PERFORM * FROM Aereo WHERE _id = Aereo.idVeiculo;
                IF FOUND THEN
                    UPDATE Aereo SET sala = _sala, nome = _nome, vida = _vida, combustivel = _combustivel, maxAltitude = _maxAltitude WHERE idVeiculo = _id;
                ELSE 
                    RAISE EXCEPTION 'O id colocado não existe na tabela Aéreo';
                END IF;

            ELSIF _numRodas IS NOT NULL THEN
                PERFORM * FROM Aquatico WHERE _id = Aquatico.idVeiculo;
                IF FOUND THEN
                    DELETE FROM Aquatico WHERE _id = Aquatico.idVeiculo;
                    INSERT INTO Terrestre VALUES (_id, _sala, _nome, _vida, _numRodas, _combustivel);
                    UPDATE Veiculo SET tipo = 'Terrestre' WHERE idVeiculo = _id;
                END IF;
                PERFORM * FROM Aereo WHERE _id = Aereo.idVeiculo;
                IF FOUND THEN
                    DELETE FROM Aereo WHERE _id = Aereo.idVeiculo;
                    INSERT INTO Terrestre VALUES (_id, _sala, _nome, _vida, _numRodas, _combustivel);
                    UPDATE Veiculo SET tipo = 'Terrestre' WHERE idVeiculo = _id;
                END IF;
                PERFORM * FROM Terrestre WHERE _id = Terrestre.idVeiculo;
                IF FOUND THEN
                    UPDATE Terrestre SET sala = _sala, nome = _nome, vida = _vida, numRodas = _numRodas, combustivel = _combustivel WHERE idVeiculo = _id;
                ELSE 
                    RAISE EXCEPTION 'O id colocado não existe na tabela Terrestre';
                END IF;

            ELSIF _propulsao IS NOT NULL THEN
                PERFORM * FROM Terrestre WHERE _id = Terrestre.idVeiculo;
                IF FOUND THEN
                    DELETE FROM Terrestre WHERE _id = Terrestre.idVeiculo;
                    INSERT INTO Aquatico VALUES (_id, _sala, _nome, _vida, _combustivel, _propulsao);
                    UPDATE Veiculo SET tipo = 'Aquatico' WHERE idVeiculo = _id;
                END IF;
                PERFORM * FROM Aereo WHERE _id = Aereo.idVeiculo;
                IF FOUND THEN
                    DELETE FROM Aereo WHERE _id = Aereo.idVeiculo;
                    INSERT INTO Aquatico VALUES (_id, _sala, _nome, _vida, _combustivel, _propulsao);
                    UPDATE Veiculo SET tipo = 'Aquatico' WHERE idVeiculo = _id ;
                END IF;
                PERFORM * FROM Aquatico WHERE _id = Aquatico.idVeiculo;
                IF FOUND THEN
                    UPDATE Aquatico SET sala = _sala, nome = _nome, vida = _vida, combustivel = _combustivel, propulsao = _propulsao WHERE idVeiculo = _id;
                ELSE 
                    RAISE EXCEPTION 'O id colocado não está na tabela Aquatico';
                END IF;
            END IF;
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE removerVeiculo(_id INT)
            LANGUAGE plpgsql AS $$
            BEGIN
                    IF _id IS NULL THEN
                RAISE EXCEPTION 'Preciso de um id válido';
            ELSE
                PERFORM * FROM Veiculo WHERE Veiculo.idVeiculo = _id;
                IF FOUND THEN
                    PERFORM * FROM Aquatico WHERE Aquatico.idVeiculo = _id;
                    IF FOUND THEN 
                        DELETE FROM Aquatico WHERE Aquatico.idVeiculo = _id;
                    END IF;
                    PERFORM * FROM Terrestre WHERE Terrestre.idVeiculo = _id;
                    IF FOUND THEN
                        DELETE FROM Terrestre WHERE Terrestre.idVeiculo = _id;
                    END IF;
                    PERFORM * FROM Aereo WHERE Aereo.idVeiculo = _id;
                    IF FOUND THEN
                        DELETE FROM Aereo WHERE Aereo.idVeiculo = _id;
                    END IF;
                    DELETE FROM Veiculo WHERE Veiculo.idVeiculo = _id;
                ELSE 
                    RAISE EXCEPTION 'Esse id não existe';
                END IF;
            END IF;
            END $$;
            """,
            """
            CREATE OR REPLACE FUNCTION verifica_terrestres() RETURNS TRIGGER AS $verifica_terrestres$
            BEGIN
                PERFORM * FROM Aquatico WHERE Aquatico.idVeiculo = New.idVeiculo;
            IF FOUND THEN
                RAISE EXCEPTION 'ERRO: Já existe um veículo aquático com esse ID';
            END IF;

            PERFORM * FROM Aereo WHERE Aereo.idVeiculo = New.idVeiculo;
            IF FOUND THEN
                RAISE EXCEPTION 'ERRO: Já existe um veículo aéreo com esse ID';
            END IF;

            RETURN NEW;
            END;
            $verifica_terrestres$ LANGUAGE plpgsql;

            CREATE TRIGGER terrestres
            BEFORE INSERT OR UPDATE ON Terrestre
            FOR EACH ROW EXECUTE PROCEDURE verifica_terrestres();
            """,
            """
            CREATE OR REPLACE FUNCTION verifica_aquaticos() RETURNS TRIGGER AS $verifica_aquaticos$
            BEGIN
                PERFORM * FROM Terrestre WHERE Terrestre.idVeiculo = New.idVeiculo;
            IF FOUND THEN
                RAISE EXCEPTION 'ERRO: Já existe um veículo terrestre com esse ID';
            END IF;

            PERFORM * FROM Aereo WHERE Aereo.idVeiculo = New.idVeiculo;
            IF FOUND THEN
                RAISE EXCEPTION 'ERRO: Já existe um veículo aéreo com esse ID';
            END IF;

            RETURN NEW;
            END;
            $verifica_aquaticos$ LANGUAGE plpgsql;

            CREATE TRIGGER aquaticos
            BEFORE INSERT OR UPDATE ON Aquatico
            FOR EACH ROW EXECUTE PROCEDURE verifica_aquaticos();
            """,
            """
            CREATE OR REPLACE FUNCTION verifica_aereos() RETURNS TRIGGER AS $verifica_aereos$
            BEGIN
                PERFORM * FROM Terrestre WHERE Terrestre.idVeiculo = New.idVeiculo;
            IF FOUND THEN
                RAISE EXCEPTION 'ERRO: Já existe um veículo terrestre com esse ID';
            END IF;

            PERFORM * FROM Aquatico WHERE Aquatico.idVeiculo = New.idVeiculo;
            IF FOUND THEN
                RAISE EXCEPTION 'ERRO: Já existe um veículo aquático com esse ID';
            END IF;

            RETURN NEW;
            END;
            $verifica_aereos$ LANGUAGE plpgsql;

            CREATE TRIGGER aereos
            BEFORE INSERT OR UPDATE ON Aereo
            FOR EACH ROW EXECUTE PROCEDURE verifica_aereos();
            """,
            """
            CREATE OR REPLACE PROCEDURE inserirPersonagem(_id INT, _sala INT, _nome VARCHAR(255), _vida INT, _stamina INT, _classe VARCHAR(255), _dano INT, _especie VARCHAR(255))
            LANGUAGE plpgsql AS $$
            BEGIN
            IF _id IS NULL THEN
                RAISE EXCEPTION 'Preciso do id para criar o personagem';
            END IF;
            IF _nome IS NULL AND _stamina IS NULL AND _classe IS NULL AND _dano IS NULL AND _especie IS NULL THEN 
                RAISE EXCEPTION 'Preciso que coloque atributos especificos para eu saber onde guardar as informações';
            END IF;
            IF _classe IS NOT NULL AND _especie IS NOT NULL THEN
                RAISE EXCEPTION 'Posso ser ou animal, ou zumbi, não ambos ao mesmo tempo';
            END IF;
            IF _nome IS NOT NULL AND _stamina IS NOT NULL AND _classe IS NOT NULL AND _dano IS NOT NULL AND _especie IS NOT NULL THEN
                RAISE EXCEPTION 'Não posso ser NPC E PC ao mesmo tempo';
            END IF;
            IF _nome IS NOT NULL OR _stamina IS NOT NULL THEN
                INSERT INTO PERSONAGEM VALUES (_id, 'PC');
                INSERT INTO PC VALUES (_id, _sala, _nome, _vida, _stamina);
            ELSIF _classe IS NOT NULL THEN
                INSERT INTO PERSONAGEM VALUES (_id, 'NPC');
                INSERT INTO NPC VALUES (_id, 'Zumbi');
                INSERT INTO Zumbi VALUES (_id, _vida, _classe, _dano);
            ELSIF _especie IS NOT NULL THEN
                INSERT INTO PERSONAGEM VALUES (_id, 'NPC');
                INSERT INTO NPC VALUES (_id, 'Animal');
                INSERT INTO Animal VALUES (_id, _vida, _especie);
            END IF;
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE updateZumbi(_id INT, _vida INT, _classe VARCHAR(255), _dano INT)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _id IS NULL THEN
                RAISE EXCEPTION 'Preciso do id para fazer o update do zumbi';
            END IF;
            IF _vida IS NULL AND _classe IS NULL AND _dano IS NULL THEN
                RAISE EXCEPTION 'Preciso de todas os atributos específicos para atualizar o zumbi';
            END IF;
            PERFORM * FROM Zumbi WHERE idPersonagem = _id;
            IF NOT FOUND THEN 
                RAISE EXCEPTION 'Preciso de um id que exista na tabela Zumbi para fazer o update';
            END IF;
            IF _vida IS NOT NULL AND _classe IS NOT NULL AND _dano IS NOT NULL THEN
                UPDATE Zumbi SET vida = _vida, classe = _classe, dano = _dano WHERE idPersonagem = _id;
            ELSIF _vida IS NOT NULL AND _classe IS NOT NULL AND _dano IS NULL THEN
                UPDATE Zumbi SET vida =_vida, classe =_classe WHERE idPersonagem = _id;
            ELSIF _vida IS NOT NULL AND _classe IS NULL AND _dano IS NOT NULL THEN
                UPDATE Zumbi SET vida = _vida, dano = _dano WHERE idPersonagem = _id;
            ELSIF _vida IS NULL AND _classe IS NOT NULL AND _dano IS NOT NULL THEN
                UPDATE Zumbi SET classe = _classe, dano = _dano WHERE idPersonagem = _id;
            ELSIF _vida IS NOT NULL AND _classe IS NULL AND _dano IS NULL THEN
                UPDATE Zumbi SET vida = _vida WHERE idPersonagem = _id;
            ELSIF _vida IS  NULL AND _classe IS NOT NULL AND _dano IS NULL THEN
                UPDATE Zumbi SET classe = _classe WHERE idPersonagem = _id;
            ELSIF _vida IS  NULL AND _classe IS NULL AND _dano IS NOT NULL THEN
                UPDATE Zumbi SET dano = _dano WHERE idPersonagem = _id;
            END IF;
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE updateAnimal(_id INT, _vida INT, _especie VARCHAR(255))
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _id IS NULL THEN
                RAISE EXCEPTION 'Preciso do id para fazer o update do animal';
            END IF;
            IF _vida IS NULL AND _especie IS NULL THEN
                RAISE EXCEPTION 'Preciso dos atributos específicos para fazer o update';
            END IF;
            PERFORM * FROM Animal WHERE idPersonagem = _id;
            IF NOT FOUND THEN 
                RAISE EXCEPTION 'Preciso de um id que exista na tabela Animal para fazer o update';
            END IF;
            IF _vida IS NOT NULL AND _especie IS NOT NULL THEN
                UPDATE Animal SET vida = _vida, especie = _especie WHERE idPersonagem = _id;
            ELSIF _vida IS NOT NULL AND _especie IS NULL THEN
                UPDATE Animal SET vida = _vida WHERE idPersonagem = _id;
            ELSIF _vida IS NULL AND _especie IS NOT NULL THEN
                UPDATE Animal SET especie = _especie WHERE idPersonagem = _id;
            END IF;
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE updatePC(_id INT, _sala INT, _nome VARCHAR(255), _vida INT, _stamina INT)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _id IS NULL THEN
                RAISE EXCEPTION 'Preciso do id para dar o update no PC';
            END IF;
            IF _sala IS NULL AND _nome IS NULL AND _vida IS NULL AND _stamina IS NULL THEN
                RAISE EXCEPTION 'Preciso de ao menos um atributo específico para fazer o update';
            END IF;
            PERFORM * FROM PC WHERE idPersonagem = _id;
            IF NOT FOUND THEN 
                RAISE EXCEPTION 'Preciso de um id que exista na tabela PC para fazer o update';
            END IF;
            IF _sala IS NOT NULL AND _nome IS NOT NULL AND _vida IS NOT NULL AND _stamina IS NOT NULL THEN
                UPDATE PC SET sala = _sala, nome = _nome, vida = _vida, stamina = _stamina WHERE idPersonagem = _id;
            ELSIF _sala IS NOT NULL AND _nome IS NOT NULL AND _vida IS NOT NULL AND _stamina IS NULL THEN
                UPDATE PC SET sala = _sala, nome = _nome, vida = _vida WHERE idPersonagem = _id;
            ELSIF _sala IS NOT NULL AND _nome IS NOT NULL AND _vida IS NULL AND _stamina IS NOT NULL THEN
                UPDATE PC SET sala = _sala, nome = _nome, stamina = _stamina WHERE idPersonagem = _id;
            ELSIF _sala IS NOT NULL AND _nome IS NULL AND _vida IS NOT NULL AND _stamina IS NOT NULL THEN
                UPDATE PC SET sala = _sala, vida = _vida, stamina = _stamina WHERE idPersonagem = _id;
            ELSIF _sala IS  NULL AND _nome IS NOT NULL AND _vida IS NOT NULL AND _stamina IS NOT NULL THEN
                UPDATE PC SET nome = _nome, vida = _vida, stamina = _stamina WHERE idPersonagem = _id;
            ELSIF _sala IS NOT NULL THEN
                UPDATE PC SET sala = _sala WHERE idPersonagem = _id;
            ELSIF _nome IS NOT NULL THEN
                UPDATE PC SET nome = _nome WHERE idPersonagem = _id;
            ELSIF _vida IS NOT NULL THEN
                UPDATE PC SET vida = _vida WHERE idPersonagem = _id;
            ELSIF _stamina IS NOT NULL THEN
                UPDATE PC SET stamina = _stamina WHERE idPersonagem = _id;
            END IF;
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE deletePC(_id INT)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _id IS NULL THEN
                RAISE EXCEPTION 'Preciso do id do PC para deletá-lo';
            END IF;
            IF _id IS NOT NULL THEN
                PERFORM * FROM PC WHERE idPersonagem = _id;
                IF FOUND THEN
                    DELETE FROM PC WHERE idPersonagem = _id;
                    DELETE FROM Inventario WHERE personagem = _id;
                    DELETE FROM Missao WHERE idPersonagem = _id;
                    DELETE FROM Criador WHERE idPersonagem = _id;
                    DELETE FROM Personagem WHERE idPersonagem = _id;
                ELSIF NOT FOUND THEN
                    RAISE EXCEPTION 'Você não pode remover esse PC pois ele não existe';
                END IF;
            END IF;
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE deleteZumbi(_id INT)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _id IS NULL THEN
                RAISE EXCEPTION 'Preciso do id do Zumbi para deletá-lo';
            END IF;
            IF _id IS NOT NULL THEN
                PERFORM * FROM Zumbi WHERE idPersonagem = _id;
                IF FOUND THEN
                    DELETE FROM Instancia WHERE NPC = _id;
                    DELETE FROM Zumbi WHERE idPersonagem = _id;
                    DELETE FROM NPC WHERE idPersonagem = _id;
                    DELETE FROM Personagem WHERE idPersonagem = _id;
                ELSIF NOT FOUND THEN
                    RAISE EXCEPTION 'Você não pode remover esse Zumbi pois ele não existe';
                END IF;
            END IF;
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE deleteAnimal(_id INT)
            LANGUAGE plpgsql AS $$
            BEGIN
                    IF _id IS NULL THEN
                RAISE EXCEPTION 'Preciso do id do Animal para deletá-lo';
            END IF;
            IF _id IS NOT NULL THEN
                PERFORM * FROM Animal WHERE idPersonagem = _id;
                IF FOUND THEN
                    DELETE FROM Animal WHERE idPersonagem = _id;
                    DELETE FROM NPC WHERE idPersonagem = _id;
                    DELETE FROM Personagem WHERE idPersonagem = _id;
                ELSIF NOT FOUND THEN
                    RAISE EXCEPTION 'Você não pode remover esse Animal pois ele não existe';
                END IF;
            END IF;
            END $$;
            """,
            """
            CREATE OR REPLACE FUNCTION verifica_npcs() RETURNS TRIGGER AS $verifica_npcs$
            BEGIN
                PERFORM * FROM PC WHERE PC.idPersonagem = New.idPersonagem;
            IF FOUND THEN
                RAISE EXCEPTION 'ERRO: Já existe um PC com esse ID';
            END IF;

            RETURN NEW;
            END;
            $verifica_npcs$ LANGUAGE plpgsql;

            CREATE TRIGGER npcs
            BEFORE INSERT OR UPDATE ON NPC
            FOR EACH ROW EXECUTE PROCEDURE verifica_npcs();
            """,
            """
            CREATE OR REPLACE FUNCTION verifica_pcs() RETURNS TRIGGER AS $verifica_pcs$
            BEGIN
                PERFORM * FROM NPC WHERE NPC.idPersonagem = New.idPersonagem;
            IF FOUND THEN
                RAISE EXCEPTION 'ERRO: Já existe um NPC com esse ID';
            END IF;

            RETURN NEW;
            END;
            $verifica_pcs$ LANGUAGE plpgsql;

            CREATE TRIGGER pcs
            BEFORE INSERT OR UPDATE ON PC
            FOR EACH ROW EXECUTE PROCEDURE verifica_pcs();
            """,
            """
            CREATE OR REPLACE FUNCTION verifica_zumbis() RETURNS TRIGGER AS $verifica_zumbis$
            BEGIN
                PERFORM * FROM Animal WHERE Animal.idPersonagem = New.idPersonagem;
            IF FOUND THEN
                RAISE EXCEPTION 'ERRO: Já existe um Animal com esse ID';
            END IF;

            RETURN NEW;
            END;
            $verifica_zumbis$ LANGUAGE plpgsql;

            CREATE TRIGGER zumbis
            BEFORE INSERT OR UPDATE ON Zumbi
            FOR EACH ROW EXECUTE PROCEDURE verifica_zumbis();
            """,
            """
            CREATE OR REPLACE FUNCTION verifica_animais() RETURNS TRIGGER AS $verifica_animais$
            BEGIN
                PERFORM * FROM Zumbi WHERE Zumbi.idPersonagem = New.idPersonagem;
            IF FOUND THEN
                RAISE EXCEPTION 'ERRO: Já existe um Zumbi com esse ID';
            END IF;

            RETURN NEW;
            END;
            $verifica_animais$ LANGUAGE plpgsql;

            CREATE TRIGGER animais
            BEFORE INSERT OR UPDATE ON Animal
            FOR EACH ROW EXECUTE PROCEDURE verifica_animais();
            """,
                """
            CREATE OR REPLACE FUNCTION verifica_ferramentas() RETURNS TRIGGER AS $verifica_ferramentas$
            BEGIN
                PERFORM * FROM Alimento WHERE Alimento.idItem = New.idItem;
                IF FOUND THEN
                    RAISE EXCEPTION 'ERRO: Já existe um Alimento com esse ID';
                END IF;

                PERFORM * FROM Arma WHERE Arma.idItem = New.idItem;
                IF FOUND THEN
                    RAISE EXCEPTION 'ERRO: Já existe uma Arma com esse ID';
                END IF;

                RETURN NEW;
            END;
            $verifica_ferramentas$ LANGUAGE plpgsql;
            """,
            """
            CREATE TRIGGER ferramentas
            BEFORE INSERT OR UPDATE ON Ferramenta
            FOR EACH ROW EXECUTE PROCEDURE verifica_ferramentas();
            """,
            """
            CREATE OR REPLACE FUNCTION verifica_alimentos() RETURNS TRIGGER AS $verifica_alimentos$
            BEGIN
                PERFORM * FROM Ferramenta WHERE Ferramenta.idItem = New.idItem;
                IF FOUND THEN
                    RAISE EXCEPTION 'ERRO: Já existe uma Ferramenta com esse ID';
                END IF;

                PERFORM * FROM Arma WHERE Arma.idItem = New.idItem;
                IF FOUND THEN
                    RAISE EXCEPTION 'ERRO: Já existe uma Arma com esse ID';
                END IF;

                RETURN NEW;
            END;
            $verifica_alimentos$ LANGUAGE plpgsql;
            """,
            """
            CREATE TRIGGER alimentos
            BEFORE INSERT OR UPDATE ON Alimento
            FOR EACH ROW EXECUTE PROCEDURE verifica_alimentos();
            """,
            """
            CREATE OR REPLACE FUNCTION verifica_armas() RETURNS TRIGGER AS $verifica_armas$
            BEGIN
                PERFORM * FROM Ferramenta WHERE Ferramenta.idItem = New.idItem;
                IF FOUND THEN
                    RAISE EXCEPTION 'ERRO: Já existe uma Ferramenta com esse ID';
                END IF;

                PERFORM * FROM Alimento WHERE Alimento.idItem = New.idItem;
                IF FOUND THEN
                    RAISE EXCEPTION 'ERRO: Já existe um Alimento com esse ID';
                END IF;

                RETURN NEW;
            END;
            $verifica_armas$ LANGUAGE plpgsql;
            """,
            """
            CREATE TRIGGER armas
            BEFORE INSERT OR UPDATE ON Arma
            FOR EACH ROW EXECUTE PROCEDURE verifica_armas();
            """,
            """
            CREATE OR REPLACE FUNCTION verifica_fogos() RETURNS TRIGGER AS $verifica_fogos$
            BEGIN
                PERFORM * FROM Branca WHERE Branca.idItem = New.idItem;
                IF FOUND THEN
                    RAISE EXCEPTION 'ERRO: Já existe uma arma Branca com esse ID';
                END IF;

                RETURN NEW;
            END;
            $verifica_fogos$ LANGUAGE plpgsql;
            """,
            """
            CREATE TRIGGER fogos
            BEFORE INSERT OR UPDATE ON Fogo
            FOR EACH ROW EXECUTE PROCEDURE verifica_fogos();
            """,
            """
            CREATE OR REPLACE FUNCTION verifica_brancas() RETURNS TRIGGER AS $verifica_brancas$
            BEGIN
                PERFORM * FROM Fogo WHERE Fogo.idItem = New.idItem;
                IF FOUND THEN
                    RAISE EXCEPTION 'ERRO: Já existe uma arma de Fogo com esse ID';
                END IF;

                RETURN NEW;
            END;
            $verifica_brancas$ LANGUAGE plpgsql;
            """,
            """
            CREATE TRIGGER brancas
            BEFORE INSERT OR UPDATE ON Branca
            FOR EACH ROW EXECUTE PROCEDURE verifica_brancas();
            """,
            """
            CREATE OR REPLACE PROCEDURE inserirItem(_idItem INT, _tipo VARCHAR)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _idItem IS NULL THEN
                    RAISE EXCEPTION 'O ID do item é necessário para a criação.';
                END IF;
                IF _tipo IS NULL THEN
                    RAISE EXCEPTION 'O tipo do item é necessário para a criação.';
                END IF;

                IF _tipo NOT IN ('Ferramenta', 'Alimento', 'Arma') THEN
                    RAISE EXCEPTION 'O tipo do item deve ser Ferramenta, Alimento ou Arma.';
                END IF;

                INSERT INTO Item(idItem, tipo)
                VALUES (_idItem, _tipo);
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE inserirFerramenta(_idItem INT, _sala INT, _inventario INT, _durabilidade INT, _nome VARCHAR)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _idItem IS NULL OR _durabilidade IS NULL THEN
                    RAISE EXCEPTION 'Todos os campos devem ser preenchidos para inserir uma ferramenta.';
                END IF;

                CALL inserirItem(_idItem, 'Ferramenta');
                INSERT INTO Ferramenta(idItem, sala, inventario, durabilidade, nome)
                VALUES (_idItem, _sala, _inventario, _durabilidade, _nome);
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE inserirAlimento(_idItem INT, _sala INT, _inventario INT, _status VARCHAR, _nome VARCHAR)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _idItem IS NULL OR _status IS NULL THEN
                    RAISE EXCEPTION 'Todos os campos devem ser preenchidos para inserir um alimento.';
                END IF;

                CALL inserirItem(_idItem, 'Alimento');
                INSERT INTO Alimento(idItem, sala, inventario, status, nome)
                VALUES (_idItem, _sala, _inventario, _status, _nome);
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE inserirArma(_idItem INT, _tipo_arma VARCHAR)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _idItem IS NULL OR _tipo_arma IS NULL THEN
                    RAISE EXCEPTION 'Todos os campos devem ser preenchidos para inserir uma arma.';
                END IF;

                CALL inserirItem(_idItem, 'Arma');
                INSERT INTO Arma(idItem, tipo_arma)
                VALUES (_idItem, _tipo_arma);
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE inserirBranca(_idItem INT, _sala INT, _inventario INT, _nome VARCHAR, _dano INT, _material VARCHAR)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _idItem IS NULL OR _nome IS NULL OR _dano IS NULL OR _material IS NULL THEN
                    RAISE EXCEPTION 'Todos os campos devem ser preenchidos para inserir uma arma branca.';
                END IF;

                CALL inserirArma(_idItem, 'Branca');
                INSERT INTO Branca(idItem, sala, inventario, nome, dano, material)
                VALUES (_idItem, _sala, _inventario, _nome, _dano, _material);
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE inserirFogo(_idItem INT, _sala INT, _inventario INT, _nome VARCHAR, _dano INT, _distancia INT, _capacidadeMunicao INT)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _idItem IS NULL OR _nome IS NULL OR _dano IS NULL OR _distancia IS NULL OR _capacidadeMunicao IS NULL THEN
                    RAISE EXCEPTION 'Todos os campos devem ser preenchidos para inserir uma arma de fogo.';
                END IF;
                
                CALL inserirArma(_idItem, 'Fogo');
                INSERT INTO Fogo(idItem, sala, inventario, nome, dano, distancia, capacidadeMunicao)
                VALUES (_idItem, _sala, _inventario, _nome, _dano, _distancia, _capacidadeMunicao);
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE atualizarItem(_idItem INT, _tipo VARCHAR)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _idItem IS NULL OR _tipo IS NULL THEN
                    RAISE EXCEPTION 'O ID do item e o tipo são necessários para atualização.';
                END IF;
                UPDATE Item SET tipo = _tipo WHERE idItem = _idItem;
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE deletarItem(_idItem INT)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _idItem IS NULL THEN
                    RAISE EXCEPTION 'O ID do item é necessário para deleção.';
                END IF;
                DELETE FROM Item WHERE idItem = _idItem;
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE atualizarFerramenta(_idItem INT, _sala INT, _inventario INT, _durabilidade INT, _nome VARCHAR)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _idItem IS NULL OR _sala IS NULL OR _inventario IS NULL OR _durabilidade IS NULL THEN
                    RAISE EXCEPTION 'Todos os campos devem ser preenchidos para atualizar uma ferramenta.';
                END IF;

                UPDATE Ferramenta SET sala = _sala, inventario = _inventario, durabilidade = _durabilidade, nome = _nome WHERE idItem = _idItem;
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE deletarFerramenta(_idItem INT)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _idItem IS NULL THEN
                    RAISE EXCEPTION 'O ID da ferramenta é necessário para deleção.';
                END IF;

                DELETE FROM Ferramenta WHERE idItem = _idItem;
                CALL deletarItem(_idItem);
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE atualizarAlimento(_idItem INT, _sala INT, _inventario INT, _status VARCHAR, _nome VARCHAR)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _idItem IS NULL OR _sala IS NULL OR _inventario IS NULL OR _status IS NULL OR _NOME IS NULL THEN
                    RAISE EXCEPTION 'Todos os campos devem ser preenchidos para atualizar um alimento.';
                END IF;

                UPDATE Alimento SET sala = _sala, inventario = _inventario, status = _status, nome = _nome WHERE idItem = _idItem;
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE deletarAlimento(_idItem INT)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _idItem IS NULL THEN
                    RAISE EXCEPTION 'O ID do alimento é necessário para deleção.';
                END IF;

                DELETE FROM Alimento WHERE idItem = _idItem;
                CALL deletarItem(_idItem);
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE atualizarArma(_idItem INT, _tipo_arma VARCHAR)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _idItem IS NULL OR _tipo_arma IS NULL THEN
                    RAISE EXCEPTION 'O ID da arma e o tipo da arma são necessários para atualização.';
                END IF;

                UPDATE Arma SET tipo_arma = _tipo_arma WHERE idItem = _idItem;
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE deletarArma(_idItem INT)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _idItem IS NULL THEN
                    RAISE EXCEPTION 'O ID da arma é necessário para deleção.';
                END IF;

                DELETE FROM Arma WHERE idItem = _idItem;
                CALL deletarItem(_idItem);
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE atualizarBranca(_idItem INT, _sala INT, _inventario INT, _nome VARCHAR, _dano INT, _material VARCHAR)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _idItem IS NULL OR _nome IS NULL OR _dano IS NULL OR _material IS NULL THEN
                    RAISE EXCEPTION 'Todos os campos devem ser preenchidos para atualizar uma arma branca.';
                END IF;

                UPDATE Branca SET sala = _sala, inventario = _inventario, nome = _nome, dano = _dano, material = _material WHERE idItem = _idItem;
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE deletarBranca(_idItem INT)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _idItem IS NULL THEN
                    RAISE EXCEPTION 'O ID da arma branca é necessário para deleção.';
                END IF;

                DELETE FROM Branca WHERE idItem = _idItem;
                CALL deletarArma(_idItem);
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE atualizarFogo(_idItem INT, _sala INT, _inventario INT, _nome VARCHAR, _dano INT, _distancia INT, _capacidadeMunicao INT)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _idItem IS NULL OR _inventario IS NULL OR _nome IS NULL OR _dano IS NULL OR _distancia IS NULL OR _capacidadeMunicao IS NULL THEN
                    RAISE EXCEPTION 'Todos os campos devem ser preenchidos para atualizar uma arma de fogo.';
                END IF;

                UPDATE Fogo SET sala = _sala, inventario = _inventario, nome = _nome, dano = _dano, distancia = _distancia, capacidadeMunicao = _capacidadeMunicao WHERE idItem = _idItem;
            END $$;
            """,
            """
            CREATE OR REPLACE PROCEDURE deletarFogo(_idItem INT)
            LANGUAGE plpgsql AS $$
            BEGIN
                IF _idItem IS NULL THEN
                    RAISE EXCEPTION 'O ID da arma de fogo é necessário para deleção.';
                END IF;
                
                DELETE FROM Fogo WHERE idItem = _idItem;
                CALL deletarArma(_idItem);
            END $$;
            """,
            """
            CREATE OR REPLACE FUNCTION atualizarQuantidadeItens()
            RETURNS TRIGGER AS $$
            DECLARE
                _nova_quantidade INT;
            BEGIN
                IF TG_OP = 'INSERT' THEN
                    UPDATE Inventario
                    SET quantidadeItens = quantidadeItens + 1
                    WHERE personagem = NEW.inventario
                    RETURNING quantidadeItens INTO _nova_quantidade;
                ELSIF TG_OP = 'DELETE' THEN
                    UPDATE Inventario
                    SET quantidadeItens = quantidadeItens - 1
                    WHERE personagem = OLD.inventario
                    RETURNING quantidadeItens INTO _nova_quantidade;
                END IF;
                IF _nova_quantidade >= (SELECT maxItens FROM Inventario WHERE personagem = NEW.inventario) THEN
                    RAISE EXCEPTION 'A quantidade de itens excede o limite máximo no inventário.';
                END IF;
                RETURN NULL;
            END;
            $$ LANGUAGE plpgsql;
            """,
            """
            CREATE TRIGGER atualizar_quantidade_itens_alimento
            AFTER INSERT OR DELETE ON Alimento
            FOR EACH ROW EXECUTE FUNCTION atualizarQuantidadeItens();
            """,
            """
            CREATE TRIGGER atualizar_quantidade_itens_ferramenta
            AFTER INSERT OR DELETE ON Ferramenta
            FOR EACH ROW EXECUTE FUNCTION atualizarQuantidadeItens();
            CREATE TRIGGER atualizar_quantidade_itens_branca
            AFTER INSERT OR DELETE ON Branca
            FOR EACH ROW EXECUTE FUNCTION atualizarQuantidadeItens();
            """,
            """
            CREATE TRIGGER atualizar_quantidade_itens_fogo
            AFTER INSERT OR DELETE ON Fogo
            FOR EACH ROW EXECUTE FUNCTION atualizarQuantidadeItens();
            """
        ]

        for command in sql_commands:
            cursor.execute(command)

        conn.commit()



    def create_tables(conn, cursor):
        sql_commands = [
            """
            CREATE TABLE Mapa (
                idMapa SERIAL PRIMARY KEY,
                dimensao INT NOT NULL,
                nomeMapa VARCHAR(255) NOT NULL,
                descricao VARCHAR(1000) NOT NULL
            )
            """,
            """
            CREATE TABLE Cidade (
                nome VARCHAR(255) PRIMARY KEY NOT NULL,
                mapa INT NOT NULL,
                nroConstrucoes INT NOT NULL DEFAULT 0,
                CONSTRAINT fk_cidade_mapa FOREIGN KEY (mapa) REFERENCES Mapa(idMapa)
            )
            """,
            """
            CREATE TABLE Sala (
                idSala SERIAL PRIMARY KEY,
                nome VARCHAR(255),
                cidade VARCHAR(255),
                descricao VARCHAR(1000) NOT NULL,
                CONSTRAINT fk_sala_cidade FOREIGN KEY (cidade) REFERENCES Cidade(nome)
            )
            """,
            """
            CREATE TABLE Veiculo (
                idVeiculo SERIAL PRIMARY KEY,
                tipo VARCHAR(255) NOT NULL,
                CONSTRAINT veiculo_tipo_check CHECK (tipo IN ('Aereo', 'Aquatico', 'Terrestre'))
            )
            """,
            """
            CREATE TABLE Terrestre (
                idVeiculo SERIAL PRIMARY KEY,
                sala INT NOT NULL,
                nome VARCHAR(255) NOT NULL DEFAULT 'Carro',
                vida INT NOT NULL DEFAULT 100,
                numRodas SMALLINT NOT NULL DEFAULT 4,
                combustivel INT NOT NULL DEFAULT 100,
                CONSTRAINT fk_terrestre_veiculo FOREIGN KEY (idVeiculo) REFERENCES Veiculo(idVeiculo),
                CONSTRAINT fk_terrestre_sala FOREIGN KEY (sala) REFERENCES Sala(idSala),
                CHECK (vida > 0)
            )
            """,
            """
            CREATE TABLE Aquatico (
                idVeiculo SERIAL PRIMARY KEY,
                sala INT NOT NULL,
                nome VARCHAR(255) NOT NULL DEFAULT 'Barco',
                vida INT NOT NULL DEFAULT 100,
                combustivel INT NOT NULL DEFAULT 100,
                propulsao INT NOT NULL DEFAULT 30,
                CONSTRAINT fk_aquatico_veiculo FOREIGN KEY (idVeiculo) REFERENCES Veiculo(idVeiculo),
                CONSTRAINT fk_aquatico_sala FOREIGN KEY (sala) REFERENCES Sala(idSala),
                CHECK (vida > 0)
            )
            """,
            """
            CREATE TABLE Aereo (
                idVeiculo SERIAL PRIMARY KEY,
                sala INT NOT NULL,
                nome VARCHAR(255) NOT NULL DEFAULT 'Aviao',
                vida INT NOT NULL DEFAULT 100,
                combustivel INT NOT NULL DEFAULT 100,
                maxAltitude INT NOT NULL DEFAULT 250,
                CONSTRAINT fk_aereo_veiculo FOREIGN KEY (idVeiculo) REFERENCES Veiculo(idVeiculo),
                CONSTRAINT fk_aereo_sala FOREIGN KEY (sala) REFERENCES Sala(idSala),
                CHECK (vida > 0)
            )
            """,
            """
            CREATE TABLE Personagem (
                idPersonagem SERIAL PRIMARY KEY,
                tipo VARCHAR(255) NOT NULL,
                CONSTRAINT personagem_tipo_check CHECK (tipo IN ('NPC', 'PC'))
            )
            """,
            """
            CREATE TABLE PC (
                idPersonagem SERIAL PRIMARY KEY,
                sala INT,
                nome VARCHAR(255) DEFAULT 'Steve',
                vida INT NOT NULL DEFAULT 100,
                stamina INT NOT NULL DEFAULT 100,
                CONSTRAINT fk_pc_personagem FOREIGN KEY (idPersonagem) REFERENCES Personagem(idPersonagem),
                CONSTRAINT fk_pc_sala FOREIGN KEY (sala) REFERENCES Sala(idSala)
            )
            """,
            """
            CREATE TABLE NPC (
                idPersonagem SERIAL PRIMARY KEY,
                tipo_npc VARCHAR(255) NOT NULL DEFAULT 'Zumbi',
                CONSTRAINT fk_npc_personagem FOREIGN KEY (idPersonagem) REFERENCES Personagem(idPersonagem),
                CONSTRAINT NPC_tipo_check CHECK (tipo_npc IN ('Zumbi', 'Animal'))
            )
            """,
            """
            CREATE TABLE Zumbi (
                idPersonagem SERIAL PRIMARY KEY,
                vida INT NOT NULL DEFAULT 100,
                classe VARCHAR(255) NOT NULL DEFAULT 'Andarilho',
                dano INT NOT NULL DEFAULT 80,
                CONSTRAINT fk_zumbi_personagem FOREIGN KEY (idPersonagem) REFERENCES Personagem(idPersonagem),
                CONSTRAINT Zumbi_classe_check CHECK (classe IN ('Corredor', 'Andarilho', 'Rastejante'))
            )
            """,
            """
            CREATE TABLE Animal (
                idPersonagem SERIAL PRIMARY KEY,
                vida INT NOT NULL DEFAULT 100,
                especie VARCHAR(255) NOT NULL DEFAULT 'Boi',
                CONSTRAINT fk_animal_personagem FOREIGN KEY (idPersonagem) REFERENCES Personagem(idPersonagem)
            )
            """,
            """
            CREATE TABLE Instancia (
                idInstancia SERIAL PRIMARY KEY,
                NPC INT NOT NULL,
                sala INT NOT NULL,
                CONSTRAINT fk_instancia_npc FOREIGN KEY (NPC) REFERENCES NPC(idPersonagem),
                CONSTRAINT fk_instancia_sala FOREIGN KEY (sala) REFERENCES Sala(idSala)
            )
            """,
            """
            CREATE TABLE Missao (
                idMissao SERIAL PRIMARY KEY,
                idPersonagem INT NOT NULL,
                Descricao VARCHAR(255),
                Recompensa VARCHAR(255),
                Estado VARCHAR(255),
                CONSTRAINT check_estado_missao CHECK (Estado IN ('Doing', 'Done')),
                CONSTRAINT fk_personagem_missao FOREIGN KEY (idPersonagem) REFERENCES PC(idPersonagem)
            )
            """,
            """
            CREATE TABLE Criador (
                idCriador SERIAL PRIMARY KEY,
                idPersonagem INT NOT NULL,
                nome VARCHAR(255),
                CONSTRAINT fk_criador_personagem FOREIGN KEY (idPersonagem) REFERENCES PC(idPersonagem)
            )
            """,
            """
            CREATE TABLE Item (
                idItem SERIAL PRIMARY KEY,
                tipo VARCHAR(255) DEFAULT 'Alimento',
                CONSTRAINT item_tipo_check CHECK (tipo IN ('Ferramenta', 'Alimento', 'Arma'))
            )
            """,
            """
            CREATE TABLE Receita (
                idReceita SERIAL PRIMARY KEY,
                idCriador INT NOT NULL,
                idItem INT NOT NULL,
                Resultado VARCHAR(255),
                Requisitos VARCHAR(255),
                TempoCriacao INT NOT NULL,
                CONSTRAINT fk_criador_receita FOREIGN KEY (idCriador) REFERENCES Criador(idCriador),
                CONSTRAINT fk_item_receita FOREIGN KEY (idItem) REFERENCES Item(idItem)
            )
            """,
            """
            CREATE TABLE Inventario (
                personagem INT PRIMARY KEY,
                quantidadeItens INT DEFAULT 0,
                maxItens INT DEFAULT 20,
                CONSTRAINT fk_inventario_personagem FOREIGN KEY (personagem) REFERENCES Personagem(idPersonagem),
                CONSTRAINT inventario_quantidadeItem_check CHECK (quantidadeItens <= maxItens)
            )
            """,
            """
            CREATE TABLE Ferramenta (
                idItem INT PRIMARY KEY,
                sala INT,
                inventario INT,
                durabilidade INT DEFAULT 100,
                nome VARCHAR(255) NOT NULL,
                CONSTRAINT fk_ferramenta_item FOREIGN KEY (idItem) REFERENCES Item(idItem),
                CONSTRAINT fk_ferramenta_inventario FOREIGN KEY (inventario) REFERENCES Inventario(personagem),
                CONSTRAINT fk_ferramenta_sala FOREIGN KEY (sala) REFERENCES Sala(idSala)
            )
            """,
            """
            CREATE TABLE Alimento (
                idItem INT PRIMARY KEY,
                sala INT,
                inventario INT,
                status VARCHAR(255) DEFAULT 'Excelente',
                nome VARCHAR(255) NOT NULL,
                CONSTRAINT fk_alimento_item FOREIGN KEY (idItem) REFERENCES Item(idItem),
                CONSTRAINT fk_alimento_inventario FOREIGN KEY (inventario) REFERENCES Inventario(personagem),
                CONSTRAINT fk_alimento_sala FOREIGN KEY (sala) REFERENCES Sala(idSala),
                CONSTRAINT alimento_status_check CHECK (status IN ('Excelente', 'Bom', 'Mediano', 'Ruim', 'Pessimo'))
            )
            """,
            """
            CREATE TABLE Arma (
                idItem INT PRIMARY KEY,
                tipo_arma VARCHAR(255),
                CONSTRAINT fk_arma_item FOREIGN KEY (idItem) REFERENCES Item(idItem),
                CONSTRAINT arma_tipo_check CHECK (tipo_arma IN ('Fogo', 'Branca'))
            )
            """,
            """
            CREATE TABLE Fogo (
                idItem INT PRIMARY KEY,
                sala INT,
                inventario INT,
                nome VARCHAR(255),
                dano INT,
                distancia INT DEFAULT 10,
                capacidadeMunicao INT DEFAULT 15,
                CONSTRAINT fk_fogo_arma FOREIGN KEY (idItem) REFERENCES Arma(idItem),
                CONSTRAINT fk_fogo_inventario FOREIGN KEY (inventario) REFERENCES Inventario(personagem),
                CONSTRAINT fk_fogo_sala FOREIGN KEY (sala) REFERENCES Sala(idSala)
            )
            """,
            """
            CREATE TABLE Branca (
                idItem INT PRIMARY KEY,
                sala INT,
                inventario INT,
                nome VARCHAR(255) DEFAULT 'Faca',
                dano INT,
                material VARCHAR(255) DEFAULT 'Madeira',
                CONSTRAINT fk_branca_arma FOREIGN KEY (idItem) REFERENCES Arma(idItem),
                CONSTRAINT fk_branca_inventario FOREIGN KEY (inventario) REFERENCES Inventario(personagem),
                CONSTRAINT fk_branca_sala FOREIGN KEY (sala) REFERENCES Sala(idSala)
            )
            """
        ]

        for command in sql_commands:
            cursor.execute(command)

        conn.commit()

    def create_adventure(conn, cursor):
        idMapa = DataBase.inserir_mapa(conn, cursor)

        DataBase.inserir_cidade(conn, cursor, "Moscow", idMapa)

        # Cidade Arruinada
        descricao_sala= """
            Você avança pela cidade arruinada de Moscow e de repente se depara com um zumbi faminto.
            O zumbi se aproxima lentamente, gemendo e com olhos vazios fixos em você.
        """

        DataBase.inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="cidade_arruinada", descricao_sala=descricao_sala)

        # Casa Abandonada
        descricao_sala= """
            Você entra na casa abandonada.
        """

        DataBase.inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="casa_abandonada", descricao_sala=descricao_sala)

        # Rua Deserta
        descricao_sala= """
            Você pega os itens e decide avançar para fora da casa.
            Ao chegar na rua, você se depara com três zumbis bloqueando o caminho.
        """

        DataBase.inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="rua_deserta", descricao_sala=descricao_sala)

        # Igreja
        descricao_sala= """
            Você corre para dentro da igreja, conseguindo dividir os zumbis.
            Apenas um zumbi continua seguindo você para dentro da igreja.
        """

        DataBase.inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="igreja", descricao_sala=descricao_sala)

        # Igreja
        descricao_sala= """
            Você encontra uma pistola na igreja.
        """

        DataBase.inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="igreja_armado", descricao_sala=descricao_sala)

        # Celeiro
        descricao_sala= """
            Você avança em direção ao celeiro e percebe que há um carro estacionado lá dentro.
        """

        DataBase.inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="fazenda_celeiro", descricao_sala=descricao_sala)

        # Dentro do ceileiro
        descricao_sala= """
            Você entra no celeiro e encontra um carro em boas condições.
            Ao se aproximar do carro, você ouve um som estranho vindo de dentro do celeiro.
            Curioso, você decide investigar e descobre um zumbi gigante chorando no interior do celeiro.
        """

        DataBase.inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="pegar_carro", descricao_sala=descricao_sala)

        # Tentar ignorar o zumbi
        descricao_sala= """
            Você entra no carro e tenta ignorar o zumbi gigante chorando no celeiro.
            O som é perturbador, mas ao tentar dar partida, você percebe que o carro está sem gasolina.
            O zumbi gigante, ao ouvir o barulho do carro, se levanta e o segue.
            Ele alcança você, puxa-o para fora do carro e joga-o para fora do celeiro.
        """

        DataBase.inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="tentar_ignorar_zumbi", descricao_sala=descricao_sala)

        # Fugir para milharal
        descricao_sala= """
            Você se vê fora do celeiro e decide correr para o milharal nas proximidades, tentando despistar o zumbi gigante.
            Você se embrenha entre as fileiras de milho, tentando manter-se fora do alcance do zumbi.
            No milharal, um zumbi rastejante surge e agarra sua perna, fazendo você cair.
            O zumbi chorador de antes continua a perseguição, se aproximando rapidamente.
        """

        DataBase.inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="fugir_para_milharal", descricao_sala=descricao_sala)

        # Fugir para milharal
        descricao_sala= """
            Você atira no zumbi rastejante, neutralizando a ameaça temporariamente.
        """

        DataBase.inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="atirar_zumbi_rastejante", descricao_sala=descricao_sala)

        # Continuar fugindo milharal
        descricao_sala= """
            Você se levanta rapidamente e continua a correr pelo milharal, tentando despistar o zumbi chorador.
            Ao sair do milharal, você se encontra à beira de um rio. Do lado oposto, avista um barco a motor.
        """

        DataBase.inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="continuar_fugindo_milharal", descricao_sala=descricao_sala)

        # Nadar rio
        descricao_sala= """
            Você pula no rio e começa a nadar vigorosamente até o outro lado.
            Ao alcançar a margem oposta, você se afasta do rio, olhando para trás para verificar se o zumbi chorador te seguiu.
        """

        DataBase.inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="nadar_rio", descricao_sala=descricao_sala)

        # Correr ate barco
        descricao_sala= """
            Você corre em direção ao barco a motor, esperando alcançá-lo antes que o zumbi chorador chegue até você.
            Ao chegar ao barco, você se depara com uma cena angustiante: uma família dilacerada pelos zumbis.
            Você também encontra uma mala próxima ao barco com, uma metralhadora, 2 bandagens e um molotov.
        """

        DataBase.inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="corre_ate_barco", descricao_sala=descricao_sala)

        # Correr ligar barco zumbi caido
        descricao_sala= """
            Você tenta correr até o barco para ligá-lo, mas o zumbi chorador está muito próximo.
            Mas com ele quase o alcançando-o, você consegue dar partida, saindo dali rapidamente.
            Agora você o deixa em um horizonte distante enquanto escapa
        """

        DataBase.inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="correr_ligar_barco_zumbi_caido", descricao_sala=descricao_sala)

        # Correr ligar barco
        descricao_sala= """
            Você tenta correr até o barco para ligá-lo, mas o zumbi chorador está muito próximo.
            Antes que você alcance o barco, o zumbi agarra você, impedindo sua fuga.
        """

        DataBase.inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="correr_ligar_barco", descricao_sala=descricao_sala)

        # Pegar carro com gasolina
        descricao_sala= """
            Você volta ao celeiro com o carro em boas condições.
            Fazendo o mínimo de barulho possível, você coloca a gasolina no tanque.
            Você entra no carro de fininho e dar partida, mas a partida chama a atenção do zumbi chorador no ceileiro
            Entretando, você acelera no desespero o deixando para traz e saindo daquela situação
        """

        DataBase.inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="pegar_carro_com_gasolina", descricao_sala=descricao_sala)
    
        DataBase.inserir_arma_branca(conn, id=1, sala=1, nome="faca", dano=15, material="ferro")
        DataBase.inserir_ferramenta(conn, id=2, sala=1, durabilidade=10, nome="corda")
        DataBase.inserir_ferramenta(conn, id=3, sala=1, durabilidade=5, nome="isqueiro")
        DataBase.inserir_arma_fogo(conn, id=4, sala=4, nome="pistola", dano=45, distancia=10, capacidadeMunicao=8)
        DataBase.inserir_alimento(conn, id = 5, sala = 1, status = 'Bom', nome = 'Jaca')
        DataBase.create_new_zumbi(conn, id = 2, vida = 100, classe = 'Andarilho', dano = 30)
        DataBase.create_new_zumbi(conn, id = 3, vida = 100, classe = 'Corredor', dano = 15)
        DataBase.insert_instancia(conn, idInstancia = 1, NPC = 3, sala = 1)
        DataBase.insert_instancia(conn, idInstancia = 2, NPC = 2, sala = 2)
        DataBase.insert_veiculo_aereo(conn, id = 1, sala = 1, nome = 'A380', vida = 100, combustivel = 70, maxAltitude = 10000)
        DataBase.insert_veiculo_terrestre(conn, id = 2, sala = 2, nome = 'Brasília amarela', vida = 100, combustivel = 60, numRodas = 4)
        
        