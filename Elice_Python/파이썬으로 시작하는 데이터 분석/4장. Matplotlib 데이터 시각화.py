##### 그래프 그려보기
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

fig, axes = plt.subplots()      # figure는 도화지
axes.plot(x, y)
axes.set_title("First Plot")
axes.set_xlabel("x")
axes.set_ylabel("y")

# 그래프 저장하기
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
fig, axes = plt.subplots()      # figure는 도화지 / ax는 도화지 안에 그래프를 그릴 수 있는 곳
axes.plot(x, y)
axes.set_title("First Plot")
axes.set_xlabel("x")
axes.set_ylabel("y")
fig.set_dpi(300) # dot per inch(DPI)
fig.savefig("first_plot.png")

# 그래프 여러개 그리기
# numpy의 linspace 함수를 이용 / 0부터 4 * pi까지 100개의 구간으로 나눔
x = np.linspace(0, np.pi * 4, 100)
fig, axes = plt.subplots(2, 1)      # 2개의 그래프를 세로축으로 그리기 (앞 그래프 개수)
axes[0].plot(x, np.sin(x))
axes[1].plot(x, np.cos(x))

##### Matplotlib 그래프 종류
# Line plot (선 그래프)
fig, axes = plt.subplots()    # subplots에 값을 넣지 않으면 1개의 도화지와 1개의 그래프만 그림
x = np.arange(15)             # x축을 0부터 14까지 지정
y = x ** 2                    # y축을 x의 제곱값으로 지정
axes.plot(
    x, y,
    linestyle = ":",
    marker = "*",
    color = "#524FA1"
)

# Line style
x = np.arange(10)
fig, axes = plt.subplots()
fig.set_dpi(200)

axes.plot(x, x, linestyle = "-")         # solid style
axes.plot(x, x + 1, linestyle = "--")    # dashed style
axes.plot(x, x + 2, linestyle = "-.")    # dashdot style
axes.plot(x, x + 3, linestyle = ":")     # dotted style

# Color
x = np.arange(10)
fig, axes = plt.subplots()
axes.plot(x, x, color = "r")             # red, blue, green 등의 앞글자로 표현
axes.plot(x, x + 1, color = "green")     # 색깔의 영문명으로 표현
axes.plot(x, x + 2, color = "0.8")       # 0 ~ 1 사이값은 회색조로 표현
axes.plot(x, x + 3, color = "#524FA1")   # RGP의 16진수 코드로 표현

# Marker
x = np.arange(10)
fig, axes = plt.subplots()
axes.plot(x, x, marker = ".")         # 작은 점으로 표현
axes.plot(x, x + 1, marker = "o")     # 원으로 표현
axes.plot(x, x + 2, marker = "v")     # 세모로 표현
axes.plot(x, x + 3, marker = "s")     # 네모로 표현
axes.plot(x, x + 4, marker = "*")     # 별모양으로 표현

# 범례 만들기
fig, axes = plt.subplots()
axes.plot(x, x, label = 'y = x', color = "red") # 라벨값(y = x)을 입력
axes.plot(x, x ** 2, label = "y = x^2", color = "blue") # 라벨값(y = x^2)을 입력
axes.set_xlabel("x")
axes.set_ylabel("y")
axes.legend(
    loc = "upper left",   # loc (상단: upper, 하단: lower, 오른쪽: right, 왼쪽: right, 중앙: center)
    shadow = True,        # 그림자 생성 / 비생성
    fancybox = True,      # 둥근 모서리 생성 / 비생성
    borderpad = 1         # 박스의 크기
)

# Scatter(산점도 그래프)
fig, axes = plt.subplots()
x = np.arange(30)
axes.plot(
    x, x ** 2, "o",               # x축 = x / y축 = x^2 / 원으로 표시
    markersize = 5,               # 원사이즈
    markerfacecolor = "white",    # 원내부 색상 지정
    markeredgecolor = "blue"      # 원 테두리 색상 지정
)

fig, axes = plt.subplots()
x = np.random.randn(50)     # 정규분포에서 50개씩 무작위 추출
y = np.random.randn(50)     # 정규분포에서 50개씩 무작위 추출

colors = np.random.randint(0, 100, 50)     # 0부터 100 사이 50개 무작위 추출  
sizes = 500 * np.pi * np.random.rand(50) ** 2

axes.scatter(
    x, y, c = colors, s = sizes, alpha = 0.6    # alpha값 = 점의 투명도 조절
)

# Matplotlib with pandas
df = pd.read_csv("pokemon.csv")
df.head()

## Type 1 또는 Type 2에 Fire 속성만 추출
fire = df[
    (df['Type 1'] == 'Fire') | ((df['Type 2']) == 'Fire')]
## Type 2 또는 Type 2에 Water 속성만 추출
water = df[
    (df['Type 1'] == "Water") | ((df['Type 2']) == 'Water')]

fig, ax = plt.subplots()
## x축은 Fire의 Attack / y축은 Fire의 Defence / s는 사이즈
ax.scatter(fire['Attack'], fire['Defense'],
          color = "red", label = "Fire", marker = "*", s = 25)
## x축은 Water의 Attack / y축은 Water의 Defence / s는 사이즈
ax.scatter(water['Attack'], water['Defense'],
          color = "blue", label = "Water", marker = ".", s = 25)
ax.set_xlabel("Attack", color = "white")
ax.set_ylabel("Defense", color = "white")
ax.legend(loc = "upper left")
fig.set_dpi(300)

##### [실습] 토끼와 거북이 경주 결과 시각화
# 인덱스값 수정하는 방법(1)
df = pd.read_csv("./data/the_hare_and_the_tortoise.csv", index = 0)
    
# 인덱스값 수정하는 방법(2)
df.set_index("시간", inplace = True)
    
fig, ax = plt.subplots()
ax.plot(df["토끼"], label = "토끼")
ax.plot(df["거북이"], label = "거북이")
ax.legend(loc = "upper left")
   
fig.savefig("plot.png")
elice_utils.send_image("plot.png")
