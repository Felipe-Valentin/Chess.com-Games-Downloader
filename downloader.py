def download(username, year, month, minimum_accuracy):
    import urllib.request
    import json
    import re
    from time import sleep

    try:
        zero = "0" if month < 10 else ""  # arruma a sintaxe do URL, para acessar a API corretamente
    except TypeError as e:
        print('[ERRO] O mês inicial foi inserido entre aspas na "config.py", retire-as.')
        print(f'\n<DEPURAÇÃO CPython> {e}.')
        print('\n[NÓ FATAL] Encerrando a execução em 25 segundos...')
        sleep(25)  # adormece a rotina por 25 segundos
        exit() # Encerra a execução do programa
    link = f'https://api.chess.com/pub/player/{username}/games/{year}/{zero}{month}'  # endereço web para o JSON da API do Chess.com

    # Fazer requisição do JSON:
    try:
        with urllib.request.urlopen(link) as response:
            data = json.loads(response.read().decode()) # Coleta o conteúdo JSON
    except urllib.error.HTTPError as e:
        print('[ERRO] Verifique na "config.py" se o nome de membro, e/ou o período entre as\ndatas são válidos ao acessar a API.')
        print(f'\n<DEPURAÇÃO CPython> {e}.')
        print('\n[NÓ FATAL] Encerrando a execução em 40 segundos...')
        sleep(40)  # adormece a rotina por 40 segundos
        exit() # Encerra a execução do programa


    # Processar os dados coletados, partida por partida:
    output_data = [] # Cria a Lista de Retorno de Dados

    for game in data["games"]:
        output = []  # define uma Nova Lista de Dados, para o retorno de dados
        evaluated = True  # considera que a partida já foi revisada pelo Chess.com

        if minimum_accuracy > 0:
            # Resgatar os nomes dos usuários, e suas precisões:
            usernames = [ game["white"]["username"], game["black"]["username"] ]
            try:
                accuracies = [ game["accuracies"]["white"], game["accuracies"]["black"] ]

                # adicionar a precisão de uma partida vencida, à Nova Lista de Dados:
                if usernames[0].upper() == username.upper() and accuracies[0] >= accuracies[1] and accuracies[0] >= minimum_accuracy:
                    output.append(accuracies[0])  # salva a precisão jogada de brancas
                elif usernames[1].upper() == username.upper() and accuracies[1] >= accuracies[0] and accuracies[1] >= minimum_accuracy:
                    output.append(accuracies[1])  # salva a precisão "" de negras
                else:
                    evaluated = False  # identifica que o usuário alvo perdeu
            except Exception:
                evaluated = False  # identifica que a partida ainda não foi revisada pelo "", ou é inválida (falha da API)

        if evaluated:
            URL = game["url"] # Resgata o link da partida
            PGN = game["pgn"] # Resgata os lances da ""
            # Salva os dados de link e PGN:
            output.append(URL)
            output.append(PGN)

            output_data.append(output)  # adiciona todos os dados à Lista de Retorno de Dados
    return output_data