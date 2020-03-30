import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

song_list=soup.select('table.list-wrap>tbody>tr>td.info')
rank=1
for song in song_list:
    title_name=song.select('a.title.ellipsis')
    artist_name=song.select('a.artist.ellipsis')
    title=title_name[0].text.strip()
    artist=artist_name[0].text
    print(rank, title, '-' , artist)
    rank+=1