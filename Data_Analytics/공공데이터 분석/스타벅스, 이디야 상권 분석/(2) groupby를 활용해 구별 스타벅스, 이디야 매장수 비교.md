
# **구별 스타벅스, 이디야 매장수 비교**


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
    스타벅스세종로점             1
    스타벅스논현힐탑             1
    스타벅스연신내역             1
    스타벅스조선호텔후문           1
    스타벅스잠실대교남단점          1
    스타벅스역삼역점             1
    스타벅스역삼럭키점            1
    스타벅스석촌호수점            1
    스타벅스황학사거리점           1
    스타벅스명동미래             1
    스타벅스구로하이엔드점          1
    스타벅스삼청동점             1
    스타벅스신촌명물거리점          1
    스타벅스을지로센타            1
    스타벅스이수역사거리점          1
    스타벅스홍대삼거리점           1
    스타벅스문정역점             1
    스타벅스이태원거리점           1
    스타벅스연신내역점            1
    스타벅스서울대입구역점          1
    스타벅스송파사거리점           1
    스타벅스가락시장역점           1
    스타벅스연세백양로점           1
    스타벅스상암DMC센트럴몰점       1
    스타벅스광장점              1
    스타벅스종로2가점            1
    스타벅스서교점              1
    스타벅스광화문점             1
    스타벅스연희DT점            1
                      ... 
    스타벅스코엑스사거리점          1
    스타벅스영등포신길DT점         1
    스타벅스커피가산브이타워         1
    스타벅스올림픽공원북문점         1
    스타벅스숙대입구역점           1
    스타벅스압구정로데오역          1
    스타벅스강북구청사거리점         1
    스타벅스둔촌동점             1
    스타벅스가산디지털단지점         1
    스타벅스청담사거리점           1
    스타벅스마포일진빌딩점          1
    스타벅스강남삼성타운점          1
    스타벅스서울중앙우체국점         1
    스타벅스삼성도심공항점          1
    스타벅스현대디큐브B2점         1
    스타벅스마포이마트점           1
    스타벅스역점               1
    스타벅스새문안로점            1
    스타벅스송파구청점            1
    스타벅스남산스테이트           1
    스타벅스압구정로데오역점         1
    스타벅스월계이마트점           1
    스타벅스화곡동점             1
    스타벅스경희대삼거리점          1
    스타벅스예술의전당점           1
    스타벅스서울교대점            1
    스타벅스경복아파트점           1
    STARBUCKSCOFFEE      1
    스타벅스한성대입구역점          1
    스타벅스광운대점             1
    Name: 상호명, Length: 204, dtype: int64




```python
# 이디야만 출력
df_seoul[df_seoul['상호명'].str.contains('ediya|EDIYA|이디야')].shape
df_seoul.loc[df_seoul['상호명'].str.contains('ediya|EDIYA|이디야'), '상호명'].value_counts()
```




    이디야커피                  337
    EDIYACOFFEE              7
    이디야마들역                   2
    이디야에스프레소                 2
    이디야커피신금호역점               2
    이디야커피정릉아리랑점              1
    마스터키이디야마곡나루역점            1
    이디야커피용두점                 1
    이디야커피은행나무사거리점            1
    이디야커피사당역점                1
    이디야커피오류북부역점              1
    이디야커피수유역점                1
    이디야커피관악농협하나로마트점          1
    이디야신사역                   1
    이디야커피텐즈힐점                1
    이디야커피연구소                 1
    이디야커피한강공원로점              1
    이디야잠실                    1
    이디야커피위례아이파크점             1
    이디야커피한성대역점2층             1
    이디야노원사거리                 1
    이디야커피대방역점                1
    이디야커피도봉산역사점              1
    이디야커피응봉동점                1
    이디야문래씨지브이                1
    이디야커피한강진역사점한강진역사점        1
    이디야커피태평로점                1
    이디야IBK고객센터               1
    이디야커피신림남부초교점             1
    이디야구로에이스                 1
                          ... 
    이디야커피양재AT점               1
    이디야커피신당중앙점               1
    이디야커피신길썬프라자점             1
    이디야커피방학사거리점              1
    이디야커피삼성봉은사로점             1
    이디야커피우장산동점               1
    이디야커피광산사거리점              1
    이디야커피김안과점                1
    이디야커피중계롯데우성점중계롯데우성점      1
    엠케이이디야마곡나루역점             1
    이디야커피송파잠실점               1
    이디야커피창신중앙점               1
    이디야커피면목본동점               1
    이디야커피문정현대시티몰점            1
    이디야커피동묘역점                1
    이디야커피중곡대원점               1
    이디야커피마장동점                1
    이디야서대문점2호                1
    이디야커피가좌역점                1
    부일이디야커피                  1
    이디야커피문정엠스테이트점            1
    을지사거리이디야커피숍              1
    이디야커피봉천중앙점               1
    이디야커피세광교회점               1
    이디야커피롯데마트구로점             1
    이디야커피보라매중앙점              1
    이디야커피돈암아리랑점              1
    이디야커피망우점                 1
    이디야커피봉천역점                1
    이디야커피마곡엠밸리점              1
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



---
* **시각화**
    * **position = 'dodge'가 있을 때**
    * **position = 'dodge'를 활용하면 개별 데이터를 비교하기에 적합한 형태로 시각화**


```python
(ggplot(df_cafe_brand)
+ aes(x = '구', y = '매장수', fill = '브랜드명')
+ geom_bar(stat = 'identity', position = 'dodge')
+ ggtitle('구별 스타벅스 / 이디야 매장수')
+ theme(text = element_text(family = 'NanumGothic'),
       axis_text_x = element_text(rotation = 60),
       figure_size = (8, 4))
)
```


![png](output_14_0.png)





    <ggplot: (168267840008)>



* **시각화**
    * **position = 'dodge'가 없을 때**
    * **position = 'dodge'가 없으면 개별 데이터를 합쳐서 전체를 분석하기 적합한 형태로 시각화**


```python
(ggplot(df_cafe_brand)
+ aes(x = '구', y = '매장수', fill = '브랜드명')
+ geom_bar(stat = 'identity')
+ ggtitle('구별 스타벅스 / 이디야 매장수')
+ theme(text = element_text(family = 'NanumGothic'),
       axis_text_x = element_text(rotation = 60),
       figure_size = (8, 4))
)
```


![png](output_16_0.png)





    <ggplot: (168267846920)>


