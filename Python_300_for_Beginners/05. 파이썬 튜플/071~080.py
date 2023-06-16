#071
my_variable = ()
print(type(my_variable))

#072
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')

#073
t = (1,)

#074
"""
t = (1, 2, 3)
t[0] = 'a'
>>> TypeError: 'tuple' object does not support item assignment
"""

#075
t = 1, 2, 3, 4
print(type(t))

#076
"""
변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
"""
t = ('a', 'b', 'c')

t = ('A', 'b', 'c')

#077
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(interest)

#078
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)
print(interest)

#079
"""
튜플 언팩킹
"""
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

#080
data = tuple(range(2, 100, 2))
print(data)