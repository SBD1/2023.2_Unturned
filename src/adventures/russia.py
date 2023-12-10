# import time
from Database import DataBase
import psycopg2

# Conectar ao banco de dados
conn = psycopg2.connect(
    host="172.21.0.3",           
    database="unturned",     
    user="postgres",             
    password="postgres"
)


# Criar um objeto cursor para executar comandos SQL
cur = conn.cursor()

def russia():
    DataBase.select_mapa_descricao(conn, cur)

# def cidade_arruinada():
#     print("\nVocê avança pela cidade arruinada e de repente se depara com um zumbi faminto.")
#     print("O zumbi se aproxima lentamente, gemendo e com olhos vazios fixos em você.")
    
    
#     while True:
#         print("\nOpções:")
#         print("1. Sair correndo")
#         print("2. Enfrentar o zumbi")

#         escolha = input("O que você deseja fazer? Escolha 1 ou 2: ")

#         if escolha == "1":
#             print("\nVocê decide correr para evitar o confronto imediato.")
#             print("Você corre desesperadamente e encontra uma casa próxima para se esconder.")
#             casa_abandonada()
#             break
#         elif escolha == "2":
#             print("\nVocê decide enfrentar o zumbi. Prepare-se para o combate!")
#             print("Após uma luta árdua, você consegue derrotar o zumbi.")
#             print("O zumbi dropa um item: uma faca.")
#             casa_abandonada_com_faca()
#             break
#         else:
#             print("Opção inválida. Por favor, escolha 1 para sair correndo ou 2 para enfrentar o zumbi.")

# def casa_abandonada():
#     print("\nDentro da casa, você percebe que não está sozinho. Outro zumbi está no local.")
#     # 
    
#     while True:
#         print("\nOpções:")
#         print("1. Sair correndo da casa")
#         print("2. Voltar para a rua onde encontrou o primeiro zumbi")

#         escolha = input("O que você deseja fazer? Escolha 1 ou 2: ")

#         if escolha == "1":
#             print("\nVocê decide sair correndo da casa, mas o zumbi te alcança e captura.")
#             death_by_running()
#             break
#         elif escolha == "2":
#             print("\nVocê decide voltar para a rua onde encontrou o primeiro zumbi.")
#             cidade_arruinada()
#             break
#         else:
#             print("Opção inválida. Por favor, escolha 1 para sair correndo da casa ou 2 para voltar para a rua.")

# def casa_abandonada_com_faca():
#     print("\nAo entrar na casa, você vê o zumbi que estava lá dentro.")
    
    
#     while True:
#         print("\nOpções:")
#         print("1. Enfrentar o zumbi")
#         print("2. Sair correndo para a rua")

#         escolha = input("O que você deseja fazer? Escolha 1 ou 2: ")

#         if escolha == "1":
#             print("\nVocê decide enfrentar o zumbi dentro da casa.")
#             print("Com a faca em mãos, você consegue derrotar o zumbi.")
#             casa_abandonada_exploracao()
#             break
#         elif escolha == "2":
#             print("\nVocê decide sair correndo da casa e volta para a rua.")
#             death_by_running()
#             break
#         else:
#             print("Opção inválida. Por favor, escolha 1 para enfrentar o zumbi ou 2 para sair correndo para a rua.")

# def casa_abandonada_exploracao():
#     print("\nCom o zumbi derrotado, você decide explorar a casa.")
    
#     print("Dentro da casa, você encontra alguns itens úteis.")
    

#     while True:
#         print("\nOpções:")
#         print("1. Pegar os itens e avançar")
#         print("2. Não pegar os itens e avançar para a rua")

#         escolha = input("O que você deseja fazer? Escolha 1 ou 2: ")

#         if escolha == "1":
#             print("\nVocê decide pegar os itens. Quem sabe eles possam ajudar na sua jornada.")
#             rua_deserta()
#             break
#         elif escolha == "2":
#             print("\nVocê decide não pegar os itens e avança para a rua.")
#             rua_deserta()
#             break
#         else:
#             print("Opção inválida. Por favor, escolha 1 para pegar os itens ou 2 para avançar para a rua.")

# def rua_deserta():
#     print("\nVocê pega os itens e decide avançar para fora da casa.")
#     print("\nAo chegar na rua, você se depara com três zumbis bloqueando o caminho.")
    

#     while True:
#         print("\nOpções:")
#         print("1. Enfrentar os zumbis")
#         print("2. Correr para dentro da igreja")

#         escolha = input("O que você deseja fazer? Escolha 1 ou 2: ")

#         if escolha == "1":
#             print("\nVocê decide enfrentar os três zumbis. Uma escolha ousada, mas arriscada.")
#             death_by_corage()
#         elif escolha == "2":
#             print("\nVocê decide correr para dentro da igreja, dividindo os zumbis.")
#             igreja()
#             break
#         else:
#             print("Opção inválida. Por favor, escolha 1 para enfrentar os zumbis ou 2 para correr para dentro da igreja.")


# def igreja():
#     print("\nVocê corre para dentro da igreja, conseguindo dividir os zumbis.")
    
#     print("Apenas um zumbi continua seguindo você para dentro da igreja.")
    
    
#     while True:
#         print("\nOpções:")
#         print("1. Se esgueirar pelas cadeiras e matar o zumbi pelas costas")
#         print("2. Fugir pela janela da igreja")

#         escolha = input("O que você deseja fazer? Escolha 1 ou 2: ")

#         if escolha == "1":
#             print("\nVocê decide se esgueirar pelas cadeiras, se aproximar do zumbi e atacar pelas costas.")
            
#             print("Com um golpe certeiro, você mata o zumbi sem chamar a atenção.")
#             igreja_armado()
#             break
#         elif escolha == "2":
#             print("\nVocê decide fugir pela janela da igreja, criando uma rota alternativa.")
            
#             print("Você consegue escapar pela janela e encontra uma rota diferente, evitando os outros zumbis na rua.")
#             fazenda_celeiro()
#             break
#         else:
#             print("Opção inválida. Por favor, escolha 1 para se esgueirar pelas cadeiras ou 2 para fugir pela janela.")

# def igreja_armado():
#     print("\nAo matar o zumbi, você encontra uma arma de fogo com 7 balas.")
    
    
#     while True:
#         print("\nOpções:")
#         print("1. Pegar a arma e avançar para fora da igreja")
#         print("2. Deixar a arma e avançar para fora da igreja")

#         escolha = input("O que você deseja fazer? Escolha 1 ou 2: ")

#         if escolha == "1":
#             print("\nVocê pega a arma de fogo. Pode ser útil para enfrentar ameaças mais perigosas.")
#             print("\nVocê encontra uma porta dos fundos na igreja, e decide avançar para não arriscar a vida com os zumbis na rua.")
#             print("Você segue pela escuridão até chegar a uma fazenda à noite.")
#             print("Na fazenda, você avista um celeiro à distância.")
#             fazenda_celeiro()
#             break
#         elif escolha == "2":
#             print("\nVocê decide deixar a arma de fogo e avança para fora da igreja.")
            
#             print("Você segue pela escuridão até chegar a uma fazenda à noite.")
            
#             print("Na fazenda, você avista um celeiro à distância.")
#             fazenda_celeiro()
#             break
#         else:
#             print("Opção inválida. Por favor, escolha 1 para pegar a arma ou 2 para avançar para fora da igreja.")

# def fazenda_celeiro():
#     print("\nVocê avança em direção ao celeiro e percebe que há um carro estacionado lá dentro.")
    

#     while True:
#         print("\nOpções:")
#         print("1. Avançar para pegar o carro")
#         print("2. Explorar a fazenda antes de pegar o carro")

#         escolha = input("O que você deseja fazer? Escolha 1 ou 2: ")

#         if escolha == "1":
#             print("\nVocê decide avançar para pegar o carro no celeiro.")
#             pegar_carro()
#             break
#         elif escolha == "2":
#             print("\nVocê decide explorar a fazenda antes de pegar o carro.")
#             explorar_fazenda()
#             break
#         else:
#             print("Opção inválida. Por favor, escolha 1 para avançar para pegar o carro ou 2 para explorar a fazenda.")

# def pegar_carro():
#     print("\nVocê entra no celeiro e encontra um carro em boas condições.")
#     print("Ao se aproximar do carro, você ouve um som estranho vindo de dentro do celeiro.")
#     print("Curioso, você decide investigar e descobre um zumbi gigante chorando no interior do celeiro.")
    
#     while True:
#         print("\nOpções:")
#         print("1. Sair do celeiro")
#         print("2. Ir para o carro")

#         escolha = input("O que você deseja fazer? Escolha 1 ou 2: ")

#         if escolha == "1":
#             print("\nVocê decide sair do celeiro e reconsiderar a situação do lado de fora.")
#             explorar_fazenda()
#             break
#         elif escolha == "2":
#             print("\nVocê decide ir para o carro e tentar ignorar o zumbi gigante chorando.")
#             tentar_ignorar_zumbi()
#             break
#         else:
#             print("Opção inválida. Por favor, escolha 1 para sair do celeiro ou 2 para ir para o carro.")

# def tentar_ignorar_zumbi():
#     print("\nVocê entra no carro e tenta ignorar o zumbi gigante chorando no celeiro.")
#     print("O som é perturbador, mas ao tentar dar partida, você percebe que o carro está sem gasolina.")
#     print("O zumbi gigante, ao ouvir o barulho do carro, se levanta e o segue.")
#     print("Ele alcança você, puxa-o para fora do carro e joga-o para fora do celeiro.")
#     fugir_para_milharal()

# def fugir_para_milharal():
#     print("\nVocê se vê fora do celeiro e decide correr para o milharal nas proximidades, tentando despistar o zumbi gigante.")
#     print("Você se embrenha entre as fileiras de milho, tentando manter-se fora do alcance do zumbi.")
#     print("\nNo milharal, um zumbi rastejante surge e agarra sua perna, fazendo você cair.")
#     print("O zumbi chorador de antes continua a perseguição, se aproximando rapidamente.")

#     while True:
#         print("\nOpções:")
#         print("1. Chutar o zumbi rastejante")
#         print("2. Atirar no zumbi rastejante (caso tenha a arma)")

#         escolha = input("O que você deseja fazer? Escolha 1 ou 2: ")

#         if escolha == "1":
#             print("\nVocê decide chutar o zumbi rastejante, mas o zumbi rastejante te morde, só soltando após dar um segundo chute")
#             death_by_bite()
#             break
#         elif escolha == "2":
#             print("\nVocê decide atirar no zumbi rastejante usando a arma que pegou antes.")
#             atirar_zumbi_rastejante()
#             break
#         else:
#             print("Opção inválida. Por favor, escolha 1 para chutar o zumbi ou 2 para atirar (caso tenha a arma).")

# def atirar_zumbi_rastejante():
#     print("\nVocê atira no zumbi rastejante, neutralizando a ameaça temporariamente.")
#     continuar_fugindo_milharal()

# def continuar_fugindo_milharal():
#     print("\nVocê se levanta rapidamente e continua a correr pelo milharal, tentando despistar o zumbi chorador.")
#     print("\nAo sair do milharal, você se encontra à beira de um rio. Do lado oposto, avista um barco a motor.")
    

#     while True:
#         print("\nOpções:")
#         print("1. Pular e nadar até o outro lado do rio")
#         print("2. Correr até o barco a motor")

#         escolha = input("O que você deseja fazer? Escolha 1 ou 2: ")

#         if escolha == "1":
#             print("\nVocê decide pular no rio e nadar até o outro lado, evitando o barco.")
#             nadar_rio()
#             break
#         elif escolha == "2":
#             print("\nVocê decide correr até o barco a motor, esperando que seja sua rota de fuga.")
#             correr_ate_barco()
#             break
#         else:
#             print("Opção inválida. Por favor, escolha 1 para pular no rio ou 2 para correr até o barco.")

# def nadar_rio():
#     print("\nVocê pula no rio e começa a nadar vigorosamente até o outro lado.")
#     print("Ao alcançar a margem oposta, você se afasta do rio, olhando para trás para verificar se o zumbi chorador te seguiu.")
#     death_by_drowning()

# def correr_ate_barco():
#     print("\nVocê corre em direção ao barco a motor, esperando alcançá-lo antes que o zumbi chorador chegue até você.")
#     print("Ao chegar ao barco, você se depara com uma cena angustiante: uma família dilacerada pelos zumbis.")
#     print("Você também encontra uma mala próxima ao barco.")

#     verificar_mala_barco()

# def verificar_mala_barco():
#     print("\nVocê decide verificar a mala e encontra:")
#     print("- Uma metralhadora")
#     print("- 2 bandagens")
#     print("- Um molotov")
    
#     print("\nEnquanto examina os itens, percebe que o zumbi chorador está se aproximando rapidamente.")

#     while True:
#         print("\nOpções:")
#         print("1. Jogar o molotov no zumbi")
#         print("2. Atirar no zumbi com a metralhadora")
#         print("3. Atirar no zumbi com a pistola")
#         print("4. Tentar correr e ligar o barco")
#         print("5. Usar uma bandagem para se curar")

#         escolha = input("O que você deseja fazer? Escolha 1, 2, 3, 4 ou 5: ")

#         if escolha == "1":
#             print("\nVocê decide jogar o molotov no zumbi chorador.")
#             jogar_molotov()
#             break
#         elif escolha == "2":
#             print("\nVocê decide atirar no zumbi com a metralhadora.")
#             atirar_metralhadora()
#             break
#         elif escolha == "3":
#             print("\nVocê decide atirar no zumbi com a pistola.")
#             atirar_pistola()
#             break
#         elif escolha == "4":
#             print("\nVocê decide tentar correr e ligar o barco.")
#             correr_ligar_barco()
#             break
#         elif escolha == "5":
#             print("\nVocê decide usar uma bandagem para se curar.")
#             usar_bandagem()
#             break
#         else:
#             print("Opção inválida. Escolha 1, 2, 3, 4 ou 5.")

# def jogar_molotov():
#     print("\nVocê joga o molotov no zumbi chorador, criando uma explosão de chamas.")
#     print("O zumbi é consumido pelas chamas e mas não é abatido, agora ele corre atrás de você pegando fogo.")
    
#     correr_ligar_barco()

# def atirar_metralhadora():
#     print("\nVocê dispara a metralhadora contra o zumbi chorador, acertando vários tiros.")
#     print("O zumbi e cai no chão, mas não está morto")
    
#     correr_ligar_barco_zumbi_caido()


# def atirar_pistola():
#     print("\nVocê atira no zumbi chorador com a pistola, acertando alguns tiros.")
#     print("O zumbi é atingido, mas continua se aproximando.")
    
#     correr_ligar_barco()

# def correr_ligar_barco():
#     print("\nVocê tenta correr até o barco para ligá-lo, mas o zumbi chorador está muito próximo.")
#     print("Antes que você alcance o barco, o zumbi agarra você, impedindo sua fuga.")


# def usar_bandagem():
#     print("\nVocê usa uma bandagem para se curar rapidamente.")
#     print("Enquanto se cura, o zumbi chorador se aproxima, mas o zumbi agarra você, impedindo você se curar..")

# def correr_ligar_barco_zumbi_caido():
#     print("\nVocê tenta correr até o barco para ligá-lo, mas o zumbi chorador está muito próximo.")
#     print("Mas com ele quase o alcançando-o, você consegue dar partida, saindo dali rapidamente.")
#     print("Agora você o deixa em um horizonte distante enquanto escapa")

# def explorar_fazenda():
#     print("\nVocê decide explorar a fazenda antes de pegar o carro.")
#     print("\nEm um galpão, você encontra um galão de gasolina.")
    

#     while True:
#         print("\nOpções:")
#         print("1. Pegar o galão de gasolina")
#         print("2. Deixar o galão de gasolina e continuar explorando")

#         escolha = input("O que você deseja fazer? Escolha 1 ou 2: ")

#         if escolha == "1":
#             print("\nVocê decide pegar o galão de gasolina. Pode ser útil para abastecer o carro.")
#             pegar_galao_gasolina()
#             break
#         elif escolha == "2":
#             print("\nVocê decide deixar o galão de gasolina e continuar explorando a fazenda.")
#             continuar_explorando_sem_gasolina()
#             break
#         else:
#             print("Opção inválida. Por favor, escolha 1 para pegar o galão de gasolina ou 2 para continuar explorando.")

# def pegar_galao_gasolina():
#     print("\nVocê pega o galão de gasolina. Agora, você tem um meio de abastecer o carro.")
    

# def continuar_explorando_sem_gasolina():
#     print("\nVocê decide deixar o galão de gasolina e continua explorando a fazenda.")
#     pegar_carro()


# def pegar_carro_com_gasolina():
#     print("\nVocê volta ao celeiro com o carro em boas condições.")
#     print("Fazendo o mínimo de barulho possível, você coloca a gasolina no tanque.")
#     print("Você entra no carro de fininho e dar partida, mas a partida chama a atenção do zumbi chorador no ceileiro")
#     print("Entretando, você acelera no desespero o deixando para traz e saindo daquela situação")


# # -------------------------------- Mortes ----------------------------------------
# def death_by_running():
#     print("\nInfelizmente, ao tentar correr, o zumbi te alcança e te captura.")
#     print("Você é incapaz de escapar, e o zumbi, com sede de carne humana, te devora.")
#     print("Game over. Sua jornada chegou ao fim. O apocalipse zumbi é impiedoso.")
#     exit()

# def death_by_corage():
#     print("Infelizmente, os zumbis são muitos e te cercam. Você não consegue escapar.")
#     print("Game over. Sua jornada chegou ao fim. O apocalipse zumbi é impiedoso.")
#     exit()

# def death_by_bite():
#     print("Após ser mordido você começa a passar mal rapidamente.")
#     print("Olha para o seu braço e está começando a se transformar.")
#     print("Sua consciência é tomada pela sede de sangue agora...")
#     print("Game over. Sua jornada chegou ao fim. O apocalipse zumbi é impiedoso.")
#     exit()

# def death_by_drowning():
#     print("Você tenta nadar até o outro lado do rio, mas está cansado demais para isso.")
#     print("Logo percebe que não vai conseguir, aceitando lentamente seu destino final.")
#     print("Em pouco tempo, lembra dos momentos felizes que viveu e de todas as decisões até aquele momento.")
#     print("Deixando o lado tomar seu corpo como seu, o levando para o fundo...")
#     print("Game over. Sua jornada chegou ao fim. O apocalipse zumbi é impiedoso.")
#     exit()