#151
리스트 = [3, -20, -3, 44]
for i in 리스트:
    if i <0:
        print(i)

#152
리스트 = [3, 100, 23, 44]
for i in 리스트:
    if i % 3 ==0:
        print(i)

#153
리스트 = [13, 21, 12, 14, 30, 18]
for i in 리스트:
    if i % 3 == 0 and i < 20:
        print(i)

#154
리스트 = ["I", "study", "python", "language", "!"]
for i in 리스트:
    if len(i) >= 3:
        print(i)

#155
리스트 = ["A", "b", "c", "D"]
for i in 리스트:
    if i.isupper() == 1:
        print(i)

#156
리스트 = ["A", "b", "c", "D"]
for i in 리스트:
    if i.islower() == 1:
        print(i)

#157
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i[0].upper() + i[1:])

#158
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for i in 리스트:
    print(i.split(".")[0])

#159
tmp = []
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    if i.split(".")[1] == 'h':
        tmp.append(i)

for i in tmp:
    print(i)

#160
tmp = []
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    if i.split(".")[1] == 'h' or i.split(".")[1] =='c':
        tmp.append(i)

for i in tmp:
    print(i)