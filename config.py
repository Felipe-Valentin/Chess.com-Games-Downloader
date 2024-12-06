def settings():

    # Usuário do Chess.com à ter suas partidas baixadas
    username = 'lpsupi'  # nome de membro
    # Padrão: 'lpsupi'
    
    # Período entre datas, que o Downloader alcançará
    initial_year, final_year = 2024, 2013  # ano inicial e final
    # Padrão: 2024, 2013
    initial_month = 11  # mês inicial
    # Padrão: 11
    
    # Precisão mínima do vencedor, para que a partida seja baixada
    minimum_accuracy = 92.5  # porcentagem
    # Use 0 para baixar todas as partidas do jogador
    # Padrão: 92.5

    return username, initial_year, final_year, initial_month, minimum_accuracy