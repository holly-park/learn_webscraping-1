import bs4
from bs4 import BeautifulSoup

print("html.parser: ", BeautifulSoup("<a><b/></a>", "html.parser"))
print("html.parser: ", BeautifulSoup("<a></p>", "html.parser"))
print("xml: ", BeautifulSoup("<a><b/></a>", "xml"))
print("lxml: ", BeautifulSoup("<a><b/></a>", "lxml"))
print("lxml: ", BeautifulSoup("<head/><a></p>", "lxml"))
print("html5lib: ", BeautifulSoup("<head/><a></p>", "html5lib"))