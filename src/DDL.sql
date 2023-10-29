-- Tabela Mapa
CREATE TABLE Mapa (
    idMapa INT PRIMARY KEY,
    dimensao INT NOT NULL,
    nomeMapa VARCHAR(255) NOT NULL
);

-- Tabela Cidade
CREATE TABLE Cidade (
    nome VARCHAR(255) PRIMARY KEY NOT NULL,
    mapa INT NOT NULL,
    radioatividade INT NOT NULL,
    CONSTRAINT fk_cidade_mapa FOREIGN KEY (mapa) REFERENCES Mapa(idMapa)
);

-- Tabela Veículo
CREATE TABLE Veiculo (
    idVeiculo INT  PRIMARY KEY,
    cidade VARCHAR(255) NOT NULL,
    tipo VARCHAR(255) NOT NULL,
    CONSTRAINT fk_veiculo_cidade FOREIGN KEY (cidade) REFERENCES Cidade(nome),
    CONSTRAINT veiculo_tipo_check CHECK (tipo IN ('Aereo', 'Aquatico', 'Terrestre'))
);

-- Tabela veículo terrestre
CREATE TABLE Terrestre (
    idVeiculo INT NOT NULL,
    cidade VARCHAR(255) NOT NULL,
    nome VARCHAR(255) NOT NULL DEFAULT 'Carro',
    vida INT NOT NULL DEFAULT 100,
    numRodas SMALLINT NOT NULL DEFAULT 4,
    combustivel INT NOT NULL DEFAULT 100,
    CONSTRAINT fk_terrestre_veiculo FOREIGN KEY (idVeiculo) REFERENCES Veiculo(idVeiculo),
    CONSTRAINT fk_terrestre_cidade FOREIGN KEY (cidade) REFERENCES Cidade(nome),
    CHECK (vida > 0)
);

-- Tabela veículo aquático
CREATE TABLE Aquatico (
    idVeiculo INT NOT NULL,
    cidade VARCHAR(255) NOT NULL,
    nome VARCHAR(255) NOT NULL DEFAULT 'Barco',
    vida INT NOT NULL DEFAULT 100,
    combustivel INT NOT NULL DEFAULT 100,
    propulsao INT NOT NULL DEFAULT 30,
    CONSTRAINT fk_aquatico_veiculo FOREIGN KEY (idVeiculo) REFERENCES Veiculo(idVeiculo),
    CONSTRAINT fk_aquatico_cidade FOREIGN KEY (cidade) REFERENCES Cidade(nome),
    CHECK (vida > 0)
);

-- Tabela veículo aéreo
CREATE TABLE Aereo (
    idVeiculo INT NOT NULL,
    cidade VARCHAR(255) NOT NULL,
    nome VARCHAR(255) NOT NULL DEFAULT 'Aviao',
    vida INT NOT NULL DEFAULT 100,
    combustivel INT NOT NULL DEFAULT 100,
    maxAltitude INT NOT NULL DEFAULT 250,
    CONSTRAINT fk_aereo_veiculo FOREIGN KEY (idVeiculo) REFERENCES Veiculo(idVeiculo),
    CONSTRAINT fk_aquatico_cidade FOREIGN KEY (cidade) REFERENCES Cidade(nome),
    CHECK (vida > 0)
);

-- Tabela Personagem
CREATE TABLE Personagem (
    idPersonagem INT PRIMARY KEY NOT NULL,
    cidade VARCHAR(255) NOT NULL,
    tipo VARCHAR(255) NOT NULL,
    CONSTRAINT fk_personagem_cidade FOREIGN KEY (cidade) REFERENCES Cidade(nome),
    CONSTRAINT personagem_tipo_check CHECK (tipo IN ('NPC', 'PC'))
);

-- Tabela do player character
CREATE TABLE PC (
    idPersonagem INT PRIMARY KEY,
    nome VARCHAR(255) DEFAULT 'Steve',
    vida INT NOT NULL DEFAULT 100,
    stamina INT NOT NULL DEFAULT 100,
    CONSTRAINT fk_pc_personagem FOREIGN KEY (idPersonagem) REFERENCES Personagem(idPersonagem)
);

-- Tabela do non player character
CREATE TABLE NPC (
    idPersonagem INT PRIMARY KEY,
    vida INT NOT NULL DEFAULT 100,
    genetica VARCHAR(255) NOT NULL DEFAULT 'Zumbi',
    CONSTRAINT fk_npc_personagem FOREIGN KEY (idPersonagem) REFERENCES Personagem(idPersonagem),
    CONSTRAINT NPC_genetica_check CHECK (genetica IN ('Zumbi', 'Animal'))
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
    cidade VARCHAR(255) NOT NULL,
    CONSTRAINT fk_instancia_npc FOREIGN KEY (NPC) REFERENCES NPC(idPersonagem),
    CONSTRAINT fk_instancia_cidade FOREIGN KEY (cidade) REFERENCES Cidade(nome)
);

-- Tabela do Inventário
CREATE TABLE Inventario (
    personagem INT,
    quantidadeItens INT DEFAULT 0,
    maxItens INT DEFAULT 20,
    CONSTRAINT fk_inventario_personagem FOREIGN KEY (personagem) REFERENCES Personagem(idPersonagem),
    CONSTRAINT inventario_quantidadeItem_check CHECK (quantidadeItens < maxItens)
);

-- Tabela do Item
CREATE TABLE Item (
    idItem INT PRIMARY KEY,
    cidade VARCHAR(255),
    personagem INT,
    tipo VARCHAR(255) DEFAULT 'Alimento',
    CONSTRAINT fk_item_cidade FOREIGN KEY (cidade) REFERENCES Cidade(nome),
    CONSTRAINT fk_item_personagem FOREIGN KEY (personagem) REFERENCES Personagem(idPersonagem),
    CONSTRAINT item_tipo_check CHECK (tipo IN ('Ferramenta', 'Alimento', 'Arma'))
);

-- Tabela das Ferramentas
CREATE TABLE Ferramenta (
    idItem INT PRIMARY KEY,
    --tipo VARCHAR(255),
    durabilidade INT DEFAULT 100,
    CONSTRAINT fk_ferramentas_item FOREIGN KEY (idItem) REFERENCES Item(idItem)
);

-- Tabela do Alimento
CREATE TABLE Alimento (
    idItem INT PRIMARY KEY,
    --tipo VARCHAR(255),
    status VARCHAR(255) DEFAULT 'Excelente',
    CONSTRAINT fk_alimento_item FOREIGN KEY (idItem) REFERENCES Item(idItem),
    CONSTRAINT alimento_status_check CHECK (status IN ('Excelente', 'Bom', 'Mediano', 'Ruim', 'Pessimo'))
);

-- Tabela da Arma
CREATE TABLE Arma (
    idItem INT PRIMARY KEY,
    --tipo VARCHAR(255),
    classe VARCHAR(255) DEFAULT 'Fogo',
    --nome VARCHAR(255) DEFAULT 'Pistola',
    dano INT DEFAULT '15',
    CONSTRAINT fk_arma_item FOREIGN KEY (idItem) REFERENCES Item(idItem),
    CONSTRAINT arma_classe_check CHECK (classe IN ('Fogo', 'Branca'))
);

-- Tabela de arma de fogo
CREATE TABLE Fogo (
    idItem INT PRIMARY KEY,
    --tipo VARCHAR(255),
    --classe VARCHAR(255),
    nome VARCHAR(255),
    --dano INT,
    distancia INT DEFAULT 10,
    capacidadeMunicao INT DEFAULT 15,
    CONSTRAINT fk_fogo_arma FOREIGN KEY (idItem) REFERENCES Arma(idItem)
);

-- Tabela de armas brancas
CREATE TABLE Branca (
    idItem INT PRIMARY KEY,
    --tipo VARCHAR(255),
    --classe VARCHAR(255),
    nome VARCHAR(255) DEFAULT 'Faca',
    --dano INT,
    material VARCHAR(255) DEFAULT 'Madeira',
    CONSTRAINT fk_branca_arma FOREIGN KEY (idItem) REFERENCES Arma(idItem)
);
