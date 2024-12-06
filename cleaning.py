def clear_pgn(PGN):
    import re

    moves = re.sub(r'\s*\{\[%clk.*?\]\}', '', PGN) # Remove marcações de tempo
    moves = re.sub(r'\[[^\]]*\]', '', moves) # Remove metadados

    moves = moves.strip()  # apaga espaços em branco nos lindes da string

    moves = re.sub(r'\d+\.\s*', '', moves) # Remove as enumerações dos lances
    moves = moves.replace(" ..", "")  # apaga o restante pertencente às enumerações dos ""

    moves = moves.replace(" ", ", ")  # separa ordenando os lances com vírgulas
    return moves