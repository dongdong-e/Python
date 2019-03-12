###GUGUDAN
def times_tables_1(num):
    n = 1
    while n <= 10:
        print(num, " * ", n, " = ", n * num)
        n = n + 1

def times_tables_2(num, how_far):
    n = 1
    while n <= how_far:
        print(num, " * ", n, " = ", num * n)
        n = n + 1


##SET UP FUNCTION

def is_same(target, number):
    if target == number:
        result = "WIN"
    elif target > number:
        result = "LOW"
    else:
        result = "HIGH"
    return result

##CHOOSE RANDOM NUMBER

import random

computer_number = random.randint(1, 100)

##GAME START

print("안녕? 내가 1에서 100 사이에서 숫자를 골라볼게 너가 맞춰봐~")

##GET USER NUMBER

guess = int(input("어떤 숫자일까?  "))

##USE is_same FUNCTION

higher_or_lower = is_same(computer_number, guess)

##KEEP PLAYING UNTIL USER GET A WIN

while higher_or_lower != "WIN":
    if higher_or_lower == "LOW":
        guess = int(input("그것보단 높습니다. 다시 생각해보세요."))
    else:
        guess = int(input("그것보단 낮습니다. 다시 생각해보세요."))

    higher_or_lower = is_same(computer_number, guess)

##FINISH THE GAME

input("정답! 잘했어요! \n\n\n 종료하려면 엔터를 누르세요.")
