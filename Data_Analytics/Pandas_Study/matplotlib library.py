import pandas as pd
import seaborn as sns
%matplotlib notebook
import matplotlib.pyplot as plt

# 기초 그래프 그리기 - 히스토그램, 산점도 그래프, 박스 그래프
tips = sns.load_dataset("tips")
print(tips.head())
print(type(tips))

# 기본 틀 만들기 - fig와 axesl 구성하기
fig = plt.figure()
axes1 = fig.add_subplot(1, 1, 1)

# 히스토그램 그래프
axes1.hist(tips["total_bill"], bins = 10)
axes1.set_title('Histogram of Total Bill')
axes1.set_xlabel('Frequency')
axes1.set_ylabel('Total Bill')

# 산점도 - 2개의 변수 / 3개 이상의 변수
# 2개의 변수
scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1, 1, 1)
axes1.scatter(tips["total_bill"], tips["tip"])
axes1.set_title("Scatterplot of Total Bill vs Tip")
axes1.set_xlabel("Total Bill")
axes1.set_ylabel("Tip")

# 3개 이상의 변수
# 점의 크기로 테이블 당 인원수 표현
# 문자열은 산점도 그래프에서 새상을 지정할 수 없으므로 정수로 치환해야 함
def record_sex(sex):
    if sex == 'Femal':
        return 0
    else:
        return 1
    
tips['sex_color'] = tips['sex'].apply(record_sex)

scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1, 1, 1)
axes1.scatter(
    x = tips['total_bill'],
    y = tips['tip'],
    s = tips['size'] * 10,
    c = tips['sex_color'],
    alpha = 0.5)

axes1.set_title("Total Bill vs Tip colored by Sex and Sized by size")
axes1.set_xlabel("Total Bill")
axes1.set_ylabel("Tip")


# 박스그래프
boxplot = plt.figure()
axes1 = boxplot.add_subplot(1, 1, 1)

axes1.boxplot([tips[tips['sex'] == 'Female']['tip'],
         tips[tips['sex'] == 'Male']['tip']],
         labels = ['Female', 'Male'])

axes1.set_xlabel("Sex")
axes1.set_ylabel("Tip")
axes1.set_title('Boxplot of Tips by Sex')

# 단변량 그래프 그리기 - 히스토그램
ax = plt.subplots()
ax = sns.distplot(tips["total_bill"])  # distplot 메서드는 히스토그램과 밀집도를 같이 노출
ax.set_title("Total Bill Histogram with Density Plot")

# 단변량 그래프 그리기 - 히스토그램 / 밀집도 그래프 삭제하기 kde = False
ax = plt.subplots()
ax = sns.distplot(tips["total_bill"], kde = False) # 밀집도 그래프 삭제하기 kde = False
ax.set_title("Total Bill Histogram with Density Plot")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Frequency")
