import bs4
from bs4 import BeautifulSoup

with open('datas/sample02.html') as fp:
    soup = BeautifulSoup(fp, features='lxml')
    body_tag = soup.body
    bodychildren = soup.body.children
    print(type(bodychildren), len(list(bodychildren)))

    print("--------------------------------------------")

    for child in body_tag.children:
        print(type(child), repr(child))   #returns a printable representation

    print("--------------------------------------------")

    title_tag = soup.title
    print(title_tag.parent, title_tag.string.parent)
    link = soup.a
    print(type(link.parents), len(list(link.parents)))
    for parent in link.parents:
        print(type(parent.name), parent.name)