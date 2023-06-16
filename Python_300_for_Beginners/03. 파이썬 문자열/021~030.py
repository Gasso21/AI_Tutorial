#021
letters = 'python'
print(letters[0], letters[2])

#022
license_plate = "24가 2210"
print(license_plate[-4:])

#023
string = "홀짝홀짝홀짝"
print(string[::2])

#024
string = "PYTHON"
print(string[::-1])

#025
phone_number = "010-1111-2222"
print(phone_number.replace('-',' '))

#026
phone_number = "010-1111-2222"
print(phone_number.replace('-',''))

#027
url = "http://sharebook.kr"
print(url[-2:])

print(url.split("."))
print(url.split(("."))[-1])

#028
"""
lang = 'python'
lang[0] = 'P'
print(lang)
"""
"""
문자열은 수정할 수 없음
TypeError: 'str' object does not support item assignment
"""

#029
string = 'abcdfe2a354a32a'
print(string.replace("a", 'A'))

#030
string = 'abcd'
string.replace('b', 'B')
print(string)
"""
replace 메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴
문자열은 변경할 수 없는 자료형이기 때문에 abcd가 그대로 출력
"""