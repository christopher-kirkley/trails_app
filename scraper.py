import requests
from bs4 import BeautifulSoup

# Config
base_url = 'https://www.oregonhikers.org'

# # Address to scrape
# url = 'https://www.oregonhikers.org/field_guide/Category:Family_Hikes'
# r = requests.get(url)


# # Error check.
# if r.status_code != 200:
#     print('Error!')
# else:
#     pass

# soup = BeautifulSoup(r.text)
# soup = soup.find_all('table')[3]

# l = []
# for link in soup.find_all('a'):
#     dict = {}
#     if link.get('href'):
#         dict['name'] = link.get('title')
#         dict['link'] = base_url + link.get('href')
#         l.append(dict)

url = 'https://www.oregonhikers.org/w/index.php?title=Special:Ask&limit=250&q=%5B%5BCategory%3APortland+Area%5D%5D%5B%5BCategory%3AEasy+Hikes%5D%5D%5B%5BCategory%3AFamily+Hikes%5D%5D&p=format%3Dbroadtable&po=%3FDifficulty%0A%3FDistance%0A%3FElevation+gain%0A&sort=&order=ASC'

r = requests.get(url)

# Error check.
if r.status_code != 200:
    print('Error!')
else:
    pass

soup = BeautifulSoup(r.text)
soup = soup.find_all('table')[3]

l = []
for link in soup.find_all('tr'):
    for item in link.find_all('td'):
        dict = {}
        dict['name'] = link.find('a').get('title')
        dict['link'] = link.find('a').get('href')
        if item.get('class'):
            item_name = item.get('class')[0]
            dict[item_name] = item.text
        l.append(dict)
