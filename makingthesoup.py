import bs4
from bs4 import BeautifulSoup

path = './datas/sample01.html'
with open(path) as fp:
    soup = BeautifulSoup(fp, features='lxml')
    print(type(soup), soup)

import requests

res = requests.get('https://www.google.com/')
print(res.status_code, res.content)

soup = BeautifulSoup(res.content, features='lxml')
print(type(soup), soup.prettify())