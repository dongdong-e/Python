##### 1장. NumPy 사용해보기
#### Reshape & 이어붙이고 나누기
x = np.arange(8).reshape(2, 4)

# cocatenate -> array 이어붙이기
x = np.array([0, 1, 2])
y = np.array([3, 4, 5])
np.concatenate([x, y])

# np.concatenate -> axis 축을 기준으로 이어붙이기
matrix = np.arange(4).reshape(2, 2)
np.concatenate([matrix, matrix], axis = 0)     # 세로로 잇기
np.concatenate([matrix, matrix], axis = 1)     # 가로로 잇기

# np.split -> axis 축을 기준으로 나누기
matrix = np.arange(16).reshape(4, 4)
upper, lower = np.split(matrix, [3], axis = 0)     # 세로 인덱스 번호로 자르기
left, right = np.split(matrix, [3], axis = 1)      # 가로 인덱스 번호로 자르기

#### Numpy 연산
# 루프는 느리다
# array의 모든 원소에 5를 더해서 만드는 함수
def add_five_to_array(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = values[i] + 5
    return output

values = np.random.randint(1, 10, size = 5, dtype = int)
add_five_to_array(values)

# 만약 array의 크기가 크다면? 속도가 매우 느려진다.
big_array = np.random.randint(1, 100, size = 10000000)
add_five_to_array(big_array)

# Numpy는 큰연산을 빠르게 처리
big_array + 5

# array는 기본 사칙연산을 지원
x = np.arange(4)
x + 5
x - 5
x * 5
x / 5
        
# 다차원 행렬에서도 적용가능
x = np.arange(4).reshape((2, 2))
y = np.random.randint(10, size = (2, 2))
x + y
x - y

#### 브로드캐스팅
# Broadcasting -> shape가 다른 array끼리 연산
matrix + 5
matrix + np.array([1, 2, 3, 4])
np.arange(3).reshape((3, 1)) + np.arange(3)

#### 집계함수 & 마스킹연산
# 집계함수
x = np.arange(8).reshape((2, 4))
np.sum(x)    # 28
np.min(x)    # 0
np.max(x)    # 7
np.mean(x)   # 3.5
np.std(x)    # 2.29128...

np.sum(x, axis = 0)    # array([ 4,  6,  8, 10])
np.sum(x, axis = 1)    # array([ 6, 22])

# 마스킹 연산
x = np.arange(5)
x < 3    # array([ True,  True,  True, False, False])
x > 5    # array([False, False, False, False, False])
x[x < 3]    # array([0, 1, 2])

#### [실습] 양치기 소년의 거짓말 횟수 구하기
# 진실 = 1 / 거짓말 = 0
daily_liar_data = [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0,
                   0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1,
                   0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                   1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1,
                   0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1,
                   1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1,
                   0, 1, 0, 0, 1, 0, 0, 0, 0, 0]

liar_array = np.array(daily_liar_data)
liar_array.dtype    # 데이터 타입 추출
liar_array.size     # 데이터 크기
len(liar_array)     # 데이터 길이

print(liar_array == 0)                     # 마스킹 연산 적용 True값(0)만 추력
print(liar_array[liar_array == 0])         # True값을 0으로 출력
print(len(liar_array[liar_array == 0]))    # 데이터 갯수 출력

# nonzero -> 0이거나 False가 아닌 데이터를 카운팅
print(np.count_nonzero(liar_array  == 0))

###############################################################################

#### Series 데이터
# numpy array가 보강된 형태
data = pd.Series([1, 2, 3, 4])

# 인덱스를 가지고 있고, 인덱스로 접근 가능
data = pd.Series([1, 2 ,3, 4], index = ['a', 'b', 'c', 'd'])
data['b']     # 'a': 1, 'b': 2, 'c': 3, 'd': 4

# 딕셔너리로 만들 수 있다.
population_dict = {
    'korea': 5180,
    'japan': 12718,
    'china': 141500,
    'usa': 32676
}
population = pd.Series(population_dict)     # 딕셔너리의 key값 = index값 / Value값 = data값

#### DataFrame
# 여러 개의 Series가 모여서 행과 열을 이룬 데이터
gdp_dict = {
    'korea': 169320000,
    'japan': 516700000,
    'china': 1409250000,
    'usa': 2041280000
}
gdp = pd.Series(gdp_dict)
country = pd.DataFrame({
    'population': population,
    'gdp': gdp
})

# Series도 numpy array처럼 연산자를 쓸 수 있다.
gdp_per_capita = country['gdp'] / country['population']     # 1인당 gdp 구하기
country['gdp per capita'] = gdp_per_capita                  # country 데이터 프레임에 'gdp per capita'를 추가

# 만든 데이터 프레임을 저장할 수 있다.
country.to_csv("./country.csv")
country.to_excel("country.xlsx")

# 저장한 데이터 프레임을 불러올 수 있다.
country = pd.read_csv("./country.csv")
country = pd.read_excel("country.xlsx")

#### Indexing & Slicing
# loc -> 명시적인 인덱스를 참조하는 인덱싱 / 슬라이싱
country.loc['china']
country.loc['korea':'japan', 'population':]     #한국부터 일본까지 인구 이후 데이터 출력

# iloc -> 파이썬 스타일 정수 인덱싱 / 슬라이싱
country.iloc[0]
country.iloc[1:3, :2]     # 한국부터 중국까지 인구와 gdp를 출력

# DataFrame 새 데이터 추가 / 수정
# 리스트로 추가하는 방법과 딕셔너리로 추가하는 방법
dataframe = pd.DataFrame(columns = ['이름', '나이', '주소'])
dataframe.loc[0] = ['임원균', '26', '서울']                          # 리스트로 추가하는 방법
dataframe.loc[1] = {'이름': '철수', '나이': '25', '주소': '인천'}     # 딕셔너리로 추가하는 방법
dataframe.loc[1, '이름'] = '영희'     # 데이터 수정하는 방법

# DataFrame 새 컬럼 추가
dataframe['전화번호'] = np.nan     # not a number의 축약 -> 데이터값이 비어있게 만듦
dataframe.loc[0, '전화번호'] = '01012341234'

# 컬럼 선택하기
dataframe['이름']                  # 컬럼 이름이 하나만 있다면 Series
dataframe[['이름', '전화번호']]     # 컬럼 이름이 여러개 들어가 있다면 DataFrame
