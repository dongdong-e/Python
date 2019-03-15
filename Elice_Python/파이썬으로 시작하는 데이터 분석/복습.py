##### 1장. NumPy 사용해보기
#### Reshape & 이어붙이고 나누기
x = np.arange(8).reshape(2, 4)

# cocatenate -> array 이어붙이기
x = np.array([0, 1, 2])
y = np.array([3, 4, 5])
np.concatenate([x, y])

# np.concatenate -> axis 축을 기준으로 이어붙이기
matrix = np.arange(4).reshape(2, 2)
np.concatenate([matrix, matrix], axis = 0) # 세로로 잇기
np.concatenate([matrix, matrix], axis = 1) # 가로로 잇기

# np.split -> axis 축을 기준으로 나누기
matrix = np.arange(16).reshape(4, 4)
upper, lower = np.split(matrix, [3], axis = 0) # 세로 인덱스 번호로 자르기
left, right = np.split(matrix, [3], axis = 1) # 가로 인덱스 번호로 자르기

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
