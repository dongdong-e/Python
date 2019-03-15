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
