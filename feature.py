import bs4

print(bs4.__version__)

from bs4 import BeautifulSoup
s_html = '<html><head></head><body>Sacr&eacute; blue!</body></html>'
soup = BeautifulSoup(s_html, 'html.parser')
print(type(soup), soup)
