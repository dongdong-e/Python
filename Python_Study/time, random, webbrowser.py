###TIME

import time
for i in range(10):
    print(i)
    time.sleep(1)

###################################

import calendar
print(calendar.calendar(2015))

calendar.prmonth(2019, 2)

calendar.weekday(2015, 12, 31)

###RANDOM

import random
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data: print(random_pop(data))


import random
data = [1, 2, 3, 4, 5]
random.shuffle(data)
print(data)

###webbrowser

import webbrowser
address = input("웹주소를 입력하세요")
webbrowser.open(address)

address = input("웹주소를 입력하세요")
webbrowser.open_new(address)

