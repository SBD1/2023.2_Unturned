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
        END IF;
        PERFORM * FROM Terrestre WHERE _id = Terrestre.idVeiculo;
        IF FOUND THEN
            DELETE FROM Terrestre WHERE _id = Terrestre.idVeiculo;
            INSERT INTO Aereo VALUES (_id, _sala, _nome, _vida, _combustivel, _maxAltitude);
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
        END IF;
        PERFORM * FROM Aereo WHERE _id = Aereo.idVeiculo;
        IF FOUND THEN
            DELETE FROM Aereo WHERE _id = Aereo.idVeiculo;
            INSERT INTO Terrestre VALUES (_id, _sala, _nome, _vida, _numRodas, _combustivel);
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
        END IF;
        PERFORM * FROM Aereo WHERE _id = Aereo.idVeiculo;
        IF FOUND THEN
            DELETE FROM Aereo WHERE _id = Aereo.idVeiculo;
            INSERT INTO Aquatico VALUES (_id, _sala, _nome, _vida, _combustivel, _propulsao);
        END IF;
        PERFORM * FROM Aquatico WHERE _id = Aquatico.idVeiculo;
        IF FOUND THEN
            UPDATE Aquatico SET sala = _sala, nome = _nome, vida = _vida, combustivel = _combustivel, propulsao = _propulsao WHERE idVeiculo = _id;
        ELSE 
            RAISE EXCEPTION 'O id colocado não está na tabela Aquatico';
        END IF;
    END IF;
END $$;


