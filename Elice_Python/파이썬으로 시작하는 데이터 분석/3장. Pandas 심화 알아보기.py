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
