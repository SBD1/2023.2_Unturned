# import time
from Database import DataBase
from commands import Commands
from classes import Mortes
import psycopg2

conn = psycopg2.connect(
    host="172.23.0.2",           
    database="unturned",     
    user="postgres",             
    password="postgres"
)

cur = conn.cursor()

global name

def russia():
    global name
    print("Vamos criar seu personagem!")
    name = input("Escolha o nome do seu personagem: ")
    DataBase.create_new_pc(conn, 1, 1, name, 100, 100)
    DataBase.inserir_inventario(conn, cur)
    DataBase.select_mapa_descricao(conn, cur)
    cidade_arruinada()

def cidade_arruinada():
    DataBase.select_sala_descricao(conn, cur, nome="cidade_arruinada")
    
    while True:
        print("\nOpções:")
        print("Fugir. Sair correndo")
        print("Lutar. Enfrentar o zumbi")

        escolha = input("Digite sua escolha: ").lower()

        if escolha == 'fugir':
            print("Você decide correr para evitar o confronto imediato.")
            print("Você corre desesperadamente e encontra uma casa próxima para se esconder.")
            casa_abandonada()

        elif escolha == 'lutar':
            print("Você decide enfrentar o zumbi. Prepare-se para o combate!")
            print("Após uma luta árdua, você consegue derrotar o zumbi.")
            print("O zumbi dropa um item: uma faca.")
            print("\nOpções:")
            print("Pegar. Sair correndo")
            print("Deixar. Enfrentar o zumbi")

            escolha = input("O que você deseja fazer? Digite 'ajuda' para ver os comandos\n").lower()

            if escolha == 'pegar':
                DataBase.update_arma_branca(connection=conn,id=1, sala=1,inventario=1, nome="faca", dano=15, material="ferro")
                casa_abandonada_com_faca()

            elif escolha == 'deixar':
                casa_abandonada()

        elif escolha == 'ajuda':
            Commands.ajuda(escolha)
        
        elif escolha == 'sair':
            Commands.ajuda(escolha)
        
        else:
            print("Opção inválida.")
            

def casa_abandonada():
    DataBase.select_sala_descricao(conn, cur, nome="casa_abandonada")
    DataBase.update_pc(conn, 1, 2, name, 100, 50)
    
    while True:
        print("\nOpções:")
        print("Fugir. Sair correndo da casa")
        print("Voltar. Voltar para a rua onde encontrou o primeiro zumbi")

        escolha = input("Digite sua escolha: ").lower()

        if escolha == 'fugir':
            print("Você decide sair correndo da casa, mas o zumbi te alcança e captura.")
            DataBase.update_pc(conn, 1, 2, name, 0, 50)
            Mortes.death_by_running()

        elif escolha == 'voltar':
            cidade_arruinada()

        elif escolha == 'ajuda':
            Commands.ajuda(escolha)
        
        elif escolha == 'sair':
            Commands.ajuda(escolha)
        
        else:
            print("Opção inválida.")


def casa_abandonada_com_faca():
    DataBase.select_sala_descricao(conn, cur, nome="casa_abandonada")
    DataBase.update_pc(conn, 1, 3, name, 100, 50)

    while True:
        print("\nOpções:")
        print("lutar. Enfrentar o zumbi")
        print("fugir. Sair correndo para a rua")

        escolha = input("Digite sua escolha: ").lower()

        if escolha == 'fugir':
            print("Você decide sair correndo da casa, mas o zumbi te alcança e captura.")
            Mortes.death_by_running()
            DataBase.update_pc(conn, 1, 2, name, 0, 50)

        elif escolha == 'lutar':
            print("\nVocê decide enfrentar o zumbi dentro da casa.")
            print("Com a faca em mãos, você consegue derrotar o zumbi.")
            casa_abandonada_exploracao()

        elif escolha == 'ajuda':
            Commands.ajuda(escolha)
        
        elif escolha == 'sair':
            Commands.ajuda(escolha)
        
        else:
            print("Opção inválida.")
    

def casa_abandonada_exploracao():
    DataBase.select_sala_descricao(conn, cur, nome="casa_abandonada")

    while True:
        print("\nOpções:")
        print("Pegar. Pegar os itens e avançar")
        print("Fugir. Não pegar os itens e avançar para a rua")

        escolha = input("Digite sua escolha: ").lower()

        if escolha == 'pegar':
            print("\nVocê decide pegar os itens. Quem sabe eles possam ajudar na sua jornada.")
            print("\nVocê pegou uma corda e um isqueiro")
            DataBase.update_ferramenta(connection=conn, id = 1, sala = 1, inventario = 1, durabilidade = 100, nome = 'corda')
            DataBase.update_ferramenta(connection=conn, id = 3, sala = 1, inventario = 1, durabilidade = 90, nome = 'isqueiro')
            rua_deserta()
            DataBase.update_pc(conn, 1, 3, name, 0, 50)

        elif escolha == 'fugir':
            print("\nVocê decide não pegar os itens e avança para a rua.")
            rua_deserta()

        elif escolha == 'ajuda':
            Commands.ajuda(escolha)
        
        elif escolha == 'sair':
            Commands.ajuda(escolha)
        
        else:
            print("Opção inválida.")


def rua_deserta():
    DataBase.select_sala_descricao(conn, cur, nome="rua_deserta")

    while True:
        print("\nOpções:")
        print("Lutar. Enfrentar os zumbis")
        print("Fugir. Correr para dentro da igreja")

        escolha = input("Digite sua escolha: ").lower()

        if escolha == 'lutar':
            print("\nVocê decide enfrentar os três zumbis. Uma escolha ousada, mas arriscada.")
            Mortes.death_by_corage()  

        elif escolha == 'fugir':
            print("\nVocê decide correr para dentro da igreja, dividindo os zumbis.")
            igreja()
            DataBase.update_pc(conn, 1, 4, name, 0, 50)

        elif escolha == 'ajuda':
            Commands.ajuda(escolha)
        
        elif escolha == 'sair':
            Commands.ajuda(escolha)
        
        else:
            print("Opção inválida.")


def igreja():
    DataBase.select_sala_descricao(conn, cur, nome="igreja")

    while True:
        print("\nOpções:")
        print("Lutar. Se esgueirar pelas cadeiras e matar o zumbi pelas costas")
        print("Fugir. Fugir pela janela da igreja")

        escolha = input("Digite sua escolha: ").lower()

        if escolha == 'lutar':
            print("\nVocê decide se esgueirar pelas cadeiras, se aproximar do zumbi e atacar pelas costas.")
            print("Com um golpe certeiro, você mata o zumbi sem chamar a atenção.")
            igreja_armado() 

        elif escolha == 'fugir':
            print("\nVocê decide fugir pela janela da igreja, criando uma rota alternativa.")
            print("Você consegue escapar pela janela e encontra uma rota diferente, evitando os outros zumbis na rua.")
            fazenda_celeiro()
            DataBase.update_pc(conn, 1, 5, name, 0, 50)

        elif escolha == 'ajuda':
            Commands.ajuda(escolha)
        
        elif escolha == 'sair':
            Commands.ajuda(escolha)
        
        else:
            print("Opção inválida.")
    

def igreja_armado():
    while True:
        print("\nOpções:")
        print("Pegar. Pegar a arma e avançar para fora da igreja")
        print("Fugir. Deixar a arma e avançar para fora da igreja")

        escolha = input("Digite sua escolha: ").lower()

        if escolha == 'pegar':
            print("\nVocê pega a arma de fogo. Pode ser útil para enfrentar ameaças mais perigosas.")
            DataBase.update_arma_fogo(id=4, sala='NULL', inventario=1, nome="pistola", dano=45, distancia=15, capacidadeMunicao=8)
            print("\nVocê encontra uma porta dos fundos na igreja, e decide avançar para não arriscar a vida com os zumbis na rua.")
            print("Você segue pela escuridão até chegar a uma fazenda à noite.")
            print("Na fazenda, você avista um celeiro à distância.")
            fazenda_celeiro() 

        elif escolha == 'fugir':
            print("\nVocê decide deixar a arma de fogo e avança para fora da igreja.")
            print("Você segue pela escuridão até chegar a uma fazenda à noite.")
            print("Na fazenda, você avista um celeiro à distância.")
            fazenda_celeiro()
            DataBase.update_pc(conn, 1, 6, name, 0, 50)

        elif escolha == 'ajuda':
            Commands.ajuda(escolha)
        
        elif escolha == 'sair':
            Commands.ajuda(escolha)
        
        else:
            print("Opção inválida.")
    

def fazenda_celeiro():
    DataBase.select_sala_descricao(conn, cur, nome="fazenda_celeiro")

    while True:
        print("\nOpções:")
        print("Pegar. Avançar para pegar o carro")
        print("Fugir. Explorar a fazenda antes de pegar o carro")

        escolha = input("Digite sua escolha: ").lower()

        if escolha == 'pegar':
            print("\nVocê decide avançar para pegar o carro no celeiro.")
            pegar_carro() 

        elif escolha == 'fugir':
            print("\nVocê decide explorar a fazenda antes de pegar o carro.")
            explorar_fazenda()
            DataBase.update_pc(conn, 1, 7, name, 0, 50)

        elif escolha == 'ajuda':
            Commands.ajuda(escolha)
        
        elif escolha == 'sair':
            Commands.ajuda(escolha)
        
        else:
            print("Opção inválida.")
    

def pegar_carro():
    DataBase.select_sala_descricao(conn, cur, nome="pegar_carro")

    while True:
        print("\nOpções:")
        print("Voltar. Sair do celeiro")
        print("Pegar. Ir para o carro")

        escolha = input("Digite sua escolha: ").lower()

        if escolha == 'pegar':
            print("\nVocê decide ir para o carro e tentar ignorar o zumbi gigante chorando.")
            tentar_ignorar_zumbi()
            DataBase.update_pc(conn, 1, 8, name, 0, 50)

        elif escolha == 'voltar':
            print("\nVocê decide sair do celeiro e reconsiderar a situação do lado de fora.")
            explorar_fazenda()
            

        elif escolha == 'ajuda':
            Commands.ajuda(escolha)
        
        elif escolha == 'sair':
            Commands.ajuda(escolha)
        
        else:
            print("Opção inválida.")
    
def tentar_ignorar_zumbi():
    DataBase.select_sala_descricao(conn, cur, nome="tentar_ignorar_zumbi")
    fugir_para_milharal()

def fugir_para_milharal():
    DataBase.select_sala_descricao(conn, cur, nome="fugir_para_milharal")

    while True:
        print("\nOpções:")
        print("Lutar. Chutar o zumbi rastejante")
        print("Usar arma. Atirar no zumbi rastejante (caso tenha a arma)")

        escolha = input("Digite sua escolha: ").lower()

        if escolha == 'lutar':
            print("\nVocê decide chutar o zumbi rastejante, mas o zumbi rastejante te morde, só soltando após dar um segundo chute")
            Mortes.death_by_bite()

        elif escolha == 'usar arma':
            print("\nVocê decide atirar no zumbi rastejante usando a arma que pegou antes.")
            atirar_zumbi_rastejante()
            

        elif escolha == 'ajuda':
            Commands.ajuda(escolha)
        
        elif escolha == 'sair':
            Commands.ajuda(escolha)
        
        else:
            print("Opção inválida.")

def atirar_zumbi_rastejante():
    DataBase.select_sala_descricao(conn, cur, nome="atirar_zumbi_rastejante")
    continuar_fugindo_milharal()

def continuar_fugindo_milharal():
    DataBase.select_sala_descricao(conn, cur, nome="continuar_fugindo_milharal")
    
    while True:
        print("\nOpções:")
        print("Fugir. Pular e nadar até o outro lado do rio")
        print("Avançar. Correr até o barco a motor")

        escolha = input("Digite sua escolha: ").lower()

        if escolha == 'fugir':
            print("\nVocê decide pular no rio e nadar até o outro lado, evitando o barco.")
            nadar_rio()

        elif escolha == 'avançar':
            print("\nVocê decide correr até o barco a motor, esperando que seja sua rota de fuga.")
            correr_ate_barco()
            

        elif escolha == 'ajuda':
            Commands.ajuda(escolha)
        
        elif escolha == 'sair':
            Commands.ajuda(escolha)
        
        else:
            print("Opção inválida.")


def nadar_rio():
    DataBase.select_sala_descricao(conn, cur, nome="nadar_rio")
    Mortes.death_by_drowning()

def correr_ate_barco():
    DataBase.select_sala_descricao(conn, cur, nome="corre_ate_barco")
    verificar_mala_barco()

def verificar_mala_barco():
    print("\nVocê decide verificar a mala e encontra:")
    print("Uma metralhadora")
    print("2 bandagens")
    print("Um molotov")
    
    print("\nEnquanto examina os itens, percebe que o zumbi chorador está se aproximando rapidamente.")

    while True:
        print("\nOpções:")
        print("Usar <nome-arma>")
        print("Fugir - Tentar fugir para o barco")

        escolha = input("Digite sua escolha: ").lower()

        if escolha == "usar molotov":
            print("\nVocê decide jogar o molotov no zumbi chorador.")
            jogar_molotov()
            break
        elif escolha == "usar metralhadora":
            print("\nVocê decide atirar no zumbi com a metralhadora.")
            atirar_metralhadora()
            break
        elif escolha == "usar pistola":
            print("\nVocê decide atirar no zumbi com a pistola.")
            atirar_pistola()
            break
        elif escolha == "fugir":
            print("\nVocê decide tentar correr e ligar o barco.")
            correr_ligar_barco()
            break
        elif escolha == "usar bandagem":
            print("\nVocê decide usar uma bandagem para se curar.")
            usar_bandagem()
            break
            

        elif escolha == 'ajuda':
            Commands.ajuda(escolha)
        
        elif escolha == 'sair':
            Commands.ajuda(escolha)
        
        else:
            print("Opção inválida.")

def jogar_molotov():
    print("\nVocê joga o molotov no zumbi chorador, criando uma explosão de chamas.")
    print("O zumbi é consumido pelas chamas e mas não é abatido, agora ele corre atrás de você pegando fogo.")
    
    correr_ligar_barco()

def atirar_metralhadora():
    print("\nVocê dispara a metralhadora contra o zumbi chorador, acertando vários tiros.")
    print("O zumbi e cai no chão, mas não está morto")
    
    correr_ligar_barco_zumbi_caido()


def atirar_pistola():
    print("\nVocê atira no zumbi chorador com a pistola, acertando alguns tiros.")
    print("O zumbi é atingido, mas continua se aproximando.")
    
    correr_ligar_barco()

def correr_ligar_barco():
    DataBase.select_sala_descricao(conn, cur, nome="corre_ligar_barco")

def usar_bandagem():
    print("\nVocê usa uma bandagem para se curar rapidamente.")
    print("Enquanto se cura, o zumbi chorador se aproxima, mas o zumbi agarra você, impedindo você se curar..")

def correr_ligar_barco_zumbi_caido():
    print("\nVocê tenta correr até o barco para ligá-lo, mas o zumbi chorador está muito próximo.")
    print("Mas com ele quase o alcançando-o, você consegue dar partida, saindo dali rapidamente.")
    print("Agora você o deixa em um horizonte distante enquanto escapa")

def explorar_fazenda():
    DataBase.select_sala_descricao(conn, cur, nome="explorar_fazenda")

    while True:
        print("\nOpções:")
        print("Pegar - Pegar o galão de gasolina")
        print("Fugir - Deixar o galão de gasolina e continuar explorando")

        escolha = input("Digite sua escolha: ").lower()

        if escolha == "pegar":
            print("\nVocê decide pegar o galão de gasolina. Pode ser útil para abastecer o carro.")
            pegar_galao_gasolina()
            break
        elif escolha == "fugir":
            print("\nVocê decide deixar o galão de gasolina e continuar explorando a fazenda.")
            continuar_explorando_sem_gasolina()
            break
            

        elif escolha == 'ajuda':
            Commands.ajuda(escolha)
        
        elif escolha == 'sair':
            Commands.ajuda(escolha)
        
        else:
            print("Opção inválida.")
    

def pegar_galao_gasolina():
    print("\nVocê pega o galão de gasolina. Agora, você tem um meio de abastecer o carro.")
    

def continuar_explorando_sem_gasolina():
    print("\nVocê decide deixar o galão de gasolina e continua explorando a fazenda.")
    pegar_carro()


def pegar_carro_com_gasolina():
    DataBase.select_sala_descricao(conn, cur, nome="pegar_carro_com_gasolina")
