#111
x = input()
print(x*2)

#112
x = input("숫자를 입력하세요: ")
print(int(x)+10)

#113
x = int(input())
if x % 2 == 0:
    print("짝수")
else:
    print("홀수")

#114
x = int(input("입력값: "))
result = x + 20
if result > 255:
    print("255")
else:
    print(result)

#115
x = int(input("입력값: "))
result = x - 20
if result < 0:
    print("0")
elif result > 255:
    print("255")
else:
    print(result)

#116
x = input("현재시간:")
result = x.split(":")
if int(result[1]) != 0:
    print("정각이 아닙니다")
else:
    print("정각 입니다.")

#117
fruit = ["사과", "포도", "홍시"]
x = input("좋아하는 과일은? ")
if x in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

#118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
x = input()
if x in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")

#119
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
x = input("제가좋아하는계절은: ")
if x in fruit.keys():
    print("정답입니다.")
else:
    print("오답입니다.")

#120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
x = input("좋아하는과일은: ")
if x in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")