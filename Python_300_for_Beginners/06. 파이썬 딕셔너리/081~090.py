#081
"""
>> a, b, *c = (0, 1, 2, 3, 4, 5)
>> a
0
>> b
1
>> c
[2, 3, 4, 5]
"""
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*vallid_score, a, b = scores
print(vallid_score)

#082
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *vallid_score = scores
print(vallid_score)

#083
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *vallid_score, b = scores
print(vallid_score)

#084
temp = {}
print(type(temp))

#085
cookie = {'메로나':'1000', '폴라포':'1200', '빵빠레':'1800'}
print(cookie)

#086
cookie = {'메로나':'1000', '폴라포':'1200', '빵빠레':'1800'}
cookie['죠스바'] = 1200
cookie['월드콘'] = 1500
print(cookie)

#087
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print(ice['메로나'])

#088
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
ice['메로나'] = 1300
print(ice)

#089
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
ice.pop('메로나')
print(ice)

#090
icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream['누가바']
"""
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    icecream['누가바']
KeyError: '누가바'
"""