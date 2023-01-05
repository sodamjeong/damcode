# 문제 1
# 문자열을 입력 받고 문자열에서 e 의 개수를 구해서 출력하세요.

n = input('문자열을 입력하세요 > ')
m = 0
for i in n:
    if i == 'e':
        m += 1
print(m)

# 문제 2
# 문자열을 입력 받고, 문자열 중 알파벳 모음의 총 개수를 출력하세요.

n = input('문자열을 입력하세요 > ')
a = ['A', 'a', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
m = 0
for i in n:
    if i in a:
        m += 1
print(m)

# 문제 3
# 입력과 같은 딕셔너리 변수가 있을 때, 해당 인물의 나이를 출력하세요.   
# 나이 : 24세

dict_variable = {
    '이름': '정우영',
    '생년': '2000',
    '회사': '하이퍼그로스',
}
print((2023 - int(dict_variable['생년']) + 1),'세')


# 문제 4 
# 이름, 전화번호, 거주지 정보를 입력받아 딕셔너리 구조로 저장하고, 
# 해당 딕셔너리와 딕셔너리의 정보를 구분해서 출력하세요.

name = input('이름을 입력하세요 > ')
num = input('전화번호를 입력하세요 > ')
home = input('거주지를 입력하세요 > ')

dict_variable = {
    '이름' : name,
    '전화번호' : num,
    '거주지' : home
}

print(dict_variable)

for info in dict_variable:
    print(info,':',dict_variable[info])

# 문제 5
#이름, 전화번호, 이메일, 거주지 정보를 입력받아 출력 예시와 동일한 딕셔너리 구조를 출력하세요.

name = input('이름을 입력하세요 > ')
num = input('전화번호를 입력하세요 > ')
mail = input('이메일을 입력하세요 > ')
home = input('거주지를 입력하세요 > ')

dict_variable = {
    name : {
        '전화번호' : num,
        '이메일' : mail,
        '거주지' : home
    }
}

print(dict_variable)

# 문제 6
# 문자열을 입력받고, 문자열에서 개별 문자가 나오는 횟수를 출력하세요.

n = input('문자열을 입력하세요 > ')
dict = {}

for i in n:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

for m in dict:
    print(m,dict[m])


