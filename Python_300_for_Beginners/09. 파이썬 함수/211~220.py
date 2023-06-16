#211
def 함수(문자열) :
    print(문자열)

함수("안녕")
함수("Hi")

#212
def 함수(a, b) :
    print(a + b)

함수(3, 4)
함수(7, 8)

#213

#214
"""
def 함수(a, b) :
    print(a + b)

함수("안녕", 3)
"""

#215
def print_with_smile(str):
    print(str, ":D")

print_with_smile("Hi")

#216
print_with_smile("안녕하세요")

#217
def print_upper_price(number):
    print(number*1.3)
print_upper_price(10000)

#218
def print_sum(a, b):
    sum = a + b
    print(sum)
print_sum(10, 20)

#219
def print_arithmetic_operation(a, b):
    print(a, "+", b, "=", a+b)
    print(a, "-", b, "=", a-b)
    print(a, "*", b, "=", a*b)
    print(a, "/", b, "=", a/b)

print_arithmetic_operation(3, 4)

#220
def print_max(a, b, c):
    if a > b:
        if a > c:
            print(a)
        else:
            print(c)
    else:
        if b > c:
            print(b)
        else:
            print(c)
print_max(4, 12, 3)
"""
def print_max(a, b, c) :
    max_val = 0
    if a > max_val :
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    print(max_val)
"""