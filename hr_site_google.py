import requests
import pandas as pd
from bs4 import BeautifulSoup

# download hrsite
hrsite = "https://www.google.com/search?q=%EC%B7%A8%EC%97%85%EC%82%AC%EC%9D%B4%ED%8A%B8&rlz=1C1CHBD_koKR912KR912&oq=%EC%B7%A8%EC%97%85%EC%82%AC%EC%9D%B4%ED%8A%B8&aqs=chrome..69i57.2521j0j15&sourceid=chrome&ie=UTF-8"
result = requests.get(hrsite)

# if successful parse the download into a BeautifulSoup object, which allows easy manipulation 
if result.status_code == 200:
    soup = BeautifulSoup(result.content, "html.parser")
    div_tag = soup.select('div')
    # divchildren = soup.div.children
    # print(type(divchildren), len(list(divchildren)))
    print(div_tag[30])
    for i in range(30,60):
        for link in div_tag[i]:
            print(type(link),link)



    # for child in a_tag.children[16]:
    #     #print(type(child), repr(child))
    #     a_tag = soup.a
    #     achildren = soup.a.children
    #     print(type(achildren), len(list(achildren)))
