import csv
file = open("village_population.csv", encoding = "utf-8")
data = csv.reader(file)
next(data)

pop = []
for row in data:
    if '송도1동' in row[0]:
        for ingu in range(3, len(row)):
            pop.append(int(row[ingu]))

import matplotlib.pyplot as plt
plt.hist(pop)
plt.show()

###### show()는 그래프 각자 표시하기 위해서 사용

plt.plot(pop)
plt.show()
