from urllib.request import urlopen
from bs4 import BeautifulSoup
url= "http://example.webscraping.com/places/default/index"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
# match = soup
# print(match)

for m in soup.findAll('td'):
    print('\n country name    :',end='')
    print(m.div.a.text)
    print('\n img url     :' ,end='')
    print((m.div.img)['src'])

