# **Pandas_Cheat_Sheet**

```python
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.DataFrame(
        {"a" : [4 ,5, 6, 6, np.nan],
        "b" : [7, 8, np.nan, 9, 9],
        "c" : [10, 11, 12, np.nan, 12]},
        index = pd.MultiIndex.from_tuples(
        [('d',1),('d',2),('e',2), ('e', 3), ('e', 4)],
        names=['n','v']))
```



- **Summarize Pandas Cheat Sheet**

```python
df = df.drop_duplicates()

# 특정값의 유무 확인 isin() -> 리스트로 입력
df["a"].isin([5, 6])

# 특정 열에 있는 null 값의 갯수 출력
df['a'].isnull().sum()

# Logic in Python (and pandas)
&, |, ~, ^, df.any(), df.all()
and, or, not, xor, any, all

df[df["b"] == 7] | df[df["a"] == 5]

# frac -> 특정 비율만큼 데이터를 랜덤 샘플링
df.sample(frac = 0.3)

# sample - > 특정 갯수만큼 데이터를 랜덤 샘플링
df.sample(n = 1)

# 정규표현식으로 특정 컬럼 찾아오기
df.filter(regex = '.')                    # 점(.)이 들어간 컬럼값 출력
df.filter(regex = '_')                    # 점(.)이 들어간 컬럼값 출력
df.filter(regex = '^(?!species$).*')      # species가 들어간 컬럼 제외하고 출력
df.filter(regex = '^sepal')               # 'sepal'로 시작하는 컬럼값 출력
df.filter(regex = '^s[1-5]$')             # 's'로 시작하고 1 ~ 5 사이의 숫자로 끝나는 컬럼만 출력

# Summarize Data
df = sns.load_dataset('iris')
df.head(2)

# value_counts -> 종류의 갯수 파악
df["petal_width"].value_counts()

# dropna
df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                    [3, 4, np.nan, 1],
                    [np.nan, np.nan, np.nan, 5],
                    [np.nan, 3, np.nan, 4]],
                    columns=list('ABCD'))

# 0 = row / 1 = columns
df.dropna(axis = 1, how = "all") # any = 전부다 null값이면 삭제
df.dropna(axis = 1, how = "any") # all = 하나라도 null값이면 삭제
df.dropna(axis = 0, how = "any")
df.dropna(axis = 0, how = "all")

values = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
df.fillna(value = values)

values = {"A": 0}
df.fillna(value = values)

df = pd.DataFrame({'A': range(1, 11), 'B': np.random.randn(10)})

# 새로운 컬럼 만들기 - 모두 똑같은 결과
df.assign(Area = lambda df: df.Length * df.Height)
df.assign(ln_A = lambda x: np.log(x.A)).head()
df["In_A"] = np.log(df.A)

# pd.qcut
pd.qcut(df.B, 3, labels = ["good", "medium", "bad"])
pd.qcut(df.A, 2, labels = ["good", "bad"])

# 절대값 출력
df.abs()

# reshaping
df.sort_values('mpg')
df.sort_values('mpg', ascending = False)
df.rename(columns = {'model_year' : 'year'})     # 컬럼 이름 바꾸기
df.sort_index()
df.reset_index()                                 # index가 없을 때 index를 생성
df.drop(columns = ['Length','Height'])           # 특정 열 삭제 후 출력

# df.melt
df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                   'B': {0: 1, 1: 3, 2: 5},
                   'C': {0: 2, 1: 4, 2: 6}})

df.melt(value_vars=['A', 'B', 'C']).rename(columns ={
'variable' : 'var',
'value' : 'val'})

df3.melt(
    id_vars = ['foo'],
    value_vars = ['A', 'B', 'C']).sort_values(
    ['foo', 'bar']).rename(columns = {'value': 'baz'})Apply 활용하기**
```



- **Apply 함수**

```python
import pandas as pd
import numpy as np
import seaborn as sns

# Apply
df["species_3"] = df["species"].apply(lambda x: x[:3])

def smp(x):
    # 뒤에서 3번째까지 문자를 가져오는 함수
    x = x[-3:]
    return x

df["species-3"] = df["species"].apply(smp)
```
