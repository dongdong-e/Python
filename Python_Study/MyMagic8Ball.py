import random

answers =(
    "자! 해보세요!",
    "됐네요, 이 사람아",
    "뭐라고? 다시 생각해봐",
    "모르니 두려운 것입니다.",
    "칠푼인가요? 정신이 나갔네!",
    "당신이라면 할 수 있어요!",
    "해도 되고, 안해도 돼요!",
    "맞아요, 당신은 올바른 선택을 했어요!")

print("MyMagic8Ball에 오신 것을 환영합니다.\n")

question = input("조언을 구하고 싶으면 질문을 입력하고 엔터키를 누르세요.\n")

print("고민중입니다...\n" * 4)

choice = random.randint(0, 7)

print(answers[choice])

input("\n\n마치려면 엔터키를 누르세요.")
