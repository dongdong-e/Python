
# **GeoJSON을 활용하여 구별로 스타벅스, 이디야 매장 합계 표현**


```python
import warnings
warnings.filterwarnings('ignore')
```


```python
import pandas as pd
import numpy as np
from plotnine import *
import folium
```


```python
import matplotlib
import matplotlib.font_manager as fm
from matplotlib import rc
fm.get_fontconfig_fonts()

font_location = 'C:/Windows/Fonts/NanumGothic.ttf'
font_name = fm.FontProperties(fname = font_location, size = 50).get_name()
matplotlib.rc('font', family = font_name)
```


```python
shop_2018 = pd.read_csv('shop_201806_01.csv', encoding = 'cp949', engine = 'python')
df_seoul = shop_2018[shop_2018['시도명'].str.startswith('서울')].copy()
```

---
* **데이터 전처리**


```python
# 스타벅스만 출력
df_seoul[df_seoul['상호명'].str.contains('스타벅스|starbucks|STARBUCKS')].shape
df_seoul.loc[df_seoul['상호명'].str.contains('스타벅스|starbucks|STARBUCKS'), '상호명'].value_counts()
```




    스타벅스            235
    스타벅스중구저동점         1
    스타벅스숭실대점          1
    스타벅스역삼역점          1
    스타벅스석촌역           1
    스타벅스이수역사거리점       1
    스타벅스잠실점           1
    스타벅스구로하이엔드점       1
    스타벅스숙대입구역점        1
    스타벅스논현힐탑          1
    스타벅스구로디지털로점       1
    스타벅스중랑역점          1
    스타벅스숭실대입구역점       1
    스타벅스용산역점          1
    스타벅스서울중앙우체국점      1
    스타벅스종각점           1
    스타벅스교대역점          1
    스타벅스월계이마트점        1
    스타벅스중랑구청점         1
    스타벅스송파방이DT점       1
    스타벅스종암점           1
    스타벅스가산디지털단지점      1
    스타벅스명지대점          1
    스타벅스경복궁역          1
    스타벅스마포이마트점        1
    스타벅스구산역점          1
    스타벅스종로평창          1
    스타벅스문정역점          1
    스타벅스현대디큐브B2점      1
    스타벅스신천역점          1
                   ... 
    스타벅스오목교역점         1
    스타벅스신설동역점         1
    스타벅스연신내역점         1
    스타벅스커피마포염리        1
    스타벅스서초파라곤점        1
    스타벅스이수역점          1
    스타벅스종로관수점         1
    스타벅스커피홍대역         1
    스타벅스청담사거리점        1
    스타벅스충정타워          1
    스타벅스미아사거리역점       1
    스타벅스홍대삼거리점        1
    스타벅스삼성도심공항점       1
    스타벅스선정릉역점         1
    스타벅스커피강남대로신사      1
    스타벅스광장점           1
    스타벅스청계산입구역점       1
    스타벅스사당로데오점        1
    스타벅스명동길점          1
    스타벅스건국클래식점        1
    스타벅스삼성교점          1
    스타벅스올림픽공원북문점      1
    스타벅스W-MALL점       1
    스타벅스합정점           1
    스타벅스연희DT점         1
    스타벅스커리학동사거리점      1
    스타벅스강동역점          1
    스타벅스고대프라자점        1
    스타벅스목동5단지점        1
    스타벅스방화DT          1
    Name: 상호명, Length: 204, dtype: int64




```python
# 이디야만 출력
df_seoul[df_seoul['상호명'].str.contains('ediya|EDIYA|이디야')].shape
df_seoul.loc[df_seoul['상호명'].str.contains('ediya|EDIYA|이디야'), '상호명'].value_counts()
```




    이디야커피              337
    EDIYACOFFEE          7
    이디야에스프레소             2
    이디야마들역               2
    이디야커피신금호역점           2
    이디야커피오류북부역점          1
    이디야커피동묘역점            1
    이디야커피신길썬프라자점         1
    이디야커피중곡대원점           1
    이디야구로에이스             1
    이디야커피논골사거리점          1
    이디야커피가좌역점            1
    이디야커피마곡엠밸리점          1
    EDIYACOFFEESHOP      1
    이디야커피연구소             1
    이디야커피을지로역점           1
    이디야커피신도림테크노마트        1
    이디야커피마장동점            1
    이디야커피송파잠실점           1
    이디야커피봉천중앙점           1
    이디야커피신림문화교점          1
    이디야커피도봉산역사점          1
    이디야커피애오개역점           1
    이디야커피응봉동점            1
    이디야커피점               1
    ediyacoffee          1
    이디야커피우장산동점           1
    이디야커피롯데마트구로점         1
    이디야역삼플래티넘            1
    이디야커피마곡역점            1
                      ... 
    이디야신사역               1
    이디야커피김안과점            1
    이디야커피중계중앙점           1
    이디야커피방학사거리점          1
    이디야커피청계천점            1
    이디야커피전농뉴타운점          1
    이디야커피성동구청점           1
    이디야화곡사거리             1
    EDIYA카페              1
    이디야커피창신중앙점           1
    이디야문래씨지브이            1
    이디야커피수유역점            1
    이디야커피은행나무사거리점        1
    을지사거리이디야커피숍          1
    이디야커피한성대역점2층         1
    이디야커피종합운동장역점         1
    이디야당산                1
    이디야커피삼성봉은사로점         1
    이디야서대문점2호            1
    이디야커피대방역점            1
    서아이디야                1
    마스터키이디야마곡나루역점        1
    이디야커피돈암아리랑점          1
    이디야커피봉천역점            1
    이디야커피화곡남부시장점         1
    이디야커피등촌동점            1
    이디야커피한강공원로점          1
    이디야커피문정엠스테이트점        1
    이디야커피관악농협하나로마트점      1
    이디야을지로3가             1
    Name: 상호명, Length: 107, dtype: int64




```python
# 스타벅스, 이디야 데이터 합치기
df_cafe = df_seoul[df_seoul['상호명'].str.contains('스타벅스|starbucks|STARBUCKS|ediya|EDIYA|이디야')]
```


```python
# df_cafe에 '브랜드명'이라는 컬럼 추가하기
df_cafe['브랜드명'] = ''
df_cafe.loc[df_cafe['상호명'].str.contains('스타벅스|starbucks|STARBUCKS'), '브랜드명'] = '스타벅스'
df_cafe.loc[~df_cafe['상호명'].str.contains('스타벅스|starbucks|STARBUCKS'), '브랜드명'] = '이디야'
```

---
* **구별 브랜드별 점포수**


```python
pd.DataFrame(df_cafe.groupby(['시군구명', '브랜드명'])['상호명'].count())
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>상호명</th>
    </tr>
    <tr>
      <th>시군구명</th>
      <th>브랜드명</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">강남구</th>
      <th>스타벅스</th>
      <td>69</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>32</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">강동구</th>
      <th>스타벅스</th>
      <td>10</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>12</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">강북구</th>
      <th>스타벅스</th>
      <td>5</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>12</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">강서구</th>
      <th>스타벅스</th>
      <td>14</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>34</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">관악구</th>
      <th>스타벅스</th>
      <td>9</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>23</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">광진구</th>
      <th>스타벅스</th>
      <td>14</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>13</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">구로구</th>
      <th>스타벅스</th>
      <td>11</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>21</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">금천구</th>
      <th>스타벅스</th>
      <td>9</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>10</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">노원구</th>
      <th>스타벅스</th>
      <td>9</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>30</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">도봉구</th>
      <th>스타벅스</th>
      <td>1</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>9</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">동대문구</th>
      <th>스타벅스</th>
      <td>8</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>18</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">동작구</th>
      <th>스타벅스</th>
      <td>7</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>10</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">마포구</th>
      <th>스타벅스</th>
      <td>29</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>20</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">서대문구</th>
      <th>스타벅스</th>
      <td>17</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>11</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">서초구</th>
      <th>스타벅스</th>
      <td>43</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>19</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">성동구</th>
      <th>스타벅스</th>
      <td>6</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>17</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">성북구</th>
      <th>스타벅스</th>
      <td>13</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>21</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">송파구</th>
      <th>스타벅스</th>
      <td>26</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>28</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">양천구</th>
      <th>스타벅스</th>
      <td>9</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>16</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">영등포구</th>
      <th>스타벅스</th>
      <td>26</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>25</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">용산구</th>
      <th>스타벅스</th>
      <td>17</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>10</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">은평구</th>
      <th>스타벅스</th>
      <td>9</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>19</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">종로구</th>
      <th>스타벅스</th>
      <td>28</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>14</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">중구</th>
      <th>스타벅스</th>
      <td>43</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>20</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">중랑구</th>
      <th>스타벅스</th>
      <td>6</td>
    </tr>
    <tr>
      <th>이디야</th>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_cafe_brand = pd.DataFrame(
    df_cafe.groupby(['시군구명', '브랜드명'])['상호명'].count()
).reset_index()
df_cafe_brand.columns = ['구', '브랜드명', '매장수']
df_cafe_brand
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구</th>
      <th>브랜드명</th>
      <th>매장수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강남구</td>
      <td>스타벅스</td>
      <td>69</td>
    </tr>
    <tr>
      <th>1</th>
      <td>강남구</td>
      <td>이디야</td>
      <td>32</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강동구</td>
      <td>스타벅스</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>강동구</td>
      <td>이디야</td>
      <td>12</td>
    </tr>
    <tr>
      <th>4</th>
      <td>강북구</td>
      <td>스타벅스</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>강북구</td>
      <td>이디야</td>
      <td>12</td>
    </tr>
    <tr>
      <th>6</th>
      <td>강서구</td>
      <td>스타벅스</td>
      <td>14</td>
    </tr>
    <tr>
      <th>7</th>
      <td>강서구</td>
      <td>이디야</td>
      <td>34</td>
    </tr>
    <tr>
      <th>8</th>
      <td>관악구</td>
      <td>스타벅스</td>
      <td>9</td>
    </tr>
    <tr>
      <th>9</th>
      <td>관악구</td>
      <td>이디야</td>
      <td>23</td>
    </tr>
    <tr>
      <th>10</th>
      <td>광진구</td>
      <td>스타벅스</td>
      <td>14</td>
    </tr>
    <tr>
      <th>11</th>
      <td>광진구</td>
      <td>이디야</td>
      <td>13</td>
    </tr>
    <tr>
      <th>12</th>
      <td>구로구</td>
      <td>스타벅스</td>
      <td>11</td>
    </tr>
    <tr>
      <th>13</th>
      <td>구로구</td>
      <td>이디야</td>
      <td>21</td>
    </tr>
    <tr>
      <th>14</th>
      <td>금천구</td>
      <td>스타벅스</td>
      <td>9</td>
    </tr>
    <tr>
      <th>15</th>
      <td>금천구</td>
      <td>이디야</td>
      <td>10</td>
    </tr>
    <tr>
      <th>16</th>
      <td>노원구</td>
      <td>스타벅스</td>
      <td>9</td>
    </tr>
    <tr>
      <th>17</th>
      <td>노원구</td>
      <td>이디야</td>
      <td>30</td>
    </tr>
    <tr>
      <th>18</th>
      <td>도봉구</td>
      <td>스타벅스</td>
      <td>1</td>
    </tr>
    <tr>
      <th>19</th>
      <td>도봉구</td>
      <td>이디야</td>
      <td>9</td>
    </tr>
    <tr>
      <th>20</th>
      <td>동대문구</td>
      <td>스타벅스</td>
      <td>8</td>
    </tr>
    <tr>
      <th>21</th>
      <td>동대문구</td>
      <td>이디야</td>
      <td>18</td>
    </tr>
    <tr>
      <th>22</th>
      <td>동작구</td>
      <td>스타벅스</td>
      <td>7</td>
    </tr>
    <tr>
      <th>23</th>
      <td>동작구</td>
      <td>이디야</td>
      <td>10</td>
    </tr>
    <tr>
      <th>24</th>
      <td>마포구</td>
      <td>스타벅스</td>
      <td>29</td>
    </tr>
    <tr>
      <th>25</th>
      <td>마포구</td>
      <td>이디야</td>
      <td>20</td>
    </tr>
    <tr>
      <th>26</th>
      <td>서대문구</td>
      <td>스타벅스</td>
      <td>17</td>
    </tr>
    <tr>
      <th>27</th>
      <td>서대문구</td>
      <td>이디야</td>
      <td>11</td>
    </tr>
    <tr>
      <th>28</th>
      <td>서초구</td>
      <td>스타벅스</td>
      <td>43</td>
    </tr>
    <tr>
      <th>29</th>
      <td>서초구</td>
      <td>이디야</td>
      <td>19</td>
    </tr>
    <tr>
      <th>30</th>
      <td>성동구</td>
      <td>스타벅스</td>
      <td>6</td>
    </tr>
    <tr>
      <th>31</th>
      <td>성동구</td>
      <td>이디야</td>
      <td>17</td>
    </tr>
    <tr>
      <th>32</th>
      <td>성북구</td>
      <td>스타벅스</td>
      <td>13</td>
    </tr>
    <tr>
      <th>33</th>
      <td>성북구</td>
      <td>이디야</td>
      <td>21</td>
    </tr>
    <tr>
      <th>34</th>
      <td>송파구</td>
      <td>스타벅스</td>
      <td>26</td>
    </tr>
    <tr>
      <th>35</th>
      <td>송파구</td>
      <td>이디야</td>
      <td>28</td>
    </tr>
    <tr>
      <th>36</th>
      <td>양천구</td>
      <td>스타벅스</td>
      <td>9</td>
    </tr>
    <tr>
      <th>37</th>
      <td>양천구</td>
      <td>이디야</td>
      <td>16</td>
    </tr>
    <tr>
      <th>38</th>
      <td>영등포구</td>
      <td>스타벅스</td>
      <td>26</td>
    </tr>
    <tr>
      <th>39</th>
      <td>영등포구</td>
      <td>이디야</td>
      <td>25</td>
    </tr>
    <tr>
      <th>40</th>
      <td>용산구</td>
      <td>스타벅스</td>
      <td>17</td>
    </tr>
    <tr>
      <th>41</th>
      <td>용산구</td>
      <td>이디야</td>
      <td>10</td>
    </tr>
    <tr>
      <th>42</th>
      <td>은평구</td>
      <td>스타벅스</td>
      <td>9</td>
    </tr>
    <tr>
      <th>43</th>
      <td>은평구</td>
      <td>이디야</td>
      <td>19</td>
    </tr>
    <tr>
      <th>44</th>
      <td>종로구</td>
      <td>스타벅스</td>
      <td>28</td>
    </tr>
    <tr>
      <th>45</th>
      <td>종로구</td>
      <td>이디야</td>
      <td>14</td>
    </tr>
    <tr>
      <th>46</th>
      <td>중구</td>
      <td>스타벅스</td>
      <td>43</td>
    </tr>
    <tr>
      <th>47</th>
      <td>중구</td>
      <td>이디야</td>
      <td>20</td>
    </tr>
    <tr>
      <th>48</th>
      <td>중랑구</td>
      <td>스타벅스</td>
      <td>6</td>
    </tr>
    <tr>
      <th>49</th>
      <td>중랑구</td>
      <td>이디야</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_cafe_gu = pd.DataFrame(df_cafe.groupby(['시군구명'])['상호명'].count())
```

---
## **choropleth 그리기**

* **구별로 매장수를 표현하기 위해 GeoJSON 파일 로드**
* **파일출처 : southkorea/seoul-maps: Seoul administrative divisions in ESRI Shapefile, GeoJSON and TopoJSON formats.**


```python
import json

geo_path = 'seoul_municipalities_geo_simple.json'
geo_json = json.load(open(geo_path, encoding = 'utf-8'))
```

* **서울 각 구별 스타벅스 / 이디야 매장 총합 시각화**


```python
geo_df = df_cafe
map = folium.Map(location = [geo_df['위도'].mean(), geo_df['경도'].mean()],
                zoom_start = 12)

map.choropleth(geo_data = geo_json,
              data = df_cafe_gu['상호명'],
               columns = [df_cafe_gu.index, df_cafe_gu['상호명']],
               key_on = 'feature.properties.name',
               fill_color = 'Purples',
               fill_opacity = 0.6,
               line_opacity = 0.5
              )
```
![image](https://user-images.githubusercontent.com/42408554/55055322-ff073880-50a5-11e9-8f75-2d8a4c2fa401.png)

* **서울 각 구별 스타벅스 / 이디야 매장 총합 시각화 + folium.CircleMarker 함께 표시하기**


```python


map = folium.Map(location = [geo_df['위도'].mean(), geo_df['경도'].mean()],
                zoom_start = 12)

map.choropleth(geo_data = geo_json,
              data = df_cafe_gu['상호명'],
               columns = [df_cafe_gu.index, df_cafe_gu['상호명']],
               key_on = 'feature.properties.name',
               fill_color = 'Purples',
               fill_opacity = 0.6,
               line_opacity = 0.5
              )

for n in geo_df.index:
    # 팝업에 들어갈 텍스트를 지정
    popup_name = geo_df.loc[n, '상호명'] + ' - ' + geo_df.loc[n, '도로명주소']
    # 브랜드명에 따라 아이콘 색상 지정
    if geo_df.loc[n, '브랜드명'] == '스타벅스':
        icon_color = 'green'
    else:
        icon_color = 'blue'
    
    folium.CircleMarker(
        location = [geo_df.loc[n, '위도'], geo_df.loc[n, '경도']],
        radius = 3,
        popup = popup_name,
        color = icon_color,
        fill = True,
        fill_color = icon_color
    ).add_to(map)
```
![image](https://user-images.githubusercontent.com/42408554/55055346-09c1cd80-50a6-11e9-923a-7a27da23e1f8.png)

---

### **스타벅스와 이디야 개별 분석**
* **https://colorbrewer2.org/**

* **(1) 스타벅스 매장 분포**


```python
df_cafe_s = df_cafe[df_cafe['브랜드명'] == '스타벅스']
df_cafe_starbucks = pd.DataFrame(df_cafe_s.groupby(['시군구명'])['상호명'].count())
df_cafe_starbucks.columns = ['매장수']
df_cafe_starbucks.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>매장수</th>
    </tr>
    <tr>
      <th>시군구명</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>69</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>10</td>
    </tr>
    <tr>
      <th>강북구</th>
      <td>5</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>14</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
map = folium.Map(location = [geo_df['위도'].mean(), geo_df['경도'].mean()],
                zoom_start = 12, tiles = 'Stamen Toner')

map.choropleth(geo_data = geo_json,
              data = df_cafe_starbucks['매장수'],
               columns = [df_cafe_starbucks.index, df_cafe_starbucks['매장수']],
               key_on = 'feature.properties.name',
               fill_color = 'YlGn',
               fill_opacity = 0.6,
               line_opacity = 0.7
              )

for n in geo_df.index:
    # 팝업에 들어갈 텍스트 지정
    popup_name = geo_df.loc[n, '상호명'] + ' - ' + geo_df.loc[n, '도로명주소']
    # 브랜드명에 따라 아이콘 색상 다르게 지정
    if geo_df.loc[n, '브랜드명'] == '스타벅스':
        icon_color = 'green'
    
        folium.CircleMarker(
            location = [geo_df.loc[n, '위도'], geo_df.loc[n, '경도']],
            radius = 3,
            popup = popup_name,
            color = icon_color,
            fill = True,
            fill_color = icon_color
        ).add_to(map)
```
![image](https://user-images.githubusercontent.com/42408554/55055367-180fe980-50a6-11e9-8b26-1d89d00a414b.png)

* **(2) 이디야 매장 분포**


```python
df_cafe_e = df_cafe[df_cafe['브랜드명'] == '이디야']
df_cafe_ediya = pd.DataFrame(df_cafe_e.groupby(['시군구명'])['상호명'].count())
df_cafe_ediya.columns = ['매장수']
df_cafe_ediya.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>매장수</th>
    </tr>
    <tr>
      <th>시군구명</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>32</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>12</td>
    </tr>
    <tr>
      <th>강북구</th>
      <td>12</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>34</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>23</td>
    </tr>
  </tbody>
</table>
</div>




```python
map = folium.Map(location = [geo_df['위도'].mean(), geo_df['경도'].mean()],
                zoom_start = 12, tiles = 'Stamen Toner')

map.choropleth(geo_data = geo_json,
              data = df_cafe_ediya['매장수'],
               columns = [df_cafe_ediya.index, df_cafe_ediya['매장수']],
               key_on = 'feature.properties.name',
               fill_color = 'Blues',
               fill_opacity = 0.6,
               line_opacity = 0.7
              )

for n in geo_df.index:
    # 팝업에 들어갈 텍스트 지정
    popup_name = geo_df.loc[n, '상호명'] + ' - ' + geo_df.loc[n, '도로명주소']
    # 브랜드명에 따라 아이콘 색상 다르게 지정
    if geo_df.loc[n, '브랜드명'] == '이디야':
        icon_color = 'blue'
    
        folium.CircleMarker(
            location = [geo_df.loc[n, '위도'], geo_df.loc[n, '경도']],
            radius = 3,
            popup = popup_name,
            color = icon_color,
            fill = True,
            fill_color = icon_color
        ).add_to(map)
```
![image](https://user-images.githubusercontent.com/42408554/55055383-20682480-50a6-11e9-9cce-65599a751bd6.png)
