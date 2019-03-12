<h1> 0부터 5사이 랜덤한 값이 담긴 3x5 array를 만들어 봅시다! </h1>
np.random.randint(0, 5, (3, 5))

##################### array 자료형, 차원, 모양, 크기, 타입

def main():
    print("1차원 array")
    array = np.arange(10)
    print(array)

    # Q1. array의 자료형을 출력해보세요.
    print(type(array))
    
    # Q2. array의 차원을 출력해보세요.
    print(array.ndim)
    
    # Q3. array의 모양을 출력해보세요.
    print(array.shape)
    
    # Q4. array의 크기를 출력해보세요.
    print(array.size)
    
    # Q5. array의 dtype(data type)을 출력해보세요.
    print(array.dtype)
    
    # Q6. array의 5번째 요소를 출력해보세요.
    print(array[5])
    
    # Q7. array의 3번째 요소부터 5번째 요소까지 출력해보세요.
    print(array[3:6])

##################### 2차원 array

def main():
    print("2차원 array")
    
    #1부터 15까지 들어있는 (3,5)짜리 배열을 만듭니다.
    
    matrix = np.arange(1, 16).reshape(3,5)
    print(matrix)
    
    # Q1. matrix의 자료형을 출력해보세요.
    print("자료형 : ", type(matrix) )
    
    # Q2. matrix의 차원을 출력해보세요.
    print("차원 : ", matrix.ndim )
    
    # Q3. matrix의 모양을 출력해보세요.
    print("모양 : ", matrix.shape )
    
    # Q4. matrix의 크기를 출력해보세요.
    print("크기 : ", matrix.size )
    
    # Q5. matrix의 dtype(data type)을 출력해보세요.
    print("dtype :", matrix.dtype )
    
    # Q6. matrix의 (2,3)번째 요소를 출력해보세요.
    print(matrix[2,3])
    
    # Q7. matrix의 행은 0번째부터 1번째까지, 열은 1번째부터 3번째까지 출력해보세요.
    print(matrix[0:2, 1:4])

##################### array reshape하기

def main():
    print("array")
    array = np.arange(8)
    print(array)
    print("shape : ", array.shape, "\n")


    # Q1. array를 (2,4) 크기로 reshape하여 matrix에 저장한 뒤 matrix와 그의 shape를 출력해보세요.
    print("# reshape (2, 4)")
    matrix = array.reshape(2, 4)
    
    print(matrix)
    print("shape : ", matrix.shape)

##################### array reshape 활용

def main():
    print("array")
    array = np.arange(8)
    print(array)
    print("shape : ", array.shape, "\n")


    # Q1. array를 (2,4) 크기로 reshape하여 matrix에 저장한 뒤 matrix와 그의 shape를 출력해보세요.
    print("# reshape (2, 4)")
    matrix = array.reshape(2, 4)
    
    print(matrix)
    print("shape : ", matrix.shape)
 
##################### concatenate 활용하여 array 붙이기

def main():
    print("matrix")
    matrix = np.array([[0,1,2,3],[4,5,6,7]])
    print(matrix)
    print("shape : ", matrix.shape, "\n")


    # Q1. matrix 두 개를 세로로 붙이기
    '''
    [[0 1 2 3]
     [4 5 6 7]
     [0 1 2 3]
     [4 5 6 7]]
    '''
    m = np.concatenate([matrix, matrix], axis = 0)
    
    print(m, "\n")
    
    
    # Q2. matrix 두 개를 가로로 붙이기
    '''
    [[0 1 2 3 0 1 2 3]
     [4 5 6 7 4 5 6 7]]
    '''
    n = np.concatenate([matrix, matrix], axis = 1)
    
    print(n)

##################### split 사용하여 array 

def main():
    print("matrix")
    matrix = np.array([[ 0, 1, 2, 3],
                       [ 4, 5, 6, 7],
                       [ 8, 9,10,11], 
                       [12,13,14,15]])
    print(matrix, "\n")

    # Q1. matrix를 [3] 행에서 axis 0으로 나누기
    '''
    [[0  1   2  3]
     [4  5   6  7]
     [8  9  10 11]],
     
     [12 13 14 15]
    '''
    a, b = np.split(matrix, [3], axis = 0)
    
    print(a, "\n")
    print(b, "\n")
    
    
    # Q2. matrix를 [1] 열에서 axis 1로 나누기
    '''
    [[ 0]
     [ 4]
     [ 8]
     [12]],
     
    [[ 1  2  3]
     [ 5  6  7]
     [ 9 10 11]
     [13 14 15]]
    '''
    
    c, d = np.split(matrix, [1], axis = 1)
    
    print(c, "\n")
    print(d)

##################### 브로드캐스팅(Broadcasting) 연산

def main():
    array = np.array([1,2,3,4,5])
    
    print(array)
    
    # Q1. array에 5를 더한 값을 출력해보세요.
    print("array + 5 : ", array + 5 )
    
    # Q2. array에 5를 뺀 값을 출력해보세요.
    print("array - 5 : ", array - 5 )
    
    # Q3. array에 5를 곱한 값을 출력해보세요.
    print("array * 5 : ", array * 5 )
    
    # Q4. array를 5로 나눈 값을 출력해보세요.
    print("array / 5 : ", array / 5 )
    
    
    # Q5. array에 array2를 더한 값을 출력해보세요.    
    array2 = np.array([5,4,3,2,1])
    
    print("배열끼리의 덧셈 : ", array + array2 )
    
    # Q6. array에 array2를 뺀 값을 출력해보세요.
    print("배열끼리의 뺄셈 : ", array - array2 )



    def main():
#     x = np.arange(3).reshape((3,1)) 
#     y = np.arange(3)
#     print("x")
#     print(x, "\n")
#     print("y")
#     print(y, "\n")
#     print("x + y")
#     print(x + y)
    
#     '''
#     [[0]
#      [1]
#      [2]
#      [3]
#      [4]
#      [5]] 배열과
     
#      [0 1 2 3 4 5] 배열을 선언하고, 덧셈 연산해보세요.
#     '''
    
    x = np.arange(6).reshape((6, 1))
    y = np.arange(6)
    print("x")
    print(x, "\n")
    print("y")
    print(y, "\n")
    print("x + y")
    print(x + y)

##################### 마스킹 연산
x = np.arange(5)

x < 3     # array([ True,  True,  True, False, False])

x > 5     # array([False, False, False, False, False])

x[x < 3]  # array([0, 1, 2])

##################### 양치기 소년 거짓말 횟수 

daily_liar_data = [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]

def main():
    liar_array = np.array(daily_liar_data)
    # print(liar_array[liar_array == 0].size)
    print(np.count_nonzero(liar_array == 0))
