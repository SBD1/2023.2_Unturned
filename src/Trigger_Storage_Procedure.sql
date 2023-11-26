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
