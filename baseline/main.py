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
        global jogos_gratis
        global elements
        global precos_desconto
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

    
    def pesquisar_estatisticas_jogos():
        global porcentagem_positiva
        for i in range(len(jogos_gratis)):
            # Fazer pesquisa no google
            url_pesquisa = requests.get(f'https://www.google.com/search?q={jogos_gratis[i]}+steam')
            soup_pesquisa = BeautifulSoup(url_pesquisa.text, 'html.parser')

            # Achar todos os links e escolher apenas o primeiro
            links = soup_pesquisa.find_all('a', attrs={'data-ved': True})
            href = [link['href'] for link in links]
            href = href[3][7:]

            # Scrapping do site achado no google
            url_jogo = requests.get(str(href))
            soup_jogo = BeautifulSoup(url_jogo.text, 'html.parser')

            # Encontrar elemento para porcentagem estatística de aprovação
            status = soup_jogo.find_all('span', class_='responsive_reviewdesc_short')

            # Manipulação e Fatiamente de strings para extrair apenas o número
            porcentagem_positiva = status[0].text.replace('(', '').split()
            porcentagem_positiva = (int(porcentagem_positiva[0].replace('%', '')))

    def avaliar_jogo():
        #Avaliar se o jogo é bom com base na porcentagem positiva
        if porcentagem_positiva >= 80:
            print('Jogo Bom')
        elif porcentagem_positiva >= 50:
            print('Jogo Neutro')
        elif porcentagem_positiva < 50:
            print('Jogo Ruim')

    def ver_data_final():
        # Função para reconhecer o dia atual, e calcular quanto tempo falta até a promoção acabar

        datas = np.array([elements[i]['price']['lineOffers'] for i in range(len(elements))])
        datas = datas[np.where(precos_desconto == 0)]

        # Adicionando ao vetor 'data_final' os dados dentro do arquivo json

        data_final = [i['endDate'][:10] for data in datas for dat in data for i in dat['appliedRules']]
        data_final = datetime.strptime(data_final[0], '%Y-%m-%d')
        dias_restantes = data_final - datetime.now()

        print(f'Data Final: {data_final.date()}, Faltam {dias_restantes.days} dias')




Scrapper.obter_nomes()
Scrapper.pesquisar_estatisticas_jogos()
Scrapper.avaliar_jogo()
Scrapper.ver_data_final()