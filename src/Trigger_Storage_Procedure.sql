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
