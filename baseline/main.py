import requests
import json
import numpy as np
import sqlite3 as sql
from datetime import datetime
from bs4 import BeautifulSoup

class Scrapper:
    def __init__(self) -> None:
        pass

    def obter_nomes():
        # Conseguir nome dos jogos na epic
        url = requests.get('https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=pt-BR&country=BR&allowCountries=BR')
        dados = str(url.text)

        # Transformar dados recebidos em json
        json1 = json.loads(dados)
        elements = json1['data']['Catalog']['searchStore']['elements']

        # Utilizar preço do desconto como parametro para dividir jogos gratis e jogos que são pagos que estão na lista
        precos_desconto = np.array([elements[i]['price']['totalPrice']['discountPrice'] for i in range(len(elements))])
        titulos = np.array([elements[i]['title'] for i in range(len(elements))])

        # Adicionar ao array 'Jogos Gratis' apenas os jogos que estiverem com o preço igual a 0
        jogos_gratis = titulos[np.where(precos_desconto == 0)]
        print(jogos_gratis)

Scrapper.obter_nomes()