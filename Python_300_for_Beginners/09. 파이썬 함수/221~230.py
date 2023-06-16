#221
def print_reverse(string):
    print(string[::-1])
print_reverse("python")

#222
def print_score(a):
    sum = 0
    for i in a:
        sum += i
    result = sum/len(a)
    print(result)
print_score([1, 2, 3])

#223
def print_even(l):
    for i in l:
        if i % 2 == 0:
            print(i)
print_even ([1, 3, 2, 10, 12, 11, 15])

#224
def print_keys(d):
    for keys in d.keys():
        print(keys)
print_keys ({"이름":"김말똥", "나이":30, "성별":0})

#225
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
def print_value_by_key(dict, key):
    print(dict[key])

print_value_by_key  (my_dict, "10/26")

#226
def print_5xn(string):
    x = len(string) // 5
    for i in range(x+1):
        print(string[5*i:5*(i+1)])

print_5xn("아이엠어보이유알어걸")

#227
def printmxn(string, number):
    x = len(string) // number
    for i in range(x+1):
        print(string[number*i:number*(i+1)])

printmxn("아이엠어보이유알어걸", 3)

#228
def calc_monthly_salary(n):
    print(n//12)
calc_monthly_salary(12000000)

#229
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)

#230
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)
