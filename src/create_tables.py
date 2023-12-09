import psycopg2


conn = psycopg2.connect(
    host="172.21.0.3",           
    database="mydatabase",     
    user="myuser",             
    password="mysecretpassword"
)


cur = conn.cursor()

sql_commands = [
    """
    CREATE TABLE Mapa (
        idMapa SERIAL PRIMARY KEY,
        dimensao INT NOT NULL,
        nomeMapa VARCHAR(255) NOT NULL,
        descricao VARCHAR(1000) NOT NULL
    )
    """,
    """
    CREATE TABLE Cidade (
        nome VARCHAR(255) PRIMARY KEY NOT NULL,
        mapa INT NOT NULL,
        nroConstrucoes INT NOT NULL DEFAULT 0,
        CONSTRAINT fk_cidade_mapa FOREIGN KEY (mapa) REFERENCES Mapa(idMapa)
    )
    """,
    """
    CREATE TABLE Sala (
        idSala SERIAL PRIMARY KEY,
        cidade VARCHAR(255),
        radioatividade INT NOT NULL,
        descricao VARCHAR(1000) NOT NULL,
        CONSTRAINT fk_sala_cidade FOREIGN KEY (cidade) REFERENCES Cidade(nome)
    )
    """,
    """
    CREATE TABLE Veiculo (
        idVeiculo SERIAL PRIMARY KEY,
        tipo VARCHAR(255) NOT NULL,
        CONSTRAINT veiculo_tipo_check CHECK (tipo IN ('Aereo', 'Aquatico', 'Terrestre'))
    )
    """,
    """
    CREATE TABLE Terrestre (
        idVeiculo SERIAL PRIMARY KEY,
        sala INT NOT NULL,
        nome VARCHAR(255) NOT NULL DEFAULT 'Carro',
        vida INT NOT NULL DEFAULT 100,
        numRodas SMALLINT NOT NULL DEFAULT 4,
        combustivel INT NOT NULL DEFAULT 100,
        CONSTRAINT fk_terrestre_veiculo FOREIGN KEY (idVeiculo) REFERENCES Veiculo(idVeiculo),
        CONSTRAINT fk_terrestre_sala FOREIGN KEY (sala) REFERENCES Sala(idSala),
        CHECK (vida > 0)
    )
    """,
    """
    CREATE TABLE Aquatico (
        idVeiculo SERIAL PRIMARY KEY,
        sala INT NOT NULL,
        nome VARCHAR(255) NOT NULL DEFAULT 'Barco',
        vida INT NOT NULL DEFAULT 100,
        combustivel INT NOT NULL DEFAULT 100,
        propulsao INT NOT NULL DEFAULT 30,
        CONSTRAINT fk_aquatico_veiculo FOREIGN KEY (idVeiculo) REFERENCES Veiculo(idVeiculo),
        CONSTRAINT fk_aquatico_sala FOREIGN KEY (sala) REFERENCES Sala(idSala),
        CHECK (vida > 0)
    )
    """,
    """
    CREATE TABLE Aereo (
        idVeiculo SERIAL PRIMARY KEY,
        sala INT NOT NULL,
        nome VARCHAR(255) NOT NULL DEFAULT 'Aviao',
        vida INT NOT NULL DEFAULT 100,
        combustivel INT NOT NULL DEFAULT 100,
        maxAltitude INT NOT NULL DEFAULT 250,
        CONSTRAINT fk_aereo_veiculo FOREIGN KEY (idVeiculo) REFERENCES Veiculo(idVeiculo),
        CONSTRAINT fk_aereo_sala FOREIGN KEY (sala) REFERENCES Sala(idSala),
        CHECK (vida > 0)
    )
    """,
    """
    CREATE TABLE Personagem (
        idPersonagem SERIAL PRIMARY KEY,
        tipo VARCHAR(255) NOT NULL,
        CONSTRAINT personagem_tipo_check CHECK (tipo IN ('NPC', 'PC'))
    )
    """,
    """
    CREATE TABLE PC (
        idPersonagem SERIAL PRIMARY KEY,
        sala INT,
        nome VARCHAR(255) DEFAULT 'Steve',
        vida INT NOT NULL DEFAULT 100,
        stamina INT NOT NULL DEFAULT 100,
        CONSTRAINT fk_pc_personagem FOREIGN KEY (idPersonagem) REFERENCES Personagem(idPersonagem),
        CONSTRAINT fk_pc_sala FOREIGN KEY (sala) REFERENCES Sala(idSala)
    )
    """,
    """
    CREATE TABLE NPC (
        idPersonagem SERIAL PRIMARY KEY,
        tipo_npc VARCHAR(255) NOT NULL DEFAULT 'Zumbi',
        CONSTRAINT fk_npc_personagem FOREIGN KEY (idPersonagem) REFERENCES Personagem(idPersonagem),
        CONSTRAINT NPC_tipo_check CHECK (tipo_npc IN ('Zumbi', 'Animal'))
    )
    """,
    """
    CREATE TABLE Zumbi (
        idPersonagem SERIAL PRIMARY KEY,
        vida INT NOT NULL DEFAULT 100,
        classe VARCHAR(255) NOT NULL DEFAULT 'Andarilho',
        dano INT NOT NULL DEFAULT 80,
        CONSTRAINT fk_zumbi_personagem FOREIGN KEY (idPersonagem) REFERENCES Personagem(idPersonagem),
        CONSTRAINT Zumbi_classe_check CHECK (classe IN ('Corredor', 'Andarilho', 'Rastejante'))
    )
    """,
    """
    CREATE TABLE Animal (
        idPersonagem SERIAL PRIMARY KEY,
        vida INT NOT NULL DEFAULT 100,
        especie VARCHAR(255) NOT NULL DEFAULT 'Boi',
        CONSTRAINT fk_animal_personagem FOREIGN KEY (idPersonagem) REFERENCES Personagem(idPersonagem)
    )
    """,
    """
    CREATE TABLE Instancia (
        idInstancia SERIAL PRIMARY KEY,
        NPC INT NOT NULL,
        sala INT NOT NULL,
        CONSTRAINT fk_instancia_npc FOREIGN KEY (NPC) REFERENCES NPC(idPersonagem),
        CONSTRAINT fk_instancia_sala FOREIGN KEY (sala) REFERENCES Sala(idSala)
    )
    """,
    """
    CREATE TABLE Missao (
        idMissao SERIAL PRIMARY KEY,
        idPersonagem INT NOT NULL,
        Descricao VARCHAR(255),
        Recompensa VARCHAR(255),
        Estado VARCHAR(255),
        CONSTRAINT check_estado_missao CHECK (Estado IN ('Doing', 'Done')),
        CONSTRAINT fk_personagem_missao FOREIGN KEY (idPersonagem) REFERENCES PC(idPersonagem)
    )
    """,
    """
    CREATE TABLE Criador (
        idCriador SERIAL PRIMARY KEY,
        idPersonagem INT NOT NULL,
        nome VARCHAR(255),
        CONSTRAINT fk_criador_personagem FOREIGN KEY (idPersonagem) REFERENCES PC(idPersonagem)
    )
    """,
    """
    CREATE TABLE Item (
        idItem SERIAL PRIMARY KEY,
        tipo VARCHAR(255) DEFAULT 'Alimento',
        CONSTRAINT item_tipo_check CHECK (tipo IN ('Ferramenta', 'Alimento', 'Arma'))
    )
    """,
    """
    CREATE TABLE Receita (
        idReceita SERIAL PRIMARY KEY,
        idCriador INT NOT NULL,
        idItem INT NOT NULL,
        Resultado VARCHAR(255),
        Requisitos VARCHAR(255),
        TempoCriacao INT NOT NULL,
        CONSTRAINT fk_criador_receita FOREIGN KEY (idCriador) REFERENCES Criador(idCriador),
        CONSTRAINT fk_item_receita FOREIGN KEY (idItem) REFERENCES Item(idItem)
    )
    """,
    """
    CREATE TABLE Inventario (
        personagem INT PRIMARY KEY,
        quantidadeItens INT DEFAULT 0,
        maxItens INT DEFAULT 20,
        CONSTRAINT fk_inventario_personagem FOREIGN KEY (personagem) REFERENCES Personagem(idPersonagem),
        CONSTRAINT inventario_quantidadeItem_check CHECK (quantidadeItens < maxItens)
    )
    """,
    """
    CREATE TABLE Ferramenta (
        idItem INT PRIMARY KEY,
        sala INT,
        inventario INT,
        durabilidade INT DEFAULT 100,
        CONSTRAINT fk_ferramenta_item FOREIGN KEY (idItem) REFERENCES Item(idItem),
        CONSTRAINT fk_ferramenta_inventario FOREIGN KEY (inventario) REFERENCES Inventario(personagem),
        CONSTRAINT fk_ferramenta_sala FOREIGN KEY (sala) REFERENCES Sala(idSala)
    )
    """,
    """
    CREATE TABLE Alimento (
        idItem INT PRIMARY KEY,
        sala INT,
        inventario INT,
        status VARCHAR(255) DEFAULT 'Excelente',
        CONSTRAINT fk_alimento_item FOREIGN KEY (idItem) REFERENCES Item(idItem),
        CONSTRAINT fk_alimento_inventario FOREIGN KEY (inventario) REFERENCES Inventario(personagem),
        CONSTRAINT fk_alimento_sala FOREIGN KEY (sala) REFERENCES Sala(idSala),
        CONSTRAINT alimento_status_check CHECK (status IN ('Excelente', 'Bom', 'Mediano', 'Ruim', 'Pessimo'))
    )
    """,
    """
    CREATE TABLE Arma (
        idItem INT PRIMARY KEY,
        tipo_arma VARCHAR(255),
        CONSTRAINT fk_arma_item FOREIGN KEY (idItem) REFERENCES Item(idItem),
        CONSTRAINT arma_tipo_check CHECK (tipo_arma IN ('Fogo', 'Branca'))
    )
    """,
    """
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
    )
    """,
    """
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
    )
    """
]

for command in sql_commands:
    cur.execute(command)

conn.commit()

cur.close()
conn.close()
