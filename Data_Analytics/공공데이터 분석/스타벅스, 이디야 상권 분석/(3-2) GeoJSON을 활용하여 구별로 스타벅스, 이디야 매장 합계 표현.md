
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




    스타벅스               235
    스타벅스약수역점             1
    스타벅스사당점              1
    스타벅스새문안로점            1
    스타벅스종로관수점            1
    스타벅스중랑역점             1
    스타벅스서강대흥역점           1
    스타벅스강남우성점            1
    스타벅스석촌호수점            1
    스타벅스차병원사거리점          1
    스타벅스황학사거리점           1
    스타벅스한남동점             1
    스타벅스마포트라팰점           1
    스타벅스서소문배재            1
    스타벅스신압구정점            1
    스타벅스잠실대교남단점          1
    STARBUCKSCOFFEE      1
    스타벅스종로3가점            1
    스타벅스중계역점             1
    스타벅스삼청동점             1
    스타벅스충정타워점            1
    스타벅스현대디큐브B2점         1
    스타벅스낙성대DT점           1
    스타벅스마포일진빌딩점          1
    스타벅스강남오거리점           1
    스타벅스서교점              1
    스타벅스상일동점             1
    스타벅스동교점              1
    스타벅스노원마들역점           1
    스타벅스을지로센타            1
                      ... 
    스타벅스광장점              1
    스타벅스외대정문점            1
    스타벅스종각점              1
    스타벅스광운대점             1
    스타벅스커피가산브이타워         1
    스타벅스세종로점             1
    스타벅스성신여대정문           1
    스타벅스청담영동대로점          1
    스타벅스신설동역점            1
    스타벅스명동메트로            1
    스타벅스마곡나루역점           1
    스타벅스커피가산그레이트         1
    스타벅스종로2가점            1
    스타벅스서울대역점            1
    스타벅스건국클래식점           1
    스타벅스구로에이스트윈타워1점      1
    스타벅스가든파이브            1
    스타벅스신세계본점            1
    스타벅스구로디지털로점          1
    스타벅스연세백양로점           1
    스타벅스대치은마사거리점         1
    스타벅스커피홍대역            1
    스타벅스역삼럭키점            1
    스타벅스강동역점             1
    스타벅스광화문역점            1
    스타벅스공덕               1
    스타벅스상암DMC센트럴몰점       1
    스타벅스양천향교역점           1
    스타벅스강북구청사거리점         1
    스타벅스명동입구점            1
    Name: 상호명, Length: 204, dtype: int64




```python
# 이디야만 출력
df_seoul[df_seoul['상호명'].str.contains('ediya|EDIYA|이디야')].shape
df_seoul.loc[df_seoul['상호명'].str.contains('ediya|EDIYA|이디야'), '상호명'].value_counts()
```




    이디야커피                337
    EDIYACOFFEE            7
    이디야커피신금호역점             2
    이디야에스프레소               2
    이디야마들역                 2
    이디야커피한강진역사점한강진역사점      1
    이디야커피논골사거리점            1
    이디야커피점                 1
    이디야커피마곡엠밸리점            1
    이디야커피위례아이파크점           1
    이디야서대문점2호              1
    이디야커피경희대점              1
    이디야커피일원동점              1
    이디야커피전농뉴타운점            1
    이디야커피가좌역점              1
    이디야커피용두점               1
    이디야커피신림미성점             1
    이디야커피천호현대점             1
    이디야커피도봉산역사점            1
    을지사거리이디야커피숍            1
    이디야커피연구소               1
    이디야커피중계중앙점             1
    이디야커피망우점               1
    이디야커피세광교회점             1
    이디야커피양재AT점             1
    이디야커피한강공원로점            1
    이디야커피돈암아리랑점            1
    이디야커피마곡역점              1
    이디야커피강남역지하상가점          1
    이디야커피을지로역점             1
                        ... 
    이디야커피봉천중앙점             1
    이디야커피봉천역점              1
    이디야커피송파잠실점             1
    이디야커피삼성봉은사로점           1
    이디야커피신당중앙점             1
    이디야카페                  1
    이디야구로에이스               1
    이디야커피응봉동점              1
    이디야커피동묘역점              1
    이디야문래씨지브이              1
    이디야커피영등포본동점            1
    마스터키이디야마곡나루역점          1
    이디야커피약수점               1
    이디야커피오류북부역점            1
    이디야커피청계천점              1
    이디야커피선정릉역점             1
    이디야커피은행나무사거리점          1
    이디야신사역                 1
    이디야커피태평로점              1
    이디야커피마포KCC점            1
    이디야당산                  1
    이디야커피낙원동점              1
    이디야커피사당역점              1
    이디야커피동소문동점             1
    이디야불광역                 1
    이디야커피개봉북부점             1
    이디야커피신도림테크노마트          1
    이디야잠실                  1
    이디야구로하이엔드              1
    ediyacoffee            1
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
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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

* **(2) 이디야 매장 분포**


```python
df_cafe_e = df_cafe[df_cafe['브랜드명'] == '이디야']
df_cafe_ediya = pd.DataFrame(df_cafe_e.groupby(['시군구명'])['상호명'].count())
df_cafe_ediya.columns = ['매장수']
df_cafe_ediya.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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

---

## **매장수 크기를 반영해 CircleMaker 그리기**
* **Pandas의 reshaping data 활용하기**


```python
df_cafe_brand.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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
  </tbody>
</table>
</div>




```python
df_cafe_brand_vs = df_cafe_brand.pivot_table(index = '구',
                                            columns = '브랜드명',
                                            values = '매장수')

df_cafe_brand_vs.columns = ['스타벅스', '이디야']
df_cafe_brand_vs.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>스타벅스</th>
      <th>이디야</th>
    </tr>
    <tr>
      <th>구</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>69</td>
      <td>32</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>10</td>
      <td>12</td>
    </tr>
    <tr>
      <th>강북구</th>
      <td>5</td>
      <td>12</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>14</td>
      <td>34</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>9</td>
      <td>23</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_cafe_brand_vs['매장수비교'] = df_cafe_brand_vs.apply( \
    lambda x: 1 if x['스타벅스'] > x['이디야'] else 0, axis = 1)

df_cafe_brand_vs.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>스타벅스</th>
      <th>이디야</th>
      <th>매장수비교</th>
    </tr>
    <tr>
      <th>구</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>69</td>
      <td>32</td>
      <td>1</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>10</td>
      <td>12</td>
      <td>0</td>
    </tr>
    <tr>
      <th>강북구</th>
      <td>5</td>
      <td>12</td>
      <td>0</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>14</td>
      <td>34</td>
      <td>0</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>9</td>
      <td>23</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# '위도', '경도' 컬럼 추가하기
lng_list = []
lat_list = []
for gu in df_cafe_brand_vs.index:
    lat = df_cafe.loc[df_cafe['시군구명'] == gu, '위도'].mean()
    lng = df_cafe.loc[df_cafe['시군구명'] == gu, '경도'].mean()
    lat_list.append(lat)
    lng_list.append(lng)

df_cafe_brand_vs['위도'] = lat_list
df_cafe_brand_vs['경도'] = lng_list
df_cafe_brand_vs.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>스타벅스</th>
      <th>이디야</th>
      <th>매장수비교</th>
      <th>위도</th>
      <th>경도</th>
    </tr>
    <tr>
      <th>구</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>69</td>
      <td>32</td>
      <td>1</td>
      <td>37.506968</td>
      <td>127.044551</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>10</td>
      <td>12</td>
      <td>0</td>
      <td>37.540750</td>
      <td>127.137271</td>
    </tr>
    <tr>
      <th>강북구</th>
      <td>5</td>
      <td>12</td>
      <td>0</td>
      <td>37.632347</td>
      <td>127.022071</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>14</td>
      <td>34</td>
      <td>0</td>
      <td>37.554969</td>
      <td>126.839652</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>9</td>
      <td>23</td>
      <td>0</td>
      <td>37.481530</td>
      <td>126.934320</td>
    </tr>
  </tbody>
</table>
</div>



---


```python
# CircleMarker의 radius 지정시 아래와 같은 타입오류가 발생하므로 float 타입으로 변경
# TypeError: Object of type 'int64' is not JSON serializable

df_cafe_brand_vs['스타벅스'] = df_cafe_brand_vs['스타벅스'].astype(float)
df_cafe_brand_vs['이디야'] = df_cafe_brand_vs['이디야'].astype(float)
```


```python
map.choropleth(geo_data = geo_json,
              data = df_cafe_brand_vs['매장수비교'],
              columns = [df_cafe_brand_vs.index,
                        df_cafe_brand_vs['매장수비교']],
               fill_color = 'BuGn',
               key_on = 'feature.properties.name',
               fill_opacity = 0.7,
               line_opacity = 0.2,
               highlight = True
              )

for gu in df_cafe_brand_vs.index:
    for cafe in ['스타벅스', '이디야']:
        
        cafe_count = df_cafe_brand_vs.loc[gu, cafe]
        msg = f'{gu} {cafe} 매장수 : {cafe_count:.0f}'
        
        icon_color = 'blue'
        if cafe == '스타벅스':
            icon_color = 'green'
            
        folium.CircleMarker(
            location = [df_cafe_brand_vs.loc[gu, '위도'],
                       df_cafe_brand_vs.loc[gu, '경도']],
            radius = cafe_count,
            color = icon_color,
            popup = msg,
            fill = True,
            fill_color = icon_color
        ).add_to(map)

map
```


```python

```
