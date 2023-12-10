import psycopg2

# Função para inserir dados na tabela Mapa
def inserir_mapa(conn, cursor):
    dados_mapa = {
        "idMapa": 1,
        "dimensao": 5,
        "nomeMapa": "Russia",
        "descricao": """
            \n===== Início na Rússia - Terra Desolada =====
            Você acorda em uma cidade russa devastada, onde os edifícios estão em ruínas e as ruas estão vazias.
            O ar está impregnado com um silêncio tenso, quebrado apenas pelos gemidos distantes de zumbis.
            A temperatura está abaixo de zero, e a neve cobre o chão, tornando cada passo mais desafiador.
            Seu objetivo é sobreviver. Procure por abrigos, suprimentos e outros sobreviventes.
            Lembre-se, o inimigo não é apenas o frio, mas também os mortos-vivos que espreitam por toda parte.
            Boa sorte, sobrevivente. A Rússia tornou-se um campo de batalha, e sua habilidade de sobrevivência será testada.
        """
    }

    # Comando SQL para inserção na tabela Mapa
    comando_sql_mapa = """
        INSERT INTO Mapa (idMapa, dimensao, nomeMapa, descricao)
        VALUES (%(idMapa)s, %(dimensao)s, %(nomeMapa)s, %(descricao)s)
        RETURNING idMapa;
    """

    # Executar o comando SQL com os dados e recuperar o ID do mapa inserido
    cursor.execute(comando_sql_mapa, dados_mapa)
    id_mapa = cursor.fetchone()[0]

    # Confirmar a transação
    conn.commit()

    return id_mapa


# Função para inserir dados na tabela Cidade
def inserir_cidade(conn, cursor, nome_cidade, id_mapa):
    dados_cidade = {
        "nome": nome_cidade,
        "mapa": id_mapa,
        "nroConstrucoes": 0,
    }

    # Comando SQL para inserção na tabela Cidade
    comando_sql_cidade = """
        INSERT INTO Cidade (nome, mapa, nroConstrucoes)
        VALUES (%(nome)s, %(mapa)s, %(nroConstrucoes)s);
    """

    # Executar o comando SQL com os dados
    cursor.execute(comando_sql_cidade, dados_cidade)

    # Confirmar a transação
    conn.commit()


# Função para inserir dados na tabela Sala
def inserir_sala(conexao, cursor, nome_cidade, descricao_sala):
    dados_sala = {
        "cidade": nome_cidade,
        "descricao": descricao_sala,
    }

    # Comando SQL para inserção na tabela Sala
    comando_sql_sala = """
        INSERT INTO Sala (cidade, descricao)
        VALUES (%(cidade)s, %(descricao)s);
    """

    # Executar o comando SQL com os dados
    cursor.execute(comando_sql_sala, dados_sala)

    # Confirmar a transação
    conexao.commit()

def inserir_sala(conexao, cursor, nome_cidade, nome_sala, descricao_sala):
    dados_sala = {
        "cidade": nome_cidade,
        "nome": nome_sala,
        "descricao": descricao_sala,
    }

    # Comando SQL para inserção na tabela Sala
    comando_sql_sala = """
        INSERT INTO Sala (cidade, nome, descricao)
        VALUES (%(cidade)s, %(nome)s, %(descricao)s);
    """

    # Executar o comando SQL com os dados
    cursor.execute(comando_sql_sala, dados_sala)

    # Confirmar a transação
    conexao.commit()

# Conectar ao banco de dados
conn = psycopg2.connect(
    host="172.18.0.2",           
    database="unturned",     
    user="postgres",             
    password="postgres"
)


# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Inserir dados na tabela Mapa e recuperar o ID do mapa inserido
id_mapa = inserir_mapa(conn, cursor)

# Inserir dados na tabela Cidade com base no ID do mapa
inserir_cidade(conn, cursor, "Moscow", id_mapa)

# Cidade Arruinada
descricao_sala= """
    Você avança pela cidade arruinada de Moscow e de repente se depara com um zumbi faminto.
    O zumbi se aproxima lentamente, gemendo e com olhos vazios fixos em você.
"""

inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="cidade_arruinada", descricao_sala=descricao_sala)

# Casa Abandonada
descricao_sala= """
    Dentro da casa, você percebe que não está sozinho. Outro zumbi está no local.
"""

inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="casa_abandonada", descricao_sala=descricao_sala)

# Rua Deserta
descricao_sala= """
    Você pega os itens e decide avançar para fora da casa.
    Ao chegar na rua, você se depara com três zumbis bloqueando o caminho.
"""

inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="rua_deserta", descricao_sala=descricao_sala)

# Igreja
descricao_sala= """
    Você corre para dentro da igreja, conseguindo dividir os zumbis.
    Apenas um zumbi continua seguindo você para dentro da igreja.
"""

inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="celeiro", descricao_sala=descricao_sala)

# Celeiro
descricao_sala= """
    Você avança em direção ao celeiro e percebe que há um carro estacionado lá dentro.
"""

inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="fazenda_celeiro", descricao_sala=descricao_sala)

# Dentro do ceileiro
descricao_sala= """
    Você entra no celeiro e encontra um carro em boas condições.
    Ao se aproximar do carro, você ouve um som estranho vindo de dentro do celeiro.
    Curioso, você decide investigar e descobre um zumbi gigante chorando no interior do celeiro.
"""

inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="pegar_carro", descricao_sala=descricao_sala)

# Tentar ignorar o zumbi
descricao_sala= """
    Você entra no carro e tenta ignorar o zumbi gigante chorando no celeiro.
    O som é perturbador, mas ao tentar dar partida, você percebe que o carro está sem gasolina.
    O zumbi gigante, ao ouvir o barulho do carro, se levanta e o segue.
    Ele alcança você, puxa-o para fora do carro e joga-o para fora do celeiro.
"""

inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="tentar_ignorar_zumbi", descricao_sala=descricao_sala)

# Fugir para milharal
descricao_sala= """
    Você se vê fora do celeiro e decide correr para o milharal nas proximidades, tentando despistar o zumbi gigante.
    Você se embrenha entre as fileiras de milho, tentando manter-se fora do alcance do zumbi.
    No milharal, um zumbi rastejante surge e agarra sua perna, fazendo você cair.
    O zumbi chorador de antes continua a perseguição, se aproximando rapidamente.
"""

inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="fugir_para_milharal", descricao_sala=descricao_sala)

# Fugir para milharal
descricao_sala= """
    Você atira no zumbi rastejante, neutralizando a ameaça temporariamente.
"""

inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="atirar_zumbi_rastejante", descricao_sala=descricao_sala)

# Continuar fugindo milharal
descricao_sala= """
    Você se levanta rapidamente e continua a correr pelo milharal, tentando despistar o zumbi chorador.
    Ao sair do milharal, você se encontra à beira de um rio. Do lado oposto, avista um barco a motor.
"""

inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="continuar_fugindo_milharal", descricao_sala=descricao_sala)

# Nadar rio
descricao_sala= """
    Você pula no rio e começa a nadar vigorosamente até o outro lado.
    Ao alcançar a margem oposta, você se afasta do rio, olhando para trás para verificar se o zumbi chorador te seguiu.
"""

inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="nadar_rio", descricao_sala=descricao_sala)

# Correr ate barco
descricao_sala= """
    Você corre em direção ao barco a motor, esperando alcançá-lo antes que o zumbi chorador chegue até você.
    Ao chegar ao barco, você se depara com uma cena angustiante: uma família dilacerada pelos zumbis.
    Você também encontra uma mala próxima ao barco com, uma metralhadora, 2 bandagens e um molotov.
"""

inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="corre_ate_barco", descricao_sala=descricao_sala)

# Correr ligar barco zumbi caido
descricao_sala= """
    Você tenta correr até o barco para ligá-lo, mas o zumbi chorador está muito próximo.
    Mas com ele quase o alcançando-o, você consegue dar partida, saindo dali rapidamente.
    Agora você o deixa em um horizonte distante enquanto escapa
"""

inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="correr_ligar_barco_zumbi_caido", descricao_sala=descricao_sala)

# Correr ligar barco
descricao_sala= """
    Você tenta correr até o barco para ligá-lo, mas o zumbi chorador está muito próximo.
    Antes que você alcance o barco, o zumbi agarra você, impedindo sua fuga.
"""

inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="correr_ligar_barco", descricao_sala=descricao_sala)

# Pegar carro com gasolina
descricao_sala= """
    Você volta ao celeiro com o carro em boas condições.
    Fazendo o mínimo de barulho possível, você coloca a gasolina no tanque.
    Você entra no carro de fininho e dar partida, mas a partida chama a atenção do zumbi chorador no ceileiro
    Entretando, você acelera no desespero o deixando para traz e saindo daquela situação
"""

inserir_sala(conn, cursor, nome_cidade="Moscow", nome_sala="pegar_carro_com_gasolina", descricao_sala=descricao_sala)


# Fechar o cursor e a conexão
cursor.close()
conn.close()
