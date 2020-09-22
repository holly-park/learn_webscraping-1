import requests

#url='http://blog.naver.com/otter35'
url='https://www.coupang.com/'

header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
#https://www.whatismybrowser.com/detect/what-is-my-user-agent

res=requests.get(url=url, headers=header)
print(type(res), res)

print(res.status_code)
if(res.status_code == 200):
    with open('./datas/response02.html', 'w') as fp:
        fp.write(res.text)
