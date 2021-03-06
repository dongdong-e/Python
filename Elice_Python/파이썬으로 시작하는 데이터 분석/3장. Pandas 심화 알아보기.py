##### 조건으로 검색하기

animal_df = pd.DataFrame({
    'Animal': ['Dog', 'Cat', 'Cat', 'Pig', 'Cat'],
    'Name': ['Happy', 'Sam', 'Toby', 'Mini', 'Rocky']
})

animal_df.Animal.str.match("Cat")
animal_df["Animal"].str.contains("Cat")

##### 함수로 데이터 처리하기

df = pd.DataFrame(np.arange(5), columns = ["Num"])

# 함수를 만들어 apply 사용하기 (1)
def square(x):
    return x ** 2
df["Num"].apply(square)
df["Square"] = df["Num"].apply(square)

# 함수를 만들어 apply 사용하기 (2)

df = pd.DataFrame(columns = ["phone"])
df.loc[0] = "010-1234-1235"
df.loc[1] = "공일공-일이삼사-1235"
df.loc[2] = "010.1234.1235"
df.loc[3] = "공1공-1234.1이3오"
df["preprocess_phone"] = ''

def get_preprocess_phone(phone):
    mapping_dict = {
        "공": "0",
        "일": "1",
        "이": "2",
        "삼": "3",
        "사": "4",
        "오": "5",
        "-": "",
        ".": ""
    }
    for key, value in mapping_dict.items():
        phone = phone.replace(key, value)
    return phone

df["preprocess_phone"] = df["phone"].apply(get_preprocess_phone)
df

# lambda 표현식 사용하기
df["Square"] = df.Num.apply(lambda x: x ** 2)

# replace: apply 기능에서 데이터 값만 대체
df = pd.DataFrame(columns = ["Sex"])
df.loc[0] = "Male"
df.loc[1] = "Male"
df.loc[2] = "Female"
df.loc[3] = "Female"
df.loc[4] = "Male"

df.Sex.replace({"Male": 0, "Female": 1}, inplace = True)
df.Sex.replace({"Male": 0, "Female": 1}, inplace = True, inplace = True) # 데이터 프레임에서 데이터 프레임으로 바로 전환

# [실습] 함수로 데이터 처리하기

def main():
    df = pd.DataFrame(np.arange(5), columns=["Num"])
    print(df, "\n")

    # 값을 받으면 제곱을 해서 돌려주는 함수
    def square(x):
        return x ** 2
        
    # # apply로 컬럼에 함수 적용
    df["Num"].apply(square)
    df["Square"] = df["Num"].apply(square)
    print(df)
    
    # 람다 표현식으로도 적용하기
    df["Square"] = df.Num.apply[lambda: x, x ** 2]
    print(df)

##### 그룹으로 묶기
# groupby 이용
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                  'data1': [1, 2, 3, 1, 2, 3],
                   'data2': np.random.randint(0, 6, 6)})
df.groupby('key')
df.groupby('key').sum()
df.groupby(['key', 'data1']).sum()

# agreegate 이용
def main():
    df = pd.DataFrame({
        'key': ['A', 'B', 'C', 'A', 'B', 'C'],
        'data1': [0, 1, 2, 3, 4, 5],
        'data2': [4, 4, 6, 0, 6, 1]
    })
    print("DataFrame:")
    print(df, "\n")
    
    # aggregate를 이용하여 요약 통계량을 산출해봅시다.
    # 데이터 프레임을 'key' 칼럼으로 묶고, data1과 data2 각각의 최솟값, 중앙값, 최댓값을 출력하세요.
    print(df.groupby('key').aggregate([min, np.median, max]))
    
    # 데이터 프레임을 'key' 칼럼으로 묶고, data1의 최솟값, data2의 합계를 출력하세요.
    print(df.groupby('key').aggregate({'data1': min, 'data2': np.sum}))

# MultiIndex (멀티인덱스) -> 인덱스를 계층적으로 만들 수 있다
df = pd.DataFrame(
    np.random.randn(4, 2),
    index = [['A', 'A', 'B', 'B'], [1, 2, 1, 2]],
    columns = ['data1', 'data2'])

df = pd.DataFrame(
    np.random.randn(4, 4),
    columns = [["A", "A", "B", "B"], ["1", "2", "1", "2"]]
)

##### [실습] 피리 부는 사나이를 따라가는 아이들

def main():
    # 파일을 읽어서 코드를 작성해보세요
    # 경로: "./data/the_pied_piper_of_hamelin.csv"
    df = pd.read_csv("./data/the_pied_piper_of_hamelin.csv")
    
    
    # 일차별로 아이들의 평균 나이 구하기
    # 마스킹 연산으로 Child만 출력
    children = df[df["구분"] == "Child"]
    print(children)
    
    # 일차별로 그룹 지정하여 평균 나이 구하기
    print(children.groupby("일차").mean())
    
    
    # 일차별로 남자 아이와 여자 아이의 평균 나이 구하기
    # 피벗 테이블로 만들어서 평균 구하기
    print(children.pivot_table(index = "일차", columns = "성별", values = "나이", aggfunc = np.mean))
    
    # 아이들의 이름 구하기
    for name in children["이름"].unique():
        print(name)
