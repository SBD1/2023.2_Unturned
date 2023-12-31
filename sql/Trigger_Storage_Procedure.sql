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

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

-------------------------------------------------------------------------------------------------------------
 
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

------------------------------------------------------------------------------------------------

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

CREATE TRIGGER ferramentas
BEFORE INSERT OR UPDATE ON Ferramenta
FOR EACH ROW EXECUTE PROCEDURE verifica_ferramentas();


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

CREATE TRIGGER alimentos
BEFORE INSERT OR UPDATE ON Alimento
FOR EACH ROW EXECUTE PROCEDURE verifica_alimentos();


-- CREATE OR REPLACE FUNCTION verifica_alimentos() RETURNS TRIGGER AS $verifica_alimentos$

-- BEGIN

-- 	PERFORM * FROM Ferramenta WHERE Ferramenta.idItem = New.idItem;
-- 	IF FOUND THEN
-- 		RAISE EXCEPTION 'ERRO: Já existe uma Ferramenta com esse ID';
-- 	END IF;

--     PERFORM * FROM Arma WHERE Arma.idItem = New.idItem;
-- 	IF FOUND THEN
-- 		RAISE EXCEPTION 'ERRO: Já existe uma Arma com esse ID';
-- 	END IF;

-- 	RETURN NEW;
-- END;
-- $verifica_alimentos$ LANGUAGE plpgsql;

-- CREATE TRIGGER alimentos
-- BEFORE INSERT OR UPDATE ON Alimento
-- FOR EACH ROW EXECUTE PROCEDURE verifica_alimentos();


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

CREATE TRIGGER armas
BEFORE INSERT OR UPDATE ON Arma
FOR EACH ROW EXECUTE PROCEDURE verifica_armas();


CREATE OR REPLACE FUNCTION verifica_fogos() RETURNS TRIGGER AS $verifica_fogos$

BEGIN

	PERFORM * FROM Branca WHERE Branca.idItem = New.idItem;
	IF FOUND THEN
		RAISE EXCEPTION 'ERRO: Já existe uma arma Branca com esse ID';
	END IF;

	RETURN NEW;
END;
$verifica_fogos$ LANGUAGE plpgsql;

CREATE TRIGGER fogos
BEFORE INSERT OR UPDATE ON Fogo
FOR EACH ROW EXECUTE PROCEDURE verifica_fogos();


CREATE OR REPLACE FUNCTION verifica_brancas() RETURNS TRIGGER AS $verifica_brancas$

BEGIN

	PERFORM * FROM Fogo WHERE Fogo.idItem = New.idItem;
	IF FOUND THEN
		RAISE EXCEPTION 'ERRO: Já existe uma arma de Fogo com esse ID';
	END IF;

	RETURN NEW;
END;
$verifica_brancas$ LANGUAGE plpgsql;

CREATE TRIGGER brancas
BEFORE INSERT OR UPDATE ON Branca
FOR EACH ROW EXECUTE PROCEDURE verifica_brancas();

-------------------------------------------------------------------------------------------------------------

-- Procedimento para inserir um novo 'Item'
CREATE OR REPLACE PROCEDURE inserirItem(_idItem INT, _tipo VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF _idItem IS NULL THEN
        RAISE EXCEPTION 'O ID do item é necessário para a criação.';
    END IF;
    IF _tipo IS NULL THEN
        RAISE EXCEPTION 'O tipo do item é necessário para a criação.';
    END IF;

    -- Verifica se o tipo do item é um dos três tipos permitidos
    IF _tipo NOT IN ('Ferramenta', 'Alimento', 'Arma') THEN
        RAISE EXCEPTION 'O tipo do item deve ser Ferramenta, Alimento ou Arma.';
    END IF;

    INSERT INTO Item(idItem, tipo)
    VALUES (_idItem, _tipo);
END $$;

-- Procedimento para inserir uma nova 'Ferramenta'
CREATE OR REPLACE PROCEDURE inserirFerramenta(_idItem INT, _sala INT, _inventario INT, _durabilidade INT, _nome VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF _idItem IS NULL OR _sala IS NULL OR _inventario IS NULL OR _durabilidade IS NULL THEN
        RAISE EXCEPTION 'Todos os campos devem ser preenchidos para inserir uma ferramenta.';
    END IF;

    CALL inserirItem(_idItem, 'Ferramenta');
    INSERT INTO Ferramenta(idItem, sala, inventario, durabilidade, nome)
    VALUES (_idItem, _sala, _inventario, _durabilidade, _nome);
END $$;

-- Procedimento para inserir um novo 'Alimento'
CREATE OR REPLACE PROCEDURE inserirAlimento(_idItem INT, _sala INT, _inventario INT, _status VARCHAR, _nome VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF _idItem IS NULL OR _sala IS NULL OR _inventario IS NULL OR _status IS NULL THEN
        RAISE EXCEPTION 'Todos os campos devem ser preenchidos para inserir um alimento.';
    END IF;

    CALL inserirItem(_idItem, 'Alimento');
    INSERT INTO Alimento(idItem, sala, inventario, status, nome)
    VALUES (_idItem, _sala, _inventario, _status, _nome);
END $$;

-- Procedimento para inserir uma nova 'Arma'
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

-- Procedimento para inserir uma nova 'Arma Branca'
CREATE OR REPLACE PROCEDURE inserirBranca(_idItem INT, _sala INT, _inventario INT, _nome VARCHAR, _dano INT, _material VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF _idItem IS NULL OR _sala IS NULL OR _inventario IS NULL OR _nome IS NULL OR _dano IS NULL OR _material IS NULL THEN
        RAISE EXCEPTION 'Todos os campos devem ser preenchidos para inserir uma arma branca.';
    END IF;

    CALL inserirArma(_idItem, 'Branca');
    INSERT INTO Branca(idItem, sala, inventario, nome, dano, material)
    VALUES (_idItem, _sala, _inventario, _nome, _dano, _material);
END $$;

-- Procedimento para inserir uma nova 'Arma de Fogo'
CREATE OR REPLACE PROCEDURE inserirFogo(_idItem INT, _sala INT, _inventario INT, _nome VARCHAR, _dano INT, _distancia INT, _capacidadeMunicao INT)
LANGUAGE plpgsql AS $$
BEGIN
    IF _idItem IS NULL OR _sala IS NULL OR _inventario IS NULL OR _nome IS NULL OR _dano IS NULL OR _distancia IS NULL OR _capacidadeMunicao IS NULL THEN
        RAISE EXCEPTION 'Todos os campos devem ser preenchidos para inserir uma arma de fogo.';
    END IF;
    
    CALL inserirArma(_idItem, 'Fogo');
    INSERT INTO Fogo(idItem, sala, inventario, nome, dano, distancia, capacidadeMunicao)
    VALUES (_idItem, _sala, _inventario, _nome, _dano, _distancia, _capacidadeMunicao);
END $$;

-- Procedimento para atualizar um 'Item'
CREATE OR REPLACE PROCEDURE atualizarItem(_idItem INT, _tipo VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF _idItem IS NULL OR _tipo IS NULL THEN
        RAISE EXCEPTION 'O ID do item e o tipo são necessários para atualização.';
    END IF;
    UPDATE Item SET tipo = _tipo WHERE idItem = _idItem;
END $$;

-- Procedimento para deletar um 'Item'
CREATE OR REPLACE PROCEDURE deletarItem(_idItem INT)
LANGUAGE plpgsql AS $$
BEGIN
    IF _idItem IS NULL THEN
        RAISE EXCEPTION 'O ID do item é necessário para deleção.';
    END IF;
    DELETE FROM Item WHERE idItem = _idItem;
END $$;

-- Procedimento para atualizar uma 'Ferramenta'
CREATE OR REPLACE PROCEDURE atualizarFerramenta(_idItem INT, _sala INT, _inventario INT, _durabilidade INT, _nome VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF _idItem IS NULL OR _sala IS NULL OR _inventario IS NULL OR _durabilidade IS NULL THEN
        RAISE EXCEPTION 'Todos os campos devem ser preenchidos para atualizar uma ferramenta.';
    END IF;

    UPDATE Ferramenta SET sala = _sala, inventario = _inventario, durabilidade = _durabilidade, nome = _nome WHERE idItem = _idItem;
END $$;

-- Procedimento para deletar uma 'Ferramenta'
CREATE OR REPLACE PROCEDURE deletarFerramenta(_idItem INT)
LANGUAGE plpgsql AS $$
BEGIN
    IF _idItem IS NULL THEN
        RAISE EXCEPTION 'O ID da ferramenta é necessário para deleção.';
    END IF;

    DELETE FROM Ferramenta WHERE idItem = _idItem;
    CALL deletarItem(_idItem);
END $$;

-- Procedimento para atualizar um 'Alimento'
CREATE OR REPLACE PROCEDURE atualizarAlimento(_idItem INT, _sala INT, _inventario INT, _status VARCHAR, _nome VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF _idItem IS NULL OR _sala IS NULL OR _inventario IS NULL OR _status IS NULL OR _NOME IS NULL THEN
        RAISE EXCEPTION 'Todos os campos devem ser preenchidos para atualizar um alimento.';
    END IF;

    UPDATE Alimento SET sala = _sala, inventario = _inventario, status = _status, nome = _nome WHERE idItem = _idItem;
END $$;

-- Procedimento para deletar um 'Alimento'
CREATE OR REPLACE PROCEDURE deletarAlimento(_idItem INT)
LANGUAGE plpgsql AS $$
BEGIN
    IF _idItem IS NULL THEN
        RAISE EXCEPTION 'O ID do alimento é necessário para deleção.';
    END IF;

    DELETE FROM Alimento WHERE idItem = _idItem;
    CALL deletarItem(_idItem);
END $$;

-- Procedimento para atualizar uma 'Arma'
CREATE OR REPLACE PROCEDURE atualizarArma(_idItem INT, _tipo_arma VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF _idItem IS NULL OR _tipo_arma IS NULL THEN
        RAISE EXCEPTION 'O ID da arma e o tipo da arma são necessários para atualização.';
    END IF;

    UPDATE Arma SET tipo_arma = _tipo_arma WHERE idItem = _idItem;
END $$;

-- Procedimento para deletar uma 'Arma'
CREATE OR REPLACE PROCEDURE deletarArma(_idItem INT)
LANGUAGE plpgsql AS $$
BEGIN
    IF _idItem IS NULL THEN
        RAISE EXCEPTION 'O ID da arma é necessário para deleção.';
    END IF;

    DELETE FROM Arma WHERE idItem = _idItem;
    CALL deletarItem(_idItem);
END $$;

-- Procedimento para atualizar uma 'Arma Branca'
CREATE OR REPLACE PROCEDURE atualizarBranca(_idItem INT, _sala INT, _inventario INT, _nome VARCHAR, _dano INT, _material VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF _idItem IS NULL OR _sala IS NULL OR _inventario IS NULL OR _nome IS NULL OR _dano IS NULL OR _material IS NULL THEN
        RAISE EXCEPTION 'Todos os campos devem ser preenchidos para atualizar uma arma branca.';
    END IF;

    UPDATE Branca SET sala = _sala, inventario = _inventario, nome = _nome, dano = _dano, material = _material WHERE idItem = _idItem;
END $$;

-- Procedimento para deletar uma 'Arma Branca'
CREATE OR REPLACE PROCEDURE deletarBranca(_idItem INT)
LANGUAGE plpgsql AS $$
BEGIN
    IF _idItem IS NULL THEN
        RAISE EXCEPTION 'O ID da arma branca é necessário para deleção.';
    END IF;

    DELETE FROM Branca WHERE idItem = _idItem;
    CALL deletarArma(_idItem);
END $$;

-- Procedimento para atualizar uma 'Arma de Fogo'
CREATE OR REPLACE PROCEDURE atualizarFogo(_idItem INT, _sala INT, _inventario INT, _nome VARCHAR, _dano INT, _distancia INT, _capacidadeMunicao INT)
LANGUAGE plpgsql AS $$
BEGIN
    IF _idItem IS NULL OR _sala IS NULL OR _inventario IS NULL OR _nome IS NULL OR _dano IS NULL OR _distancia IS NULL OR _capacidadeMunicao IS NULL THEN
        RAISE EXCEPTION 'Todos os campos devem ser preenchidos para atualizar uma arma de fogo.';
    END IF;

    UPDATE Fogo SET sala = _sala, inventario = _inventario, nome = _nome, dano = _dano, distancia = _distancia, capacidadeMunicao = _capacidadeMunicao WHERE idItem = _idItem;
END $$;

-- Procedimento para deletar uma 'Arma de Fogo'
CREATE OR REPLACE PROCEDURE deletarFogo(_idItem INT)
LANGUAGE plpgsql AS $$
BEGIN
    IF _idItem IS NULL THEN
        RAISE EXCEPTION 'O ID da arma de fogo é necessário para deleção.';
    END IF;
    
    DELETE FROM Fogo WHERE idItem = _idItem;
    CALL deletarArma(_idItem);
END $$;

------------------------------------------------------------------------------------------------

-- Trigger para adicionar ou subtrair da quantidadeItens do inventario
CREATE OR REPLACE FUNCTION atualizarQuantidadeItens()
RETURNS TRIGGER AS $$
DECLARE
    _nova_quantidade INT;
BEGIN
    -- Adiciona 1 à quantidadeItens do inventario após a inserção
    IF TG_OP = 'INSERT' THEN
        UPDATE Inventario
        SET quantidadeItens = quantidadeItens + 1
        WHERE personagem = NEW.inventario
        RETURNING quantidadeItens INTO _nova_quantidade;
    -- Subtrai 1 da quantidadeItens do inventario após a deleção
    ELSIF TG_OP = 'DELETE' THEN
        UPDATE Inventario
        SET quantidadeItens = quantidadeItens - 1
        WHERE personagem = OLD.inventario
        RETURNING quantidadeItens INTO _nova_quantidade;
    END IF;

    -- Verifica se maxItens é maior ou igual a quantidadeItens
    IF _nova_quantidade > (SELECT maxItens FROM Inventario WHERE personagem = NEW.inventario) THEN
        RAISE EXCEPTION 'A quantidade de itens excede o limite máximo no inventário.';
    END IF;

    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

-- Triggers para Alimento, Ferramenta, Branca, Fogo
CREATE TRIGGER atualizar_quantidade_itens_alimento
AFTER INSERT OR DELETE ON Alimento
FOR EACH ROW EXECUTE FUNCTION atualizarQuantidadeItens();

CREATE TRIGGER atualizar_quantidade_itens_ferramenta
AFTER INSERT OR DELETE ON Ferramenta
FOR EACH ROW EXECUTE FUNCTION atualizarQuantidadeItens();

CREATE TRIGGER atualizar_quantidade_itens_branca
AFTER INSERT OR DELETE ON Branca
FOR EACH ROW EXECUTE FUNCTION atualizarQuantidadeItens();

CREATE TRIGGER atualizar_quantidade_itens_fogo
AFTER INSERT OR DELETE ON Fogo
FOR EACH ROW EXECUTE FUNCTION atualizarQuantidadeItens();
