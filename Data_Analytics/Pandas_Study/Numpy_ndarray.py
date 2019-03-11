###### NumPy ndarray: 다차원 배열 객체
# ndarray는 같은 종류의 데이터만 담을 수 있다.
# ndarray의 모든 원소는 같은 자료형이어야 한다.

# 2행 3열의 랜덤 배열 생성
import numpy as np
data = np.random.rand(2, 3)

# 배열은 전체 데이터 블록에 수학적인 연산을 수행할 수 있음
data * 10
data + data

# 배열의 차원 크기를 알려주는 shape
data.shape

# 배열에 저장된 자료형을 알려주는 dtype
data.dtype

#############################################################
###### ndarray 생성

# 순차적인 객체(다른 배열도 포함)를 받아 새로운 Numpy 배열을 생성
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)

# np.array는 zeros와 ones로 주어진 길이나 모양에 각각 0과 1이 들어있는 배열 생성
np.zeros(10)
np.ones((3, 6))

# np.empty는 0으로 초기화된 배열을 반환하지 않는다.
np.empty((2, 3, 2))

# arange는 파이썬의 range 함수의 배열 버전
np.arange(15)

# ndarray의 astype 메서드로 배열의 dtype 바꾸기
arr = np.array([1, 2, 3, 4, 5])
arr.dtype # 'int64'로 정수형

float_arr = arr.astype(np.float64)
float_arr.dtype # 'float64'로 부동소수점형

# 숫자 형식의 문자열을 담고 있는 배열 숫자로 바꾸기
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype = np.string_)
numeric_strings.astype(float) #np를 생략해도 변환 가능

int_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype = np.float64) # 부동소수점형
int_array.astype(calibers.dtype)                  # int_array의 형태를 calibers와 일치시킴

# 배열과 스칼라 간의 연산 / # 스칼라 값에 대한 산술연산은 각 요소로 전달
arr = np.array([[1., 2., 3.], [4., 5., 6]])
arr * arr
arr - arr
1 / arr

# 1차원 배열은 파이썬의 리스트와 유사하게 동작
arr = np.arange(10)                               # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 출력
arr[5]                                            # array([5]) 출력
arr[5:8]                                          # array([5, 6, 7]) 출력

arr[5:8] = 12                                     # 기존 arr 배열의 5:8 위치를 12로 변환
arr_slice = arr[5:8]                              # 기존 arr 배열의 5:8 위치값을 arr_slice 변수로 설정
arr_slice[1] = 12345                              # arr_slice의 원래값은 array([12, 12, 12])지만 1 위치값을 12345로 변환
arr_slice[:] = 64                                 # arr_slice의 모든값을 64로 변환

# 다차원 배열 슬라이싱 3 * 3 행렬
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[2]                                          # 3번째 행을 출력
arr2d[0][2], arr2d[0, 2]                          # 1번째 행의 3번째 행 출력

# arr3d가 2 * 2 * 3 크기의 배열이라면 arr3d[0]은 2 * 3 크기의 배열
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d[0]

# arr3d[0]에는 스칼라 값과 배열 보두 대입 가능
old_values = arr3d[0].copy()
arr3d[0] = 42
arr3d[0] = old_values
