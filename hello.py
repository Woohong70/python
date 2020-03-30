import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movie_info=soup.select('table.list_ranking>tbody>tr')
rank=0
for movie in movie_info:
    title_el=movie.select('a')
    point_el=movie.select('td.point')
    if len(title_el)>0:
        rank+=1
        title=title_el[0].text
        point = point_el[0].text
        print(rank, title, point.strip())
