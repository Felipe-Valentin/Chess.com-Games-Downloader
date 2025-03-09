def settings():


    #################################################
    #                                               #
    #               Configurações do                #
    #          Chess.com Games Downloader:          #
    #                                               #
    #################################################

    # Usuário do Chess.com à ter suas partidas baixadas
    username = 'lpsupi'  # nome de membro
    # Padrão: 'lpsupi'

    # Período entre datas, que o downloader alcançará
    initial_year, final_year = 2025, 2013  # ano inicial e final
    # Padrão: 2025, 2013
    initial_month = 2  # mês inicial
    # Padrão: 2

    # Precisão mínima do vencedor, para que a partida seja baixada
    minimum_accuracy = 92.5  # porcentagem
    # Use 0 para baixar todas as partidas do jogador
    # Padrão: 92.5


    return username, initial_year, final_year, initial_month, minimum_accuracy