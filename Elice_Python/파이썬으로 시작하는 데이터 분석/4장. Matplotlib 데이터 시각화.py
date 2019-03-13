# 그래프 그려보기
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
plt.plot(x, y)

# 그래프에 제목과 라벨 달기
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
plt.plot(x, y)
plt.title("First Plot") # 그래프 제목
plt.xlabel("x") # x축 이름
plt.ylabel("y") # y축 이름

# object oriented interface로 그래프 그리기
# x, y를 수동으로 설정하여 그래프 그리기
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

fig, axes = plt.subplots() # figure는 도화지
axes.plot(x, y)
axes.set_title("First Plot")
axes.set_xlabel("x")
axes.set_ylabel("y")

# 그래프 저장하기
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
fig, axes = plt.subplots() # figure는 도화지 / ax는 도화지 안에 그래프를 그릴 수 있는 곳
axes.plot(x, y)
axes.set_title("First Plot")
axes.set_xlabel("x")
axes.set_ylabel("y")
fig.set_dpi(300) # dot per inch(DPI)
fig.savefig("first_plot.png")

# 그래프 여러개 그리기
# numpy의 linspace 함수를 이용 / 0부터 4 * pi까지 100개의 구간으로 나눔
x = np.linspace(0, np.pi * 4, 100)
fig, axes = plt.subplots(2, 1) # 2개의 그래프를 세로축으로 그리기 (앞에가 그래프 개수)
axes[0].plot(x, np.sin(x))
axes[1].plot(x, np.cos(x))
