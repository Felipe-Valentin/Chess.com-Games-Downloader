from time import sleep
from os import path, makedirs

try:
    from config import settings
    username, initial_year, final_year, initial_month, minimum_accuracy = settings() # Resgata as especificações desejadas
except NameError as e:
        print('[ERRO] Alguma variável na "config.py", foi declarada sem as aspas.')
        print(f'\n<DEPURAÇÃO CPython> {e}.')
        print('\n[NÓ FATAL] Encerrando a execução em 25 segundos...')
        sleep(25)  # adormece a rotina por 25 segundos
        exit() # Encerra a execução do programa
except SyntaxError as e:
        print('[ERRO] Verifique na "config.py", se há algum zero antes dum valor, e/ou se está vazia alguma variável.')
        print(f'\n<DEPURAÇÃO CPython> {e}.')
        print('\n[NÓ FATAL] Encerrando a execução em 40 segundos...')
        sleep(40)  # adormece ""
        exit() # Encerra a execução do programa
if isinstance(minimum_accuracy, str):
    minimum_accuracy = float(minimum_accuracy) # Corrige a declaração da variável
if isinstance(initial_year, int) and isinstance(final_year, int):
    if final_year > initial_year:
        initial_year, final_year = final_year, initial_year # Corrige a inversão das variáveis

year, month = initial_year, initial_month # Define o começo do período de analíse

# Verificar se a pasta de saída não existe:
if not path.exists("Downloaded Games PGN"):
    makedirs("Downloaded Games PGN") # Cria a pasta de saída de dados


from downloader import download
while True:
    data = download(username, year, month, minimum_accuracy) # Obtém os dados das partidas

    for i in range(len(data)):
        if len(data[i]) == 3:
            PGN_index = 2  # índice do PGN enquanto houver revisão de precisões

            # Resgatar a precisão vencedora:
            accuracy = data[i][0]
            accuracy_string = f', {accuracy}% of accuracy.'  # define a oração gramatical da precisão

            game_ID = data[i][PGN_index-1].split('/')[-1] # Resgata o ID da partida
            output_file = f'Downloaded Games PGN/{accuracy}-{game_ID}.txt'
        else:
            PGN_index = 1  # índice do PGN se não houver revisão de ""
            accuracy_string = "."  # finaliza a oração gramatical
            game_ID = data[i][PGN_index-1].split('/')[-1] # Resgata o ""
            output_file = f'Downloaded Games PGN/{game_ID}.txt'

        from cleaning import clear_pgn
        PGN = clear_pgn(data[i][PGN_index])  # limpa o PGN para um formato melhor legível
        with open(output_file, "w") as output:
            print(f'[{game_ID}] game met specifications{accuracy_string}')
            output.write(PGN) # Armazena o PGN de uma partida

    month -= 1  # prepara o downloader para o próximo mês do período
    if month == 0:
        try:
            year -= 1  # prepara "" o próximo ano do ""
            if year == final_year-1:
                break # Termina o downloader
        except TypeError as e:
            print('\n\n[ERRO] Algum ano foi inserido entre aspas na "config.py", retire-as.')
            print(f'\n<DEPURAÇÃO CPython> {e}.')
            print('\n[NÓ FATAL] Encerrando a execução em 25 segundos...')
            sleep(25)  # adormece a rotina por 25 segundos
            exit() # Encerra a execução do programa
        month = 12 # Reseta o índice dos meses


print('\nAll possible games have been downloaded successfully!')
print('Closing the Downloader in 30 seconds...')
sleep(30)  # espera 30 segundos, antes de encerrar a execução
exit() # Encerra a execução do programa