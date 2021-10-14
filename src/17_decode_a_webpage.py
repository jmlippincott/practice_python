import requests
from bs4 import BeautifulSoup
import re

url = 'http://www.nytimes.com'
r = requests.get(url).text
soup = BeautifulSoup(r, features='lxml')

articles = []

for i in soup.find_all('a'):
    if re.search('2021', str(i)):
        articles.append(i.text)

for i in articles:
    print(i)