class Commands:
    def ajuda(entrada):
        if entrada == 'ajuda' or entrada == 'Ajuda':
            print('Comandos disponíveis')
            print('Fugir - Tenta correr para a próxima sala.')
            print('Avançar - Tenta avançar')
            print('Lutar - Tenta matar o zumbi/animal')
            print('Pegar - Tenta pegar um item')
            print('Voltar - Volta para a sala anterior')
            print('Usar <nome-item> - Tenta usar um item')
            print('Combinar - Tenta criar um novo item')
            print('Inventário - Abre o inventário')
            print('Sair - Sai do jogo')

        elif entrada == 'sair' or entrada == 'Sair':
            while True:
                print("\nVocê tem certeza?\n")
                print('1 - Sim')
                print('2 - Não')

                escolha = input("Digite sua escolha: ").lower()

                if escolha == 'sim':
                    print('Você saiu do jogo')
                    exit()
                elif escolha == 'não':
                    break
                else:
                    print('Escolha inválida')
    
    def validar_comando(entrada):
        comandos_disponiveis = [
            'Fugir', 'Lutar', 'Pegar', 'Usar', 'Combinar', 'Inventário', 'Sair'
        ]

        comando_digitado = entrada

        if comando_digitado in comandos_disponiveis:
            return comando_digitado
        else:
            return 'Comando inválido'
