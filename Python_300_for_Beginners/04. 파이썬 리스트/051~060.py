#051
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']

#052
movie_rank.append('배트맨')

#053
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, '슈퍼맨')

#054
movie_rank.remove('럭키')
"""
del movie_rank[3]
"""

#055
movie_rank.remove('스플릿')
movie_rank.remove(('배트맨'))
"""
del movie_rank[2]
del movie_rank[2]
"""


#056
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

#057
nums = [1, 2, 3, 4, 5, 6, 7]
print(max(nums))
print(min(nums))

#058
nums = [1, 2, 3, 4, 5]
print(sum(nums))

#059
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

#060
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))