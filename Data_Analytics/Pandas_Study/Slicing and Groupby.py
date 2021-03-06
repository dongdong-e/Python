# 판다스에서 데이터를 불러올 때는 read_csv 메서드 사용
# 단, tap(탭)으로 구분되어 있기 때문에 sep = '\t'를 지정

import pandas as pd
df = pd.read_csv('c:/PythonTest3/gapminder.tsv', sep = '\t')

# head는 가장 앞에 있는 5개 행을 출력
print(df.head())

# shape는 행/열 크기를 출력
print(df.shape)

# columns는 열에 대한 정보
print(df.columns)

# 특정 열 1개만 저장 및 출력(상위 5개)
country_df = df['country']
print(country_df.head())

# 열 여러개 저장 및 출력(상위 5개)
subset = df[['country', 'continent', 'year']]
print(subset.head())

############################################################
# loc: 행의 인덱스 번호를 기준으로 추출
print(df.loc[0]) # 1번 인덱스
print(df.loc[99]) # 98번 인덱스

# 행의 맨 끝 데이터 추출 / shape[0]은 행의 크기 / tail 메서드 사용
number_of_rows = df.shape[0]
last_row_index = number_of_rows - 1
print(df.loc[last_row_index])
print(df.tail(1))

# 여러 인덱스를 동시에 추출
print(df.loc[[0, 99, 100]])
############################################################
# iloc: 행의 번호를 기준으로 추출 / loc와 다르게 -1로 추출 가능
print(df.iloc[0])
print(df.iloc[99])
print(df.iloc[-1])

# 여러 인덱스를 동시에 추출
print(df.iloc[[0, 99, 100]])
############################################################
# 슬라이싱 구문으로 데이터 추출하기
subset = df.loc[:, ['year', 'pop']]
print(subset.head())

subset = df.iloc[:, [2, 4, -1]]
print(subset.head())

# range로 데이터 추출하기
small_range = list(range(3))
subset = df.iloc[:, small_range]
print(subset.head())
# 위 아래 결과값 같음
subset = df.iloc[:, :3]
print(subset.head())

small_range = list(range(3, 6))
subset = df.iloc[:, small_range]
print(subset.head())

# range의 인자가 3개 => (a, b, c) => a부터 b-1값까지 c만큼 건너뜀
small_range = list(range(0, 6, 2))
subset = df.iloc[:, small_range]
print(subset.head())
# 위 아래 결과값 같음
subset = df.iloc[:, 0:6:2]
print(subset.head())
print(df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']])

subset = df.loc[10:14, ['country', 'lifeExp', 'gdpPercap']]
print(subset)
############################################################
# 위 / 아래 같은 결과
print(df.head(n = 10))
print(df.loc[:,:].head(n = 10))

# 그룹화한 평균값 구하기 / 위: 연도별 평균, 아래: 국가별 평균
print(df.groupby('year')['lifeExp'].mean())
print(df.groupby('country')['lifeExp'].mean())

# 다중으로 그룹화 하여 추출 / 위: 대륙별 평균, 아래: 국가별 평균
print(df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean())
print(df.groupby(['year', 'country'])[['lifeExp', 'gdpPercap']].mean())

# 그룹화한 데이터 개수 세기
print(df.groupby('continent')['country'].nunique())
############################################################
# 그래프 라이브러리
%matplotlib inline
import matplotlib.pyplot as plt

# 연도별 Life Expectancy와 그래프
life_exp = data1.groupby('year')['lifeExp'].mean()
life_exp.plot()
############################################################
