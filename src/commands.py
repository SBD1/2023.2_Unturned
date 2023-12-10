class Commands:
    def ajuda(input):
        if input == 'ajuda' or input == 'Ajuda':
            print('Comandos disponíveis')
            print('Fugir - Tenta correr para a próxima sala.')
            print('Lutar - Tenta matar o zumbi/animal')
            print('Pegar - Tenta pegar um item')
            print('Usar <nome-item> - Tenta usar um item')
            print('Combinar - Tenta criar um novo item')
            print('Inventário - Abre o inventário')
            print('Sair - Sai do jogo')

        elif input == 'sair' or input == 'Sair':
            print("\nVocê tem certeza?\n")
            print('1 - Sim')
            print('2 - Não')

            if input == 1:
                print('Você saiu do jogo')
                exit()
        