# 서울 범죄
import pandas as pd
import numpy as np
import seaborn as sns
%matplotlib notebook
import matplotlib.pyplot as plt

crime_seoul = pd.read_csv("crime_Seoul2.csv", encoding = "utf-8",
                         thousands = ",",
                         index_col = 0)    # 천단위에 콤마 제거하기

# pivot 테이블
data_result = pd.pivot_table(crime_seoul, index = "구별", aggfunc = np.sum)

# 강간 검거율 / 강도 검거율 / 살인 검거율 / 절도 검거율 / 폭력 검거율 추가하기
data_result["강간 검거율"] = round((data_result["강간 검거"] / data_result["강간 발생"]) * 100, 2)
data_result["강도 검거율"] = round((data_result["강도 검거"] / data_result["강도 발생"]) * 100, 2)
data_result["살인 검거율"] = round((data_result["살인 검거"] / data_result["살인 발생"]) * 100, 2)
data_result["절도 검거율"] = round((data_result["절도 검거"] / data_result["절도 발생"]) * 100, 2)
data_result["폭력 검거율"] = round((data_result["폭력 검거"] / data_result["폭력 발생"]) * 100, 2)

# 강도 검거율 100 이상인 곳 출력
data_result.loc[data_result["강도 검거율"] > 100, :]

# 검거율이 100 이상인 곳을 100으로 셋팅하기
cols = ["강간 검거율", "강도 검거율", "살인 검거율", "절도 검거율", "폭력 검거율"]

for s in cols:
    data_result.loc[data_result[s] > 100, s] = 100
