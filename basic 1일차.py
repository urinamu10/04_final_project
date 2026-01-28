# # 변수: 값을 담는 그릇

# a = '100' # 문자(str)
# b = 3 # 숫자, 정수(int)

# # type(a)
# print(type(a)) # <class 'str'>
# print(type(b)) # <class 'int'>

# # 자료형 -> 값 자체 
# # 문자 
# # 숫자, 정수
# # 숫자, 실수
# # 논리형 boolean
# # None


# # 데이터를 가져올 때(크롤링) 주식 가격, 부동산 경매가격
# # 숫자형처럼 보이지만 타입이 문자열인 경우가 대다수

# int(a) + b # '100' -> 100 + 3 = 103 
# a + str(b) # 3 -> '3' -> '100' + '3' = '1003'
# # 문자열 연산 + x -> +: 두 문자를 이어주는 것 / x: 반복
# # float(b) # 3 -> 3.0 

# # 문자열(str) 
# email ='student@example.com' # 자리 번호(인덱스 번호), 순서 있음
# # 슬라이싱
# id = email[0:7] # [입력값:뒤의자리번호+1]
# # id = email[:7]
# address = email[8:17]
# # adress = email[8:] # 맨 뒤의 인덱스는 생략가능
# # 문자열 뒤집기
# # a b c -> c b a 
# # email[::-1]

# # 대문자 
# # 'Python', 'python'
# # 'python'.upper()

# # 공백 제거 
# ' hi '.strip()

# # 분리하는 함수 
# div = 'a,b,c'.split(',')
# print(div) # ['a', 'b', 'c'] # 리스트 형태로 반환되기 때문에 리스트로 다뤄주어야함

# # 리스트, 딕셔너리, 튜플, 셋 -> 자료 구조

# # 리스트 
# # 여러개의 데이터 순서 O, 값이 변경 O -> 비슷한 값들을 다룰 때 
# scores = [90, 80, 70, 90]

# scores1 = scores.append(60) # 값 추가 [마지막에]
# scores2 = scores.count(90) # 90이 몇개 있는가?
# scores3 = scores[1:3]

# print(scores1)
# print(scores2)
# print(scores3)


# # 딕셔너리 
# # 키:값 -> 값에 대한 정보를 더 자세히 표현해줄 때 
# user = {'name': 'Tom', 'age': 25}

# # 특정 값을 가져올 때
# # user['name'] -> 'Tom'
# # user['job'] -> Error

# user['job'] = 'developer'  # 새로운 키/값 추가
# user.get('age')            # 안전하게 값 찾기 

# # 문자열 파싱 연습
# # 사용자명(username)
# # 도메인(domain) 을 분리하여 출력
# email = 'hello.world_99@naver.com'

# username = email.split('@')[0]
# domail = email.split('@')[1]

# # 문자열 숫자 정규화 
# data1 = '1,200' 
# data2 = '10.5%'
# data3 = ' 300 ' 

# # replace('바꿔야 하는것', '바꾼 것')
# data1 = int(data1.replace(',', ''))
# print(data1)
# data2 = float(data2.replace('%','')) / 100 # 0.105 -> 10.5% 
# print(data2)
# data3 = data3.strip()
# print(data3)

# # 리스트 필터링 & 컴프리헨션
# # [표현 반복 조건]

# passed = []
# scores = [95, 50, 82, 100, 59, 88]
# for score in scores:
#     if score >= 60:
#         passed.append(score)

# [score for score in scores if score >= 60]

# result = []
# for score in scores:
#     if score >= 90:
#         result.append('pass')
#     else:
#         result.append('Fail')

# ['pass' if score >= 90 else 'Fail' for score in scores]


# # 딕셔너리 변환
# info = 'name=TOM, age=20, city=Seoul' # 값을 구분(문자열 하나 -> 여러 개)
# # 값을 구분 
# items = info.split(',')
# print(items)

# # 공백 제거 <--------------- 손코딩 과제
# result = {}
# for item in itmes:
#     key, value = item.split('=') # 결과가 두 개
#     # 1: key name, value tom
#     # 2: key age, value 20 
#     # 3: key city, value Seoul 
#     result[key.strip()] = value
#     # result[name] = Tom
#     # result[age] = 20
    # result[city] = Seoul

# 과제 2

# 아래 raw 데이터를 정리해 딕셔너리 리스트로 변환
raw = [
    "name=Kim;score=90",
    "name=Lee;score=77",
    "name=Park;score=100"
]

result= []
for item in raw:
    pairs = item.split(';')

    new_dict = {}
    for pair in pairs:
        key, value = pair.split('=')

        if key == 'score':
            new_dict[key] = int(value)
        else:
            new_dict[key] = value
    result.append(new_dict)

print(result) 


DFDFD

