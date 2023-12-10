-- Mapa/Cidade
SELECT cidade.nome AS "Nome da Cidade", mapa.nomeMapa AS "Nome do Mapa"
FROM cidade
    JOIN mapa ON cidade.mapa = mapa.idMapa;

-- Personagem
SELECT genetica, COUNT(*) AS quantidade_de_npc
FROM NPC
GROUP BY genetica;

SELECT cidade, COUNT(*) AS quantidade_de_instancias
FROM Instancia
GROUP BY cidade;

SELECT tipo, cidade, COUNT(*) AS quantidade_de_personagens
FROM Personagem
GROUP BY tipo, cidade
ORDER BY tipo;

SELECT nome, tipo
FROM PC
    INNER JOIN Personagem ON PC.idPersonagem = Personagem.idPersonagem
WHERE tipo = 'PC'
ORDER BY nome;

-- Inventário
SELECT *
FROM Inventario
ORDER BY quantidadeItens ASC;

SELECT tipo, COUNT(*) AS quantidade_de_itens
FROM Item
GROUP BY tipo;

SELECT classe, COUNT(*) AS quantidade_de_armas
FROM (
                            SELECT 'Fogo' AS classe
        FROM Fogo
    UNION ALL
        SELECT 'Branca' AS classe
        FROM Branca
) AS armas
GROUP BY classe;

-- Veículos

SELECT t.nome AS "Nome do Veículo",
    c.nome AS "Nome da Cidade",
    m.nomeMapa AS "Nome do Mapa"
FROM terrestre t
    INNER JOIN cidade c ON t.cidade = c.nome
    INNER JOIN mapa m ON c.mapa = m.idMapa;

SELECT a.nome AS "Nome do Veículo",
    c.nome AS "Nome da Cidade",
    m.nomeMapa AS "Nome do Mapa"
FROM aquatico a
    INNER JOIN cidade c ON a.cidade = c.nome
    INNER JOIN mapa m ON c.mapa = m.idMapa;

SELECT ae.nome AS "Nome do Veículo",
    c.nome AS "Nome da Cidade",
    m.nomeMapa AS "Nome do Mapa"
FROM aereo ae
    INNER JOIN cidade c ON ae.cidade = c.nome
    INNER JOIN mapa m ON c.mapa = m.idMapa;

SELECT tipo, COUNT(*) AS quantidade_de_veiculos
FROM Veiculo
GROUP BY tipo;

-- Listar Tudo
SELECT *
FROM mapa;
SELECT *
FROM cidade;
SELECT *
FROM veiculo;
SELECT *
FROM terrestre;
SELECT *
FROM aereo;
SELECT *
FROM aquatico;
SELECT *
FROM personagem;
SELECT *
FROM pc;
SELECT *
FROM npc;
SELECT *
FROM instancia;
SELECT *
FROM zumbi;
SELECT *
FROM animal;
SELECT *
FROM inventario;
SELECT *
FROM item;
SELECT *
FROM arma;
SELECT *
FROM ferramenta;
SELECT *
FROM alimento;
SELECT *
FROM fogo;
SELECT *
FROM branca;
