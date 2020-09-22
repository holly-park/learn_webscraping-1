import requests
import pandas as pd
from bs4 import BeautifulSoup

with open('datas/sample02.html') as fp:
    soup = BeautifulSoup(fp, features='lxml')
    print(type(soup.find(id="link3")), soup.find(id="link3"))
    print(type(soup.find_all(name='a')), soup.find_all(name='a'))
    print(type(soup.find_all(name='b')), soup.find_all(name='b'))
    print(type(soup.find_all(name=["a","b"])), soup.find_all(name=["a", "b"]))
    print(type(soup.find_all(id=True)), soup.find_all(id=True))
    find_attrs = soup.find_all(name='a', attrs={"href":True})
    print(type(find_attrs), find_attrs)
    find_attrs = soup.find_all(name='a', attrs={"class":'sister', 'id':['link2', 'link3']})
    print(type(find_attrs), find_attrs)

import re

result = soup.find_all(name=re.compile("^b"))   #re: regulation express: string에서 어떤 것을 찍을 때 사용하는 라이브러리 (b로 시작하는 태그들의 리스트)
print("-------------")
print(type(result), result)
for tag in result:
    print(type(tag), tag, type(tag.name), tag.name)
gettag = result[0].find_all('a')
print(type(gettag), gettag)
