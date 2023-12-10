-- Tabela Mapa
CREATE TABLE Mapa (
    idMapa INT PRIMARY KEY,
    dimensao INT NOT NULL,
    nomeMapa VARCHAR(255) NOT NULL,
    descricao VARCHAR(1000) NOT NULL
);

-- Tabela Cidade
CREATE TABLE Cidade (
    nome VARCHAR(255) PRIMARY KEY NOT NULL,
    mapa INT NOT NULL,
    nroConstrucoes INT NOT NULL DEFAULT 0, -- Quantidade de salas
    CONSTRAINT fk_cidade_mapa FOREIGN KEY (mapa) REFERENCES Mapa(idMapa)
);

-- Tabela Sala 
CREATE TABLE Sala  (
    idSala INT PRIMARY KEY,
    nome VARCHAR(255),
    cidade VARCHAR(255),
    descricao VARCHAR(1000) NOT NULL,
    CONSTRAINT fk_sala_cidade FOREIGN KEY (cidade) REFERENCES Cidade(nome)
);

-- Tabela Veículo
CREATE TABLE Veiculo (
    idVeiculo INT PRIMARY KEY,
    tipo VARCHAR(255) NOT NULL,
    CONSTRAINT veiculo_tipo_check CHECK (tipo IN ('Aereo', 'Aquatico', 'Terrestre'))
);

-- Tabela veículo terrestre
CREATE TABLE Terrestre (
    idVeiculo INT PRIMARY KEY,
    -- cidade VARCHAR(255) NOT NULL,
    sala INT NOT NULL,
    nome VARCHAR(255) NOT NULL DEFAULT 'Carro',
    vida INT NOT NULL DEFAULT 100,
    numRodas SMALLINT NOT NULL DEFAULT 4,
    combustivel INT NOT NULL DEFAULT 100,
    CONSTRAINT fk_terrestre_veiculo FOREIGN KEY (idVeiculo) REFERENCES Veiculo(idVeiculo),
    -- CONSTRAINT fk_terrestre_cidade FOREIGN KEY (cidade) REFERENCES Cidade(nome),
    CONSTRAINT fk_terrestre_sala FOREIGN KEY (sala) REFERENCES Sala(idSala),
    CHECK (vida > 0)
);

-- Tabela veículo aquático
CREATE TABLE Aquatico (
    idVeiculo INT PRIMARY KEY,
    -- cidade VARCHAR(255) NOT NULL,
    sala INT NOT NULL,
    nome VARCHAR(255) NOT NULL DEFAULT 'Barco',
    vida INT NOT NULL DEFAULT 100,
    combustivel INT NOT NULL DEFAULT 100,
    propulsao INT NOT NULL DEFAULT 30,
    CONSTRAINT fk_aquatico_veiculo FOREIGN KEY (idVeiculo) REFERENCES Veiculo(idVeiculo),
    -- CONSTRAINT fk_aquatico_cidade FOREIGN KEY (cidade) REFERENCES Cidade(nome),
    CONSTRAINT fk_aquatico_sala FOREIGN KEY (sala) REFERENCES Sala(idSala),
    CHECK (vida > 0)
);

-- Tabela veículo aéreo
CREATE TABLE Aereo (
    idVeiculo INT PRIMARY KEY,
    -- cidade VARCHAR(255) NOT NULL,
    sala INT NOT NULL,
    nome VARCHAR(255) NOT NULL DEFAULT 'Aviao',
    vida INT NOT NULL DEFAULT 100,
    combustivel INT NOT NULL DEFAULT 100,
    maxAltitude INT NOT NULL DEFAULT 250,
    CONSTRAINT fk_aereo_veiculo FOREIGN KEY (idVeiculo) REFERENCES Veiculo(idVeiculo),
    -- CONSTRAINT fk_aquatico_cidade FOREIGN KEY (cidade) REFERENCES Cidade(nome),
    CONSTRAINT fk_aquatico_sala FOREIGN KEY (sala) REFERENCES Sala(idSala),
    CHECK (vida > 0)
);

-- Tabela Personagem
CREATE TABLE Personagem (
    idPersonagem INT PRIMARY KEY NOT NULL,
    tipo VARCHAR(255) NOT NULL,
    CONSTRAINT personagem_tipo_check CHECK (tipo IN ('NPC', 'PC'))
);

-- Tabela do player character
CREATE TABLE PC (
    idPersonagem INT PRIMARY KEY,
    sala INT,
    nome VARCHAR(255) DEFAULT 'Steve',
    vida INT NOT NULL DEFAULT 100,
    stamina INT NOT NULL DEFAULT 100,
    CONSTRAINT fk_pc_personagem FOREIGN KEY (idPersonagem) REFERENCES Personagem(idPersonagem),
    CONSTRAINT fk_pc_sala FOREIGN KEY (sala) REFERENCES Sala(idSala)
);

-- Tabela do non player character
CREATE TABLE NPC (
    idPersonagem INT PRIMARY KEY,
    tipo_npc VARCHAR(255) NOT NULL DEFAULT 'Zumbi',
    CONSTRAINT fk_npc_personagem FOREIGN KEY (idPersonagem) REFERENCES Personagem(idPersonagem),
    CONSTRAINT NPC_tipo_check CHECK (tipo_npc IN ('Zumbi', 'Animal'))
);

-- Tabela do tipo zumbi
CREATE TABLE Zumbi (
    idPersonagem INT PRIMARY KEY,
    vida INT NOT NULL DEFAULT 100,
    classe VARCHAR(255) NOT NULL DEFAULT 'Andarilho',
    dano INT NOT NULL DEFAULT 80,
    CONSTRAINT fk_zumbi_personagem FOREIGN KEY (idPersonagem) REFERENCES Personagem(idPersonagem),
    CONSTRAINT Zumbi_classe_check CHECK (classe IN ('Corredor', 'Andarilho', 'Rastejante'))
);

-- Tabela do tipo animal
CREATE TABLE Animal (
    idPersonagem INT PRIMARY KEY,
    vida INT NOT NULL DEFAULT 100,
    especie VARCHAR(255) NOT NULL DEFAULT 'Boi',
    CONSTRAINT fk_animal_personagem FOREIGN KEY (idPersonagem) REFERENCES Personagem(idPersonagem)
);

-- Tabela para as instancias do mesmo NPC
CREATE TABLE Instancia (
    idInstancia INT PRIMARY KEY NOT NULL,
    NPC INT NOT NULL,
    sala INT NOT NULL,
    CONSTRAINT fk_instancia_npc FOREIGN KEY (NPC) REFERENCES NPC(idPersonagem),
    CONSTRAINT fk_instancia_sala FOREIGN KEY (sala) REFERENCES Sala(idSala)
);

-- Tabela de missão
CREATE TABLE Missao(
    idMissao INT PRIMARY KEY,
    idPersonagem INT NOT NULL,
    Descricao VARCHAR(255),
    Recompensa VARCHAR(255),
    Estado VARCHAR(255),
    CONSTRAINT check_estado_missao CHECK (Estado IN ('Doing', 'Done')),
    CONSTRAINT fk_personagem_missao FOREIGN KEY (idPersonagem) REFERENCES PC(idPersonagem) -- Pode ser Personagem em vez de PC
);

-- Tabela do criador
CREATE TABLE Criador(
    idCriador INT PRIMARY KEY,
    idPersonagem INT NOT NULL,
    nome VARCHAR(255),
    CONSTRAINT fk_personagem_missao FOREIGN KEY (idPersonagem) REFERENCES PC(idPersonagem) -- Pode ser Personagem em vez de PC
);

-- Tabela do Item
CREATE TABLE Item (
    idItem INT PRIMARY KEY,
    tipo VARCHAR(255) DEFAULT 'Alimento',
    CONSTRAINT item_tipo_check CHECK (tipo IN ('Ferramenta', 'Alimento', 'Arma'))
);

-- Tabela da receita
CREATE TABLE Receita(
    idReceita INT PRIMARY KEY,
    idCriador INT NOT NULL,
    idItem INT NOT NULL,
    Resultado VARCHAR(255),
    Requisitos VARCHAR(255),
    TempoCriacao INT NOT NULL,
    CONSTRAINT fk_criador_receita FOREIGN KEY (idCriador) REFERENCES Criador(idCriador),
    CONSTRAINT fk_item_receita FOREIGN KEY (idItem) REFERENCES Item(idItem)
);

-- Tabela do Inventário
CREATE TABLE Inventario (
    personagem INT PRIMARY KEY,
    quantidadeItens INT DEFAULT 0,
    maxItens INT DEFAULT 20,
    CONSTRAINT fk_inventario_personagem FOREIGN KEY (personagem) REFERENCES Personagem(idPersonagem),
    CONSTRAINT inventario_quantidadeItem_check CHECK (quantidadeItens < maxItens)
);

-- Tabela das Ferramentas
CREATE TABLE Ferramenta (
    idItem INT PRIMARY KEY,
    sala INT,
    inventario INT,
    durabilidade INT DEFAULT 100,
    nome VARCHAR(255) NOT NULL,
    CONSTRAINT fk_ferramenta_item FOREIGN KEY (idItem) REFERENCES Item(idItem),
    CONSTRAINT fk_ferramenta_inventario FOREIGN KEY (inventario) REFERENCES Inventario(personagem),
    CONSTRAINT fk_ferramenta_sala FOREIGN KEY (sala) REFERENCES Sala(idSala)
);

-- Tabela do Alimento
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
);

-- Tabela da Arma
CREATE TABLE Arma (
    idItem INT PRIMARY KEY,
    tipo_arma VARCHAR(255),
    CONSTRAINT fk_arma_item FOREIGN KEY (idItem) REFERENCES Item(idItem),
    CONSTRAINT arma_tipo_check CHECK (tipo_arma IN ('Fogo', 'Branca'))
);

-- Tabela de arma de fogo
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
);

-- Tabela de armas brancas
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
);
