import numpy as np
import pandas as pd

def main():

# 예시) 시리즈 데이터를 만드는 방법.
    series = pd.Series([1,2,3,4], index = ['a', 'b', 'c', 'd'], name="Title")
    print(series, "\n")
    
    
# 국가별 인구 수 시리즈 데이터를 딕셔너리를 사용하여 만들어보세요.
    population_dic = {
        'korea': 5180,
        'japan': 12718,
        'china': 141500,
        'usa': 32676}
    population = pd.Series(population_dic)
    print(population)

########## DataFrame (데이터 프레임) 만들기

def main():
    print("Population series data:")
    population_dict = {
        'korea': 5180,
        'japan': 12718,
        'china': 141500,
        'usa': 32676
    }
    population = pd.Series(population_dict)
    print(population, "\n")

    print("GDP series data:")
    gdp_dict = {
        'korea': 169320000,
        'japan': 516700000,
        'china': 1409250000,
        'usa': 2041280000,
    }
    gdp = pd.Series(gdp_dict)
    print(gdp, "\n")


# 이곳에서 2개의 시리즈 값이 들어간 데이터프레임을 생성합니다.
    print("Country DataFrame")
    country = pd.DataFrame({
        'population': population,
        'gdp': gdp
    })
    print(country)

# 데이터 프레임에 gdp_per_pop 변수를 칼럼으로 추가하고 출력합니다.
    gdp_per_pop = country['gdp'] / country['population']
    country['gdp_per_pop'] = gdp_per_pop
    print(country)
    
# 데이터 프레임을 만들었다면, index와 column도 각각 출력해보세요.
    print(country.index)
    print(country.columns)

########### loc (명시적 인덱싱) / iloc (정수 인덱싱)

def main():
# 첫번째 컬럼을 인덱스로 country.csv 파일 읽어오기.
    print("Country DataFrame")
    country = pd.read_csv("./data/country.csv", index_col=0)
    print(country, "\n")

# 명시적 인덱싱을 사용하여 데이터프레임의 "china" 인덱스를 출력해봅시다.
    print(country.loc['china'])
    

# 정수 인덱싱을 사용하여 데이터프레임의 1번째부터 3번째 인덱스를 출력해봅시다.
    print(country.iloc[1:4])
