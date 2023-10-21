-- Tabela Mapa
CREATE TABLE Mapa (
    idMapa INT PRIMARY KEY NOT NULL IDENTITY(1,1),
    dimensao INT,
    nomeMapa VARCHAR(255)
);

-- Tabela Cidade
CREATE TABLE Cidade (
    nome VARCHAR(255) PRIMARY KEY NOT NULL IDENTITY(1,1),
    mapa VARCHAR(255) NOT NULL,
    radioatividade INT NOT NULL,
    FOREIGN KEY (mapa) REFERENCES Mapa(nomeMapa)
);

-- Tabela Veículo
CREATE TABLE Veiculo (
    idVeiculo INT PRIMARY KEY NOT NULL IDENTITY(1,1),
    cidade VARCHAR(255) NOT NULL,
    tipo VARCHAR(255) NOT NULL,
    FOREIGN KEY (cidade) REFERENCES Cidade(nome)
);

-- Tabela Personagem
CREATE TABLE Personagem (
    idPersonagem INT PRIMARY KEY NOT NULL IDENTITY(1,1),
    cidade VARCHAR(255) NOT NULL,
    tipo VARCHAR(255) NOT NULL,
    FOREIGN KEY (cidade) REFERENCES Cidade(nome)
);
