# 문제 1
# 정수 한 개를 입력 받고, 
# 해당 숫자가 0보다 큰 숫자라면 True 아니면 False를 출력하세요.

n = int(input('숫자를 입력해주세요 > '))

if n > 0:
    print(True)
else:
    print(False)

# 문제 2
# 정수 두 개를 입력 받고, 크기가 더 큰 정수를 출력하세요.
# 두 정수가 같으면 False를 출력하세요.

n = int(input('첫 번째 숫자를 입력해주세요 >'))
m = int(input('두 번째 숫자를 입력해주세요 > '))

if n == m:
    print(False)
elif n > m:
    print(n)
else:
    print(m)

# 문제 3 
# 정수 한 개를 입력 받고, 해당 정수가 1 보다 크고, 
# 10보다 작다면 True 아니면 False를 출력하세요.
# 
n = int(input('숫자를 입력해주세요 > '))

if n > 1 and n < 10:
    print(True)
else : 
    print(False)

# 문제 4
# 정수 한 개를 입력 받고 0 보다 크고, 
# 짝수라면 True 아니면 False를 출력하세요.

n = int(input('숫자를 입력해주세요 > '))

if (n > 0) and (n % 2 == 0):
    print(True)
else:
    print(False)

# 문제 5
# 정수 한 개를 입력 받고, 아래 조건에 따라 출력하세요.

# 값이 100 초과 / 0 미만이면 "에러" 출력
# 값이 60 이상이면 "합격" 출력
# 값이 60 미만이면 "불합격" 출력

n = int(input('숫자를 입력해주세요 > '))

if  n >= 0 and n < 60:
    print('불합격')
   
elif n >=60 and n <= 100:
    print('합격')
else:
    print('에러')

# 문제 6
# 문자열을 입력 받고, 입력 받은 문자열을 반대로 한 글자씩 출력하세요.

n = input('문자열을 입력하세요 > ')

#1
for idx in range(1, len(n) + 1):
    print(n[-idx])

#2
for idx in n[::-1]:
    print(idx)

# 문제 7
# 정수 두 개를 입력 받고, 두 수 사이의 정수를 오름차순으로 출력하세요.
# 두 값이 같으면 False를 출력하세요

#1
n = int(input('첫 번째 숫자를 입력하세요 > '))
m = int(input('두 번째 숫자를 입력하세요 > '))

if n > m:
    for idx in range(m+1, n, 1):
        print(idx)
elif m>n:
    for idx in range(n+1, m, 1):
        print(idx)
else:
    print(False)

#2
n = int(input("첫 번째 정수를 입력하세요 > "))
m = int(input("두 번째 정수를 입력하세요 > "))

for idx in range(min(n,m)+1, max(n,m)):
    print(idx)
if n == m:
    print("False")

# 문제 8
# 정수 두 개를 입력 받고, 두 수 사이의 정수를 내림차순으로 
# 한 줄에 모두 출력하세요. 두 값이 같으면 False를 출력하세요

n = int(input('첫 번째 숫자를 입력하세요 > '))
m = int(input('두 번째 숫자를 입력하세요 > '))

#1
if n > m:
    for idx in range(n-1, m, -1):
        print(idx, end=" ")
elif m > n:
    for idx in range(m-1, n, -1):
        print(idx, end=" ")
else:
    print(False)

#2
n = int(input("첫 번째 정수를 입력하세요 > "))
m = int(input("두 번째 정수를 입력하세요 > "))

for idx in range(max(n,m)-1, min(n,m), -1):
    print(idx, end=" ")
if n == m:
    print("False")

# 문제 9
# 정수 한 개를 입력 받고, 1 부터 입력 값 사이의 정수 중 홀수만 출력하세요.
# 입력 값이 1보다 작으면 False를 출력하세요.

n = int(input('숫자를 입력하세요 > '))

if n < 1:
    print(False)
else:
    for idx in range(1,n,2):
        print(idx)

# 문제 10
# 구구단을 출력하세요.

for n in range(1,10):
    for m in range(1,10):
        print(n,'x',m,'=',n*m)