# 문법문 아랫줄 띄어쓰기 4칸(스페이스4번)

if 5 > 3:
    print('크다!')
else:
    print('작다!')

if 5 < 3:
    print('크다!')
    print('!!!!')
else:
    print('작다!')



a = -10 
if a >= 0 :
    print('양수')
else:
    print('음수')
print(a)


num = int(input('숫자를 입력하세요 >'))
if num % 2 == 1:
    print('홀수')
else:
    print('짝수')

#1
dust = int(input('오늘의 미세먼지 농도는?'))
if dust <= 30:
    print('좋음')
elif dust >30 and dust <= 80:
    print('보통')
elif dust >80 and dust <= 150:
    print('나쁨')
else:
    print('매우나쁨')

#2
dust = int(input('오늘의 미세먼지 농도는?'))
if dust > 150:
    print('매우나쁨')
    if dust > 300:
        print('실외 활동을 자제하세요.')
elif dust >80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    if dust >= 0 :
        print('좋음') 
    else:
        print('잘못 입력 되었습니다.')


n = int(input("첫 번째 정수를 입력하세요 > "))
m = int(input("두 번째 정수를 입력하세요 > "))

for idx in range(max(n,m)-1, min(n,m), -1):
    print(idx, end=" ")
if n == m:
    print("False")
