# Chess.com Games Downloader
> WARNING: this repository and everything included in it has no official connection to Chess.com, it is simply a tool for downloading games through the "[Published-Data API](https://support.chess.com/en/articles/9650547-published-data-api)" publicly released by Chess.com

<br/>

## Posso configurar o Downloader?
Para você baixar partidas específicas:

- Na "**config.py**", é possível configurar um "filtro de pesquisa". Você pode alterar de qual jogador vai baixar partidas (`username`), qual será o intervalo de tempo que o Downloader alcançará (`initial_year`, `final_year` e `initial_month`), e até uma precisão mínima para que o Downloader baixe uma partida (`minimum_accuracy`).

Veja como a **config.py** se parece:
```
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
```

<br/>

## Onde obtenho o "nome de membro" de um jogador?
Caso você esteja tentando baixar partidas de outro jogador, além do padrão (*lpsupi*) na **config.py**:

- Os jeitos mais fáceis de obter o "nome de membro" de um jogador, são através do link do perfil desse jogador no Chess.com, você deve encontrá-lo após o último separador "/" na URL. Também é visivelmente possível obtê-lo no título maior, ao lado da foto de perfil desse jogador, em cima do nome do proprietário desse perfil.

![Aonde obter o "nome de membro" de um jogador, no Chess.com](https://i.imgur.com/A1oeVkT.png)

<br/>

## Como ficam as partidas baixadas?
Caso você queira saber como é a formatação das partidas pelo Downloader:

- As partidas são salvas em tipo de arquivo `TXT`, em formato PGN (*Portable Game Notation*), de acordo com as preferências inseridas no módulo **config.py**, aonde serão armazenadas dentro de uma pasta chamada "*Downloaded Games PGN*". Será atribuido um nome único para cada arquivo de partida baixada, a partir da precisão de revisão pelo Chess.com, separada e seguida pelo ID da partida nos sistemas do Chess.com (`game/live` ou `game/daily`).

[Veja](https://www.chess.com/game/live/28590615399) como um PGN se parece:
```
e4, c5, Nf3, Nc6, d4, cxd4, Nxd4, Nf6, Nc3, e5, Ndb5, d6, Bg5, a6, Na3, b5, Nd5, Be7, Bxf6, Bxf6, c4, b4, Nc2, O-O, g3, a5, Bg2, Bg5, O-O, Be6, Qd3, Qb8, a3, b3, Nce3, Nd4, f4, Bd8, Kh1, f6, Nf5, Bb6, g4, Bc5, g5, fxg5, fxg5, Ra7, Nfe7+, Kh8, Rxf8+, Qxf8, Rf1, Qe8, Nf5, Rf7, Nxd4, Rxf1+, Bxf1, exd4, Nc7, Qf7, Nxe6, Qxe6, Qf3, Kg8, Bd3, Qf7, Kg2, Qg6, h4, Qf7, e5, dxe5, Bxh7+, Kf8, Bg6, Qxf3+, Kxf3, Ke7, Bd3, Ke6, h5, Be7, h6, gxh6, gxh6, Kf7, Ke4, Kg6, c5, Kxh6, c6, Bd8, Kxe5, Kg5, Kxd4, Kf4, Kc5, Ke3, Bc4, Kd2, Bxb3, Kc1, a4, Kxb2, Bc4, Bc7, Bb5, Kc3, Kd5, Kb4, Kd4, Bb6+, Ke5, Bc7+, Ke6, Kc5, Ke7, Kb6, Kd7, Bb8, Kc8, Bc7, Kd7, Bb8, Kd8, Bc7+, Kc8, Bh2, Kd7, Bc7, Ke6, Bh2, Kd5, Bc7, Ke6, Bb8, Kd7, Bc7, Ke6, 1/2-1/2
```

![Formatação do nome de partidas baixadas pelo Downloader](https://i.imgur.com/opZWc7G.png)

<br/>

> Please, note that the source code contained in this repository is only released for use under the "[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) [(Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International)](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.txt)" license.
