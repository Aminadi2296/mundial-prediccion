from bs4 import BeautifulSoup
import requests
# import lxml
# import lxml.etree

years = [1930, 1934, 1938, 1942, 1948, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
         1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]

web = 'https://en.wikipedia.org/wiki/2014_FIFA_World_Cup'

response = requests.get(web)
content = response.text
soup = BeautifulSoup(content, 'xlml')
#encoding='utf-8' 

matches = soup.find_all('div', class_='footballbox')

for match in matches:
    print(match.find('th', class_='fhome').get_text())
    print(match.find('th', class_='fscore').get_text())
    print(match.find('th', class_='faway').get_text())