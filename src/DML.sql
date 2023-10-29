-- Inserir dados na tabela Mapa
INSERT INTO Mapa (idMapa, dimensao, nomeMapa)
VALUES (1, 1, 'Washington'),
       (2, 2, 'PEI'),
       (3, 3, 'Yukon'),
       (4, 4, 'Russia'),
       (5, 5, 'EUA');


-- Inserir dados na tabela Cidade
INSERT INTO Cidade (nome, mapa, radioatividade)
VALUES ('Seattle', 1, 25),
       ('Charlottetown', 2, 10),
       ('Whitehorse', 3, 5),
       ('Formosa', 4, 100),
       ('Chicago', 5, 30);
 
-- Inserir dados na tabela Veículo
INSERT INTO Veiculo (idVeiculo, cidade, tipo)
VALUES (1, 'Seattle', 'Aereo'),
       (2, 'Charlottetown', 'Terrestre'),
       (3, 'Whitehorse', 'Aquatico'),
       (4, 'Formosa', 'Aquatico'),
       (5, 'Chicago', 'Terrestre');

-- Inserir os dados na tabela Terrestre
INSERT INTO Terrestre
    SELECT idVeiculo, cidade FROM Veiculo
        WHERE tipo = 'Terrestre';

UPDATE Terrestre SET nome = 'Moto', vida = 23, numRodas = 2, combustivel = 80
    WHERE idVeiculo = 2;

-- Inserir os dados na tabela Aquatico
INSERT INTO Aquatico
    SELECT idVeiculo, cidade FROM Veiculo
        WHERE tipo = 'Aquatico';

UPDATE Aquatico SET nome = 'SiriCascudo', vida = 80, combustivel = 70, propulsao = 30
    WHERE idVeiculo = 3;

-- Inserir os dados na tabela Aereo
INSERT INTO Aereo
    SELECT idVeiculo, cidade FROM Veiculo
        WHERE tipo = 'Aereo';

UPDATE Aereo SET nome = 'TucTuc', vida = 75, combustivel = 100, maxAltitude = 3000;

-- Inserir dados na tabela Personagem
INSERT INTO Personagem (idPersonagem, cidade, tipo)
VALUES (1, 'Seattle', 'NPC'),
       (2, 'Charlottetown', 'PC'),
       (3, 'Whitehorse', 'NPC'),
       (4, 'Formosa', 'PC'),
       (5, 'Chicago', 'NPC');

-- Inserir dados na tabela PC
INSERT INTO PC(idPersonagem)
    SELECT idPersonagem FROM Personagem
        WHERE tipo = 'PC';

UPDATE PC SET nome = 'Messi', vida = 75, stamina = 90
    WHERE idPersonagem = 2;
UPDATE PC SET nome = 'CristianoRonaldo', vida = 90, stamina = 100
    WHERE idPersonagem = 4;

-- Inserir dados na tabela NPC
INSERT INTO NPC(idPersonagem)
    SELECT idPersonagem FROM Personagem
        WHERE tipo = 'NPC';

UPDATE NPC SET vida = 90, genetica = 'Animal'
    WHERE idPersonagem = 1;

UPDATE NPC SET vida = 80, genetica = 'Zumbi'
    WHERE idPersonagem = 3;

UPDATE NPC SET vida = 77, genetica = 'Animal'
    WHERE idPersonagem = 5;

-- Inserir dados na tabela Zumbi
INSERT INTO Zumbi(idPersonagem)
    SELECT idPersonagem FROM NPC
        WHERE genetica = 'Zumbi';

UPDATE Zumbi SET vida = 90, classe = 'Corredor', dano = 100
    WHERE idPersonagem = 3;

INSERT INTO Animal(idPersonagem)
    SELECT idPersonagem FROM NPC
        WHERE genetica = 'Animal';

UPDATE Animal SET vida = 100, especie = 'Vaca'
    WHERE idPersonagem = 1;

UPDATE Animal SET vida = 100, especie = 'Camelo'
    WHERE idPersonagem = 5;

-- Inserir dados na tabela Instancia
INSERT INTO Instancia (idInstancia, NPC, cidade)
    VALUES (1, 1, 'Formosa'),
           (2, 1, 'Chicago'),
           (3, 1, 'Seattle'),
           (4, 1, 'Formosa'),
           (5, 3, 'Whitehorse'),
           (6, 3, 'Charlottetown'),
           (7, 3, 'Chicago'),
           (8, 3, 'Charlottetown');

-- Inserir dados na tabela Inventario
INSERT INTO Inventario (Personagem, quantidadeItens, maxItens)
    VALUES (1, 0, 10),
    (2, 3, 60),
    (3, 0, 20),
    (4, 3, 40),
    (5, 0, 8);

-- Inserir dados na tabela Item
INSERT INTO Item (idItem, cidade, personagem, tipo)
VALUES
    (1, 'Seattle', 2, 'Ferramenta'),
    (2, 'Formosa', 2, 'Alimento'),
    (3, 'Seattle', 4, 'Alimento'),
    (4, 'Formosa', 4, 'Alimento'),         
    (5, 'Formosa', 2, 'Arma'),
    (6, 'Formosa', 4, 'Arma');


-- Inserir dados na tabela Ferramenta
INSERT INTO Ferramenta(idItem)
    SELECT idItem FROM Item
        WHERE tipo = 'Ferramenta';

UPDATE Ferramenta SET durabilidade = 30
    WHERE idItem = 1;

-- Inserir dados na tabela Alimento
INSERT INTO Alimento(idItem)
    SELECT idItem FROM Item
        WHERE tipo = 'Alimento';

UPDATE Alimento SET status = 'Excelente'
    WHERE idItem = 2;

UPDATE Alimento SET status = 'Bom'
    WHERE idItem = 3;

UPDATE Alimento SET status = 'Pessimo'
    WHERE idItem = 4;

-- Inserir dados na tabela Arma
INSERT INTO Arma(idItem)
    SELECT idItem FROM Item
        WHERE tipo = 'Arma';

UPDATE Arma SET classe = 'Branca', dano = 100
    WHERE idItem = 5;

UPDATE Arma SET classe = 'Fogo', dano = 300
    WHERE idItem = 6;

-- Inserir dados na tabela Fogo
INSERT INTO Fogo(idItem)
    SELECT idItem FROM Arma
        WHERE classe = 'Fogo';

UPDATE Fogo SET nome = 'Pistola', distancia = '10', capacidadeMunicao = '13'
    WHERE idItem = 6;

-- Inserir dados na tabela Branca
INSERT INTO Branca(idItem)
    SELECT idItem FROM Arma
        WHERE classe = 'Branca';

UPDATE Branca SET nome = 'Faca', material = 'Metal'
    WHERE idItem = 5;

COMMIT;