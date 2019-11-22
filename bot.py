from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import scrapy
import requests
from bs4 import BeautifulSoup

url = 'https://capricho.abril.com.br/moda/'

class bot(scrapy.Spider):


    #coletando os links
    link = 'https://capricho.abril.com.br/moda/'
    pagina = requests.get(link)
    # Criando objeto beautiful Soup
    soup = BeautifulSoup(pagina.text, "html.parser")
    count = 0
    posts = soup.find_all(class_='list-item-title')
    posts_info = soup.find_all(class_='list-date-description')

    lista = []
    for post in posts:
        links = [a['href'] for a in post.find_all('a', href=True)]
        for l in links:
            print(l)
            lista.append(l)
            # print(posts_info[count].getText())
            count = count + 1


    name = "capricho"
    start_urls = lista

    def parse(self, response):
        p = ''
        titulo = response.css('title::text')[0].extract()
        paragrafos = response.css('section.article-content p::text').extract()
        yield {'titulo': titulo}
        for paragrafo in paragrafos:
            p = p + paragrafo

        #yield {'paragrafo': p}

        print('o texto é:')
        print(p)




# def coletar(url):
#     '''----->alterar o caminho da pasta do chromedriver<-----'''
#     navegador = webdriver.Chrome(executable_path='chromedriver')
#
#     # abertura do navegador no link inserido na variável 'url'.
#     navegador.get(url)
#
#     print('passou')
#
# coletar(url)
