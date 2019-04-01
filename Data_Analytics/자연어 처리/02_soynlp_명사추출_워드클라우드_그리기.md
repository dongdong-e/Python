
# **자연어처리 시작하기**
* **soynlp로 토큰화하고 명사를 추출해 워드클라우드 그려보기**


```python
# 출력 데이터가 지저분하게 보이지 않도록
import warnings
warnings.filterwarnings('ignore')
```


```python
# soynlp 설치하기
!pip install soynlp
```


```python
import pandas as pd
from pandas.api.types import CategoricalDtype
import numpy as np
import re

import csv
import sys
import getpass

csv.field_size_limit(sys.maxsize)
```


```python
!pip install -U -q Pydrive

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

# Authenticate and create the PyDrive client.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)
```


```python
url = 'https://drive.google.com/open?id=1NS3tF09-0fRwTx8O8H5gY3oEqmpsOxYm'
id = url.split('=')[1]
```


```python
# 크롤링해 온 국민청원 데이터를 판다스로 읽어온다.
downloaded = drive.CreateFile({'id':id})
downloaded.GetContentFile('petition.csv')
df = pd.read_csv('petition.csv', index_col = 0, parse_dates = ['start', 'end'], engine = 'python')
```


```python
df.shape
```




    (377756, 7)




```python
df.head()
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
      <th>start</th>
      <th>end</th>
      <th>answered</th>
      <th>votes</th>
      <th>category</th>
      <th>title</th>
      <th>content</th>
    </tr>
    <tr>
      <th>article_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>21</th>
      <td>2017-08-19</td>
      <td>2017-11-17</td>
      <td>0</td>
      <td>9</td>
      <td>안전/환경</td>
      <td>스텔라 데이지호에 대한 제안입니다.</td>
      <td>스텔라 데이지호에 대한 제안입니다.\n3월31일 스텔라 데이지호가 침몰하고 5달째가...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2017-08-19</td>
      <td>2017-11-17</td>
      <td>0</td>
      <td>17</td>
      <td>기타</td>
      <td>비리제보처를 만들어주세요.</td>
      <td>현 정부에 국민들이 가장 원하는 것은 부패척결입니다.  우리 사회에 각종 비리들이 ...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2017-08-19</td>
      <td>2017-09-03</td>
      <td>0</td>
      <td>0</td>
      <td>미래</td>
      <td>제2의 개성공단</td>
      <td>만일 하시는 대통령님 및 각 부처 장관님,주무관님들 안녕하세요!!\n전남 목포에서 ...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2017-08-19</td>
      <td>2017-08-26</td>
      <td>0</td>
      <td>53</td>
      <td>일자리</td>
      <td>공공기관 무조건적인 정규직전환을 반대합니다.</td>
      <td>현정부에서 정규직 일자리를 늘리는 것에 찬성합니다. 그런데 공공기관 비정규직들은 인...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2017-08-19</td>
      <td>2017-09-03</td>
      <td>0</td>
      <td>0</td>
      <td>미래</td>
      <td>제2의 개성공단</td>
      <td>만일 하시는 대통령님 및 각 부처 장관님,주무관님들 안녕하세요!!\n전남 목포에서 ...</td>
    </tr>
  </tbody>
</table>
</div>




```python
p = r'.*(돌봄|육아|초등|보육).*'
care = df[df['title'].str.match(p) | 
            df['content'].str.match(p, flags = re.MULTILINE)]

care.shape
```




    (14960, 7)




```python
care.head(3)
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
      <th>start</th>
      <th>end</th>
      <th>answered</th>
      <th>votes</th>
      <th>category</th>
      <th>title</th>
      <th>content</th>
    </tr>
    <tr>
      <th>article_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>24</th>
      <td>2017-08-19</td>
      <td>2017-08-26</td>
      <td>0</td>
      <td>53</td>
      <td>일자리</td>
      <td>공공기관 무조건적인 정규직전환을 반대합니다.</td>
      <td>현정부에서 정규직 일자리를 늘리는 것에 찬성합니다. 그런데 공공기관 비정규직들은 인...</td>
    </tr>
    <tr>
      <th>36</th>
      <td>2017-08-19</td>
      <td>2017-08-26</td>
      <td>0</td>
      <td>1</td>
      <td>인권/성평등</td>
      <td>한국채식인구 100만명. 학교 급식 및 군대에서 현미채식 선택권을 보장해주십시오!</td>
      <td>문재인 대통령님과 각 정부 인사분들께 마음속 깊이 존경과 감사를 표합니다. 대한민국...</td>
    </tr>
    <tr>
      <th>45</th>
      <td>2017-08-19</td>
      <td>2017-11-17</td>
      <td>0</td>
      <td>0</td>
      <td>육아/교육</td>
      <td>초등학교 교사 임용 시험 관련 해결방안</td>
      <td>초등학교 교사 임용 시험을 수능 시험 처럼 전국 단위로 실시하고난 후에\n1지망 2...</td>
    </tr>
  </tbody>
</table>
</div>




```python
care.tail(3)
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
      <th>start</th>
      <th>end</th>
      <th>answered</th>
      <th>votes</th>
      <th>category</th>
      <th>title</th>
      <th>content</th>
    </tr>
    <tr>
      <th>article_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>491776</th>
      <td>2019-01-09</td>
      <td>2019-02-08</td>
      <td>0</td>
      <td>3</td>
      <td>일자리</td>
      <td>장애인 일자리를 지켜주세요</td>
      <td>제주에 사는 김응순입니다. 큰 딸 아이가 지적장애인 2급입니다. 요즘 나라에서 일자...</td>
    </tr>
    <tr>
      <th>491889</th>
      <td>2019-01-09</td>
      <td>2019-02-08</td>
      <td>0</td>
      <td>2</td>
      <td>기타</td>
      <td>회사발령을 반대합니다</td>
      <td>8살 남자아이를 키우고있는 엄마입니다\n몇일전 저희 신랑이 갑자기 부산에서 서울로 ...</td>
    </tr>
    <tr>
      <th>491966</th>
      <td>2019-01-09</td>
      <td>2019-02-08</td>
      <td>0</td>
      <td>0</td>
      <td>육아/교육</td>
      <td>문재인대통령님...고 김영옥 대령 교과서에 실어주세요~</td>
      <td>미국전쟁영웅이자 한국에서도 마찬가지로 영웅인분을 교과서에 실어서 기리면 좋겠습니다\...</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 샘플로 보고 싶은 인덱스 번호로 출력하기
sample_index = 24

sample_title = care.loc[sample_index, 'title']
sample_title
```




    '공공기관 무조건적인 정규직전환을 반대합니다.'




```python
sample_content = care.loc[sample_index, 'content']
sample_content
```




    '현정부에서 정규직 일자리를 늘리는 것에 찬성합니다. 그런데 공공기관 비정규직들은 인맥으로 들어온 경우가 많습니다. 자질이 안되는데도 정규직이 된다면 그 피해는 국민들에게 돌아갈것입니다. 현재 공공기관 정규직들은 100대1의 경쟁률을 뚫고 들어온 경우도 있습니다. 지금도 노량진에서 수많은 청춘들이 공부를 하고 있죠. 기존 비정규직들을 무조건적으로 무기직 전환한다면 또 다른 정유라 탄생이고 역차별입니다. 새로 필요로 하는 신규채용부터 공채절차를 거쳐 무기직 전환해야합니다. 예전에 공무원 기능직의 일반직 전환, 초등학교에 중초교사 임용 등이 그 예죠. 실제 일하는 곳에서는 그분들로 인한 업무처리 미흡으로 문제가 되고 있습니다. 사립학교는 인건비를 국가에서 주니 사립학교도 국가에서 공채해야 합니다. 부디 사례 하나하나를 보아가며 처리해주시고 전체 정규직 숫자 전환만 보며 공약실천을 무리하게 하지 말아주세요.  국민들은 정의로운 나라를 원합니다. 역차별이 아닌 공정한 채용이 되게 해주세요.'



## **토큰화 하기**
* **'토큰화'란 스페이스바(bar) 단위, 즉 띄어쓰기 단위로 단어를 리스트로 담아주는 과정**


```python
from soynlp.tokenizer import RegexTokenizer

tokenizer = RegexTokenizer()
tokenizer
```




    <soynlp.tokenizer._tokenizer.RegexTokenizer at 0x7f55f7123a20>




```python
tokened_title = tokenizer.tokenize(sample_title)
tokened_title
```




    ['공공기관', '무조건적인', '정규직전환을', '반대합니다', '.']




```python
tokened_content = tokenizer.tokenize(sample_content)
tokened_content
```




    ['현정부에서',
     '정규직',
     '일자리를',
     '늘리는',
     '것에',
     '찬성합니다',
     '.',
     '그런데',
     '공공기관',
     '비정규직들은',
     '인맥으로',
     '들어온',
     '경우가',
     '많습니다',
     '.',
     '자질이',
     '안되는데도',
     '정규직이',
     '된다면',
     '그',
     '피해는',
     '국민들에게',
     '돌아갈것입니다',
     '.',
     '현재',
     '공공기관',
     '정규직들은',
     '100',
     '대',
     '1',
     '의',
     '경쟁률을',
     '뚫고',
     '들어온',
     '경우도',
     '있습니다',
     '.',
     '지금도',
     '노량진에서',
     '수많은',
     '청춘들이',
     '공부를',
     '하고',
     '있죠',
     '.',
     '기존',
     '비정규직들을',
     '무조건적으로',
     '무기직',
     '전환한다면',
     '또',
     '다른',
     '정유라',
     '탄생이고',
     '역차별입니다',
     '.',
     '새로',
     '필요로',
     '하는',
     '신규채용부터',
     '공채절차를',
     '거쳐',
     '무기직',
     '전환해야합니다',
     '.',
     '예전에',
     '공무원',
     '기능직의',
     '일반직',
     '전환',
     ',',
     '초등학교에',
     '중초교사',
     '임용',
     '등이',
     '그',
     '예죠',
     '.',
     '실제',
     '일하는',
     '곳에서는',
     '그분들로',
     '인한',
     '업무처리',
     '미흡으로',
     '문제가',
     '되고',
     '있습니다',
     '.',
     '사립학교는',
     '인건비를',
     '국가에서',
     '주니',
     '사립학교도',
     '국가에서',
     '공채해야',
     '합니다',
     '.',
     '부디',
     '사례',
     '하나하나를',
     '보아가며',
     '처리해주시고',
     '전체',
     '정규직',
     '숫자',
     '전환만',
     '보며',
     '공약실천을',
     '무리하게',
     '하지',
     '말아주세요',
     '.',
     '국민들은',
     '정의로운',
     '나라를',
     '원합니다',
     '.',
     '역차별이',
     '아닌',
     '공정한',
     '채용이',
     '되게',
     '해주세요',
     '.']




```python
print(len(tokened_title))
print(len(tokened_content))
```

    5
    125
    

## **텍스트 데이터 전처리**
* **개행문자 제거**


```python
def preprocessing(text):
    # 개행문자 제거
    text = re.sub('\\\\n', ' ', text)
    return text
```


```python
# %time을 찍어주면 해당 코드를 실행할 때 걸리는 시간을 출력
%time sentences = care['content'].apply(preprocessing)
```

    CPU times: user 125 ms, sys: 1.07 ms, total: 126 ms
    Wall time: 128 ms
    


```python
%time tokens = sentences.apply(tokenizer.tokenize)
```

    CPU times: user 26.7 s, sys: 191 ms, total: 26.9 s
    Wall time: 26.9 s
    


```python
tokens[:3]
```




    article_id
    24    [현정부에서, 정규직, 일자리를, 늘리는, 것에, 찬성합니다, ., 그런데, 공공기...
    36    [문재인, 대통령님과, 각, 정부, 인사분들께, 마음속, 깊이, 존경과, 감사를, ...
    45    [초등학교, 교사, 임용, 시험을, 수능, 시험, 처럼, 전국, 단위로, 실시하고난...
    Name: content, dtype: object



## **폰트 설치하기**


```python
# 그래프에 retina display 적용
%config InlineBackend.figure_format = 'retina'

# 나눔고딕 설치
!apt -qq -y install fonts-nanum > /dev/null
import matplotlib.font_manager as fm
fontpath = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
font = fm.FontProperties(fname = fontpath, size = 9)
```

    
    WARNING: apt does not have a stable CLI interface. Use with caution in scripts.
    
    


```python
# 워드클라우드 설치
!pip install wordcloud
```

## **불용어 처리하기**
* **불용어는 큰 의미를 가지지 않는 단어를 의미한다. WordCloud에 불용어가 많은 부분을 차지하면 의미가 없어지므로 따로 빼놓는 것이 좋다.**


```python
stopwords_kr = ['하지만', '그리고', '그런데', '저는', '제가',
               '그럼', '이런', '저런', '합니다',
               '많은', '많이', '정말', '너무']
```


```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt
%matplotlib inline

def displayWordCloud(data = None, backgroundcolor = 'white', width = 800, height = 600):
    wordcloud = WordCloud(font_path = fontpath, stopwords = stopwords_kr,
                          background_color = backgroundcolor, width = width, height = height).generate(data)
    plt.figure(figsize = (15, 10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
```


```python
# 위에서 불용어 처리를 했음에도 불용어가 많다.
%time displayWordCloud(' '.join(sentences))
```


![png](output_30_0.png)


    CPU times: user 36.2 s, sys: 2.16 s, total: 38.3 s
    Wall time: 38.2 s
    

## **명사만 추출하기**


```python
from soynlp.noun import LRNounExtractor
```


```python
%%time
noun_extractor = LRNounExtractor(verbose = True)
noun_extractor.train(sentences)
nouns = noun_extractor.extract()
```

    [Noun Extractor] used default noun predictor; Sejong corpus predictor
    [Noun Extractor] used noun_predictor_sejong
    [Noun Extractor] All 2398 r features was loaded
    [Noun Extractor] scanning was done (L,R) has (156500, 78406) tokens
    [Noun Extractor] building L-R graph was done
    [Noun Extractor] 27007 nouns are extracted
    CPU times: user 1min 6s, sys: 298 ms, total: 1min 7s
    Wall time: 1min 7s
    


```python
%time displayWordCloud(' '.join(nouns))
```


![png](output_34_0.png)


    CPU times: user 2.34 s, sys: 157 ms, total: 2.5 s
    Wall time: 2.39 s
    
