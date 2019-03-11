############################################################
# Series 만들기
series1 = pd.Series(['banana', 42])
series2 = pd.Series(['Wes McKinney', 'Creator of Pandas'])
# index 인자로 문자열 인덱스로 지정하기
series3 = pd.Series(['Wes McKinney', 'Creator of Pandas'], index = ['Person', 'Who'])
############################################################
# DataFrame 만들기
scientists = pd.DataFrame({
    'Name': ['Rosaline Franklin', 'William Gosset'],
    'Occupation': ['Chemist', 'Statistician'],
    'Born': ['1920-07-25', '1876-06-13'],
    'Died': ['1958-04-16', '1937-10-16'],
    'Age': [37, 61]
})
# index 인자로 문자열 인덱스로 지정하기
scientists = pd.DataFrame(
    data = {'Occupation': ['Chemist', 'Statistician'],
            'Born': ['1920-07-25', '1876-06-13'],
            'Died': ['1958-04-16', '1937-10-16'],
            'Age': [37, 61]},
    index = ['Rosaline Franklin', 'William Gosset'],
    columns = ['Occupation', 'Born', 'Age', 'Died']
)
# DataFrame 생성할 때 순서 유지하기
from collections import OrderedDict

scientists = pd.DataFrame(OrderedDict([
    ('Name', ['Rosaline Franklin', 'William Gosset']),
    ('Occupation', ['Chemist', 'Statistician']),
    ('Born', ['1920-07-25', '1876-06-13']),
    ('Died', ['1958-04-16', '1937-10-16']),
    ('Age', [37, 61])
])
)
############################################################
# 특정 인덱스만 받아오기
first_row = scientists.loc['William Gosset']
print(first_row.index())

# Series의 mean, min, max, std 메서드 사용하기
ages = scientists['Age']
print(ages.mean())
print(ages.min())
print(ages.max())
print(ages.std())
############################################################
# 시리즈와 불린 추출 사용하기
ages = scientists['Age']
print(ages.mean())
print(ages[ ages > ages.mean()])
print(ages > ages.mean())

# 수동(메뉴얼)으로 True, False 지정하여 추출
manual_bool_values = [True, True, False, False, True, True, False, True]
print(ages[manual_bool_values])
############################################################
# 벡터와 스칼라로 브로드캐스팅 수행하기
## 같은 길이의 벡터 연산 / 같은 길이의 벡터 출력
print(ages + ages)
print(ages * ages)
## 벡터에 스칼라 연산
print(ages + 100)
print(ages * 2)

## 다른 길이의 벡터 연산 / 같은 인덱스 값만 계산 결과가 나오고, 나머지는 누락값(NaN)으로 처리
print(pd.Series([1, 100]))
print(ages + pd.Series([1, 100]))
############################################################
# 불린 추출하기
print(scientists[scientists['Age'] > scientists['Age'].mean()])

# 참 / 거짓을 담은 bool 벡터
print(scientists.loc[[True, True, False, True]])
