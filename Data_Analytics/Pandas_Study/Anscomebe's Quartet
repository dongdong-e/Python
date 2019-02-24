# 앤스콤의 4분할 그래프
import pandas as pd
import seaborn as sns
%matplotlib notebook
import matplotlib.pyplot as plt

# 앤스콤 데이터 집합 불러온 후 그래프 그리기
anscombe = sns.load_dataset("anscombe")

# 열에서 데이터값 추출 추출
dataset_1 = anscombe[anscombe["dataset"] == "I"]
dataset_2 = anscombe[anscombe["dataset"] == "II"]
dataset_3 = anscombe[anscombe["dataset"] == "III"]
dataset_4 = anscombe[anscombe["dataset"] == "IV"]

# 선 그래프로 표현하기
plt.plot(dataset_1['x'], dataset_1['y'])

# 점 그래프로 표현하기 => 선 그래프에 3번째 인자로 o를 넣으면 됌
plt.plot(dataset_1['x'], dataset_1['y'], 'o')

# 한 번에 4개의 그래프 그리기 / 기본 틀 만들기
fig = plt.figure()

# add_subplot()의 첫 번째 인자에는 행의 크기 / 두 번째 인자에는 열의 크기를 지정
axes1 = fig.add_subplot(2, 2, 1)
axes2 = fig.add_subplot(2, 2, 2)
axes3 = fig.add_subplot(2, 2, 3)
axes4 = fig.add_subplot(2, 2, 4)

# plot 메서드에 데이터 전달 / 그래프를 보려면 반드시 fig 입력해야함
axes1.plot(dataset_1['x'], dataset_1['y'], 'o')
axes2.plot(dataset_2['x'], dataset_2['y'], 'o')
axes3.plot(dataset_3['x'], dataset_3['y'], 'o')
axes4.plot(dataset_4['x'], dataset_4['y'], 'o')
fig

# 그래프 이름 지정하기 / set_title 메서드 사용
axes1.set_title("dataset_1")
axes2.set_title("dataset_2")
axes3.set_title("dataset_3")
axes4.set_title("dataset_4")
fig

# 기본틀(fig)에 제목 추가하기 / suptitle 메서드 사용
fig.suptitle("Anscombe Data")
fig

# 그래프의 레이아웃 조절하기 (글자 겹치는 부분 조절) / tight_layout 메서드 사용
fig.tight_layout()
fig
