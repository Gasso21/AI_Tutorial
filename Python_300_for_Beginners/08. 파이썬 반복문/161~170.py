#161
for i in range(100):
    print(i)

#162
for i in range(2002, 2051):
    if i % 4 == 0:
        print(i)

"""
for x in range(2002, 2051, 4) :
    print (x)
"""

#163
for i in range(1, 31):
    if i % 3 ==0:
        print(i)

"""
for num in range(3, 31, 3):
    print (num)
"""

#164
for i in range(99, -1, -1):
    print(i)

"""
for i in range(100):
    print(99 - i)
"""

#165
for i in range(0, 10):
    print("0.%d" %i)

"""
for num in range(10) :
    print(num / 10)
"""

#166
for i in range(1, 10):
    print("3x%d" %i, "=", i*3)

#167
for i in range(1, 10,2):
    print("3x%d" %i, "=", i*3)

#168
result = 0
for i in range(1, 11):
    result += i
print(result)

#169
result = 0
for i in range(1, 11,2):
    result += i
print(result)

#170
result = 1
for i in range(1, 11):
    result *= i
print(result)
