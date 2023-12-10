class PC:
    def __init__(self, idPersonagem, sala, nome='Steve', vida=100, stamina=100):
        self.idPersonagem = idPersonagem
        self.sala = sala
        self.nome = nome
        self.vida = vida
        self.stamina = stamina


class Zumbi:
    def __init__(self, idPersonagem, vida=100, classe='Andarilho', dano=80):
        self.idPersonagem = idPersonagem
        self.vida = vida
        self.classe = classe
        self.dano = dano

class Animal:
    def __init__(self, idPersonagem, vida=100, especie='Boi'):
        self.idPersonagem = idPersonagem
        self.vida = vida
        self.especie = especie

class Fogo:
    def __init__(self, idItem, sala, inventario, nome, dano, distancia=10, capacidadeMunicao=15):
        self.idItem = idItem
        self.sala = sala
        self.inventario = inventario
        self.nome = nome
        self.dano = dano
        self.distancia = distancia
        self.capacidadeMunicao = capacidadeMunicao

class Branca:
    def __init__(self, idItem, sala, inventario, nome='Faca', dano=0, material='Madeira'):
        self.idItem = idItem
        self.sala = sala
        self.inventario = inventario
        self.nome = nome
        self.dano = dano
        self.material = material

class Mortes:
    def death_by_running():
        print("\nInfelizmente, ao tentar correr, o zumbi te alcança e te captura.")
        print("Você é incapaz de escapar, e o zumbi, com sede de carne humana, te devora.")
        print("Game over. Sua jornada chegou ao fim. O apocalipse zumbi é impiedoso.")
        exit()

    def death_by_courage():
        print("Infelizmente, os zumbis são muitos e te cercam. Você não consegue escapar.")
        print("Game over. Sua jornada chegou ao fim. O apocalipse zumbi é impiedoso.")
        exit()

    def death_by_bite():
        print("Após ser mordido você começa a passar mal rapidamente.")
        print("Olha para o seu braço e está começando a se transformar.")
        print("Sua consciência é tomada pela sede de sangue agora...")
        print("Game over. Sua jornada chegou ao fim. O apocalipse zumbi é impiedoso.")
        exit()

    def death_by_drowning():
        print("Você tenta nadar até o outro lado do rio, mas está cansado demais para isso.")
        print("Logo percebe que não vai conseguir, aceitando lentamente seu destino final.")
        print("Em pouco tempo, lembra dos momentos felizes que viveu e de todas as decisões até aquele momento.")
        print("Deixando o lado tomar seu corpo como seu, o levando para o fundo...")
        print("Game over. Sua jornada chegou ao fim. O apocalipse zumbi é impiedoso.")
        exit()

class Acoes:
    def pegar_galao_gasolina():
        print("\nVocê pega o galão de gasolina. Agora, você tem um meio de abastecer o carro.")

    def continuar_explorando_sem_gasolina():
        print("\nVocê decide deixar o galão de gasolina e continua explorando a fazenda.")

    def atirar_pistola():
        print("\nVocê atira no zumbi chorador com a pistola, acertando alguns tiros.")
        print("O zumbi é atingido, mas continua se aproximando.")

    def correr_ligar_barco():
        print("\nVocê tenta correr até o barco para ligá-lo, mas o zumbi chorador está muito próximo.")
        print("Antes que você alcance o barco, o zumbi agarra você, impedindo sua fuga.")

    def usar_bandagem():
        print("\nVocê usa uma bandagem para se curar rapidamente.")
        print("Enquanto se cura, o zumbi chorador se aproxima, mas o zumbi agarra você, impedindo você se curar..")

    def correr_ligar_barco_zumbi_caido():
        print("\nVocê tenta correr até o barco para ligá-lo, mas o zumbi chorador está muito próximo.")
        print("Mas com ele quase o alcançando-o, você consegue dar partida, saindo dali rapidamente.")
        print("Agora você o deixa em um horizonte distante enquanto escapa")

    def explorar_fazenda():
        print("\nVocê decide explorar a fazenda antes de pegar o carro.")
        print("\nEm um galpão, você encontra um galão de gasolina.")

    def jogar_molotov():
        print("\nVocê joga o molotov no zumbi chorador, criando uma explosão de chamas.")
        print("O zumbi é consumido pelas chamas e mas não é abatido, agora ele corre atrás de você pegando fogo.")

    def atirar_metralhadora():
        print("\nVocê dispara a metralhadora contra o zumbi chorador, acertando vários tiros.")
        print("O zumbi e cai no chão, mas não está morto")
        

