# 네이버 영화 제목과 평점 출력
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
import urllib.parse

jan = []
feb = []
for a in range(20190122, 20190132):
    jan.append(a)
for b in range(20190201, 20190222):
    feb.append(b)

total = jan + feb
movie = []

for date in total:
    url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date=%d" % date
    
    with urllib.request.urlopen(url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
    
    titles = (soup.find_all('div', {'class': 'tit5'}))
    ratings = (soup.find_all('td', {'class': 'point'}))
    
    for i in range(len(titles)):
        movie.append([titles[i].a.string, round(float(ratings[i].string), 2)])

df_movie = pd.DataFrame(movie, columns = ['title', 'rating'])


# 그래프로 표현하기

import matplotlib.pyplot as plt
plt.plot(df_movie.groupby('title')['rating'].mean())
plt.show()
