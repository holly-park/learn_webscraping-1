import bs4
from bs4 import BeautifulSoup

with open('datas/sample02.html') as fp:
    soup = BeautifulSoup(fp, features='lxml')
    print(type(soup.title), soup.title)
    print(type(soup.title.string), soup.title.string)
    print(type(soup.p), soup.p)
    elementTag = soup.p
    print(type(elementTag.b), elementTag.b)
    print(type(soup.a), soup.a)
    print(type(soup.p['class']), soup.p['class'])
    