#121
x = input()
if x.islower():
    x = x.upper()
else:
    x = x.lower()
print(x)

#122
x = int(input("score: "))
print("grade is ", end="")
if 81<=x<=100:
    print("A")
elif 61<=x<=80:
    print("B")
elif 41<=x<=60:
    print("C")
elif 21<=x<=40:
    print("D")
elif 0<=x<=20:
    print("E")

#123
x = input("입력: ")
x = x.split(" ")
if x[1] == "달러":
    result = 1167 * int(x[0])
elif x[1] == "엔":
    result = 1.096 * int(x[0])
elif x[1] == "유로":
    result = 1268 * int(x[0])
elif x[1] == "위안":
    result = 171 * int(x[0])
print("%0.2d 원" %result)

"""
환율 = {"달러": 1167, 
        "엔": 1.096, 
        "유로": 1268, 
        "위안": 171}
user = input("입력: ")
num, currency = user.split()
print(float(num) * 환율[currency], "원")
"""

#124
x1 = int(input("input number: "))
x2 = int(input("input number: "))
x3 = int(input("input number: "))

result = 0
if x1 >= x2:
    if x1 >= x3:
        result = x1
    else:
        result = x3
else:
    if x2 >= x3:
        result = x2
    else:
        result = x3
print(result)

"""
num1 = input("input number1: ")
num2 = input("input number2: ")
num3 = input("input number3: ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)
"""

#125
phone = input("휴대전화 번호 입력: ")
phone = phone.split("-")
if phone[0] == '011':
    result = 'SKT'
elif phone[0] == '016':
    result = 'KT'
elif phone[0] == '019':
    result = 'LGU'
else:
    result = '알수없음'

print("당신은 %s 사용자입니다." %result)

#126
u = input("우편번호: ")
u = int(u[2])
if 0 <= u <= 2:
    print("강북구")
elif 3 <= u <= 5:
    print("도봉구")
else:
    print("노원구")

"""
우편번호 = input("우편번호: ")
우편번호 = 우편번호[:3]
if 우편번호 in ["010", "011", "012"]:
    print("강북구")
elif 우편번호 in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")
"""

#127
p = input("주민등록번호: ")
p = int(p[7])
if p == 1 or p == 3:
    print("남자")
else:
    print("여자")

#128
p = input("주민등록번호: ")
p = int(p[-6:-4])
print(p)
if 0 <= p <= 8:
    print("서울 입니다.")
else:
    print("서울이 아닙니다.")

#129
p = list(input("주민등록번호: "))
p.pop(6)
i = 2
result = 0
for x in p[:-1]:
    result += int(x) * i
    if i == 9:
        i = 1
    i += 1

result = 11 - (result % 11)
if result == int(p[-1]):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")

#130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
print(btc)
var = int(btc['max_price']) - int(btc['min_price'])
if int(btc['opening_price']) + var > int(btc['max_price']):
    print("상승장")
else:
    print("하락장")
