#231
"""
def n_plus_1 (n) :
    result = n + 1

n_plus_1(3)
print (result)
"""
"""
함수 내부에서 사용한 변수는 함수 밖에서는 접근이 불가능
함수 내부에서 계산한 값을 전달하기 위해서는 return을 사용
"""

#232
def make_url(a):
    url = "www."+a+".com"
    return url

make_url("naver")

#233
def make_list(string):
    a = list(string)
    return a

l = make_list("abcd")
print(l)

#234
def pickup_even(l):
    list = []
    for i in l:
        if i % 2 ==0:
            list.append(i)
    return list
x = pickup_even([3, 4, 5, 6, 7, 8])
print(x)

#235
def convert_int(str):
    str = str.replace(",","")
    return int(str)
result = convert_int("1,234,567")
print(result)

#236
def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)

#237
def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)

#238
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)

#239
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)

#240
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)