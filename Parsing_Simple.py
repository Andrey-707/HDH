# Простой пимер Парсинга Сайта.
# На примере stopgame.ru -> Статьи -> ОБЗОРЫ ИГР С ОЦЕНКОЙ «ИЗУМИТЕЛЬНО»
from colorama import init, Fore, Back, Style
import requests
from bs4 import BeautifulSoup as BS

init()

print(Fore.WHITE)
print("Program start")

print(Fore.YELLOW)
page = 1

while True:
    r = requests.get("https://stopgame.ru/review/new/izumitelno/p" + str(page))
    html = BS(r.content, 'html.parser')
    items  = html.select(".items > .article-summary")

    if(len(items)):
        for el in items:
            title = el.select('.caption > a')
            print( title[0].text )
        page += 1
    else:
        break

print(Fore.WHITE)
print("Program finish")

input()
