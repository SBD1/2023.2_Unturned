-- Inserir dados na tabela Mapa
INSERT INTO Mapa (idMapa, dimensao, nomeMapa, descricao)
VALUES (1, 1, 'Washington', 'Esta nos EUA'),
       (2, 2, 'PEI', 'Esta na India'),
       (3, 3, 'Yukon', 'Esta na China'),
       (4, 4, 'Russia', 'Esta na Russia'),
       (5, 5, 'EUA', 'Esta nos EUA');


-- Inserir dados na tabela Cidade
INSERT INTO Cidade (nome, mapa, nroConstrucoes)
VALUES ('Seattle', 1, 0),
       ('Charlottetown', 2, 0),
       ('Whitehorse', 3, 0),
       ('Formosa', 4, 0),
       ('Chicago', 5, 0);

-- Inserir dados na tabela Sala
INSERT INTO Sala (idSala, nome, cidade, descricao) VALUES
(1, 'Sala de Reuniões A', 'Chicago', 'Uma sala de reuniões equipada com tecnologia de ponta para apresentações e videoconferências'),
(2, 'Auditório B', 'Formosa', 'Um amplo auditório com capacidade para 100 pessoas, ideal para palestras e eventos'),
(3, 'Sala de Treinamento C', 'Whitehorse', 'Espaço dedicado para treinamentos corporativos, com mesas configuráveis e recursos audiovisuais'),
(4, 'Sala de Estudo D', 'Charlottetown', 'Ambiente tranquilo e silencioso, projetado para estudos individuais e em grupo'),
(5, 'Sala de Conferências E', 'Seattle', 'Sala versátil com configuração modular, adequada para conferências, workshops e seminários');
 
-- Para inserir veiculo terrestre
CALL insere_veiculo(1, 1, 'Ferrari', 100, 100, 4::smallint, NULL::int, NULL::int);

-- Para inserir veículo aquático
CALL insere_veiculo(2, 2, 'Barco', 80, 67, NULL::smallint, 50, NULL::int);

-- Para inserir veículo aéreo
CALL insere_veiculo(3, 3, 'Airbus', 90, 97, NULL::smallint, NULL::int, 10000);

-- Para dar algum update no veiculo para passar ele para terrestre
CALL update_veiculo(2, 2, 'Maseratti', 50, 48, 4::smallint, NULL::int, NULL::int);

-- Para deletar algum id de veiculo
CALL removerVeiculo(2);

-- Para inserir um PC por procedure
CALL inserirPersonagem(1, 1, 'Joao', 100, 100, NULL, NULL, NULL);

-- Para inserir um zumbi por procedure
CALL inserirPersonagem(2, NULL, NULL, 100, NULL, 'Andarilho', 50, NULL);

-- Para inserir um animal por procedure
CALL inserirPersonagem(3, NULL, NULL, 100, NULL, NULL, NULL, 'Vaca');

-- Para fazer um update na tabela Animal, mudando o necessário, pode mudar apenas um atributo se quiser
CALL updateAnimal(3, 65, 'Urubu');

-- Para fazer update na tabela Zumbi, mudando o necessário, pode mudar apenas um atributo se quiser
CALL updateZumbi(2, 30, 'Corredor', 20);

-- Para fazer update na tabela PC, mudando o necessário, pode mudar os 4 ou 3 ou 1 atributos especificos 
CALL updatePC(1, 2,'Joao', 100, 100)
CALL updatePC(1, NULL,'Mauricio', 70, 50)
CALL updatePC(1, NULL,NULL, NULL, 50)

-- Para deletar um PC com um id eistente
CALL deletePC(1);

-- Para deletar um Zumbi com um id existente
CALL deleteZumbi(1);

-- Para deletar um Animal com um id existente
CALL deleteAnimal(1);

-- Inserir dados na tabela Instancia
INSERT INTO Instancia (idInstancia, NPC, sala)
    VALUES (1, 2, 1),
           (2, 2, 1),
           (3, 2, 1),
           (4, 2, 2),
           (5, 3, 2),
           (6, 3, 3),
           (7, 3, 3),
           (8, 3, 4);

-- Inserir dados na tabela Inventario
INSERT INTO Inventario (Personagem, quantidadeItens, maxItens)
    VALUES (1, 0, 10)

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