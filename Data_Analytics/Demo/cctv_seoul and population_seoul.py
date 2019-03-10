# 서울 cctv 분포도
import pandas as pd
import numpy as np
import seaborn as sns
%matplotlib notebook
import matplotlib.pyplot as plt
cctv_seoul = pd.read_csv("CCTV_Seoul.csv", encoding = "utf-8")

# 열 이름 바꾸기
cctv_seoul.rename(columns = {cctv_seoul.columns[0]: "구별"},
                 inplace = True)

# 구별 cctv 증가율 추가하기
cctv_seoul["최근 증가율"] = round((cctv_seoul["2014년"] + cctv_seoul["2015년"]
                        + cctv_seoul["2016년"]) / cctv_seoul["2013년도 이전"] * 100, 2)
cctv_seoul.sort_values(by = "최근 증가율", ascending = False)


# 인구 파일 불러오기 / 필요한 열만 불러오고 이름 변경하기
pop_seoul = pd.read_excel("population_Seoul.xls",
                          header = 2,                # 3개의 헤더 중 2개는 빼는 것
                          usecols = "B, D, G, J, N", # 엑셀의 B, D, G, J, N 열만 뽑아오는 것
                          encoding = "utf-8")

pop_seoul.rename(columns ={
    pop_seoul.columns[0]: "구별",
    pop_seoul.columns[1]: "인구수",
    pop_seoul.columns[2]: "한국인",
    pop_seoul.columns[3]: "외국인",
    pop_seoul.columns[4]: "고령자",
}, inplace = True)

# Null값 파악하기
pop_seoul['구별'].unique()

# Null값 가지고 있는 행 파악
pop_seoul[pop_seoul['구별'].isnull()]

# Null값 가지고 있는 행 지우기
pop_seoul.drop([26], inplace = True)

# 인구수 대비 외국인 비율과 고령자 비율
pop_seoul["외국인 비율"] = round((pop_seoul["외국인"] / pop_seoul["인구수"]) * 100, 2)
pop_seoul["고령자 비율"] = round((pop_seoul["고령자"] / pop_seoul["인구수"]) * 100, 2)

# 인구수와 외국인 기준으로 내림차순 정렬
print(pop_seoul.sort_values(by = "인구수", ascending = False))
print(pop_seoul.sort_values(by = "외국인", ascending = False))

# cctv_seoul 데이터와 pop_seoul 데이터 합치기
data_result = pd.merge(cctv_seoul, pop_seoul,
                      on = "구별")   # 구별이라는 공통된 키로 결합

# 그래프 설정
# 히스토그램
fig_hist = plt.figure()
axes1 = fig_hist.add_subplot(1, 1, 1)
axes1.hist(data_result["외국인 비율"])

# 산점도
fig_scatter = plt.figure()
axes2 = fig_scatter.add_subplot(1, 1, 1)
axes2.scatter(data_result["구별"], data_result["한국인"])

# 가로 막대 그래프로 표현하기
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname = "c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family = font_name)

data_result["소계"].plot(kind = "barh", grid = True, figsize = (10, 10))
plt.show()
