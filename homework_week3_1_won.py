import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')
rows = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for row in rows:
    titleName = row.select_one('td.check > input')['title']
    rank = row.select_one('td.number').text[0:2].strip()
    artist = row.select_one('td.info > a.artist.ellipsis').text
    print(f'{rank}.', titleName, f'- {artist}')


