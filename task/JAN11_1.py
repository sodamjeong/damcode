# SWEA

#2047. 신문 헤드라인

n = input()
print(n.upper())

# 2025. N줄덧셈

n = int(input())
m = 0

for i in range(1,n+1):
    m += i
print(m)

# 1936. 1대1 가위바위보

a, b = map(int,(input().split()))

if (a - b) < 0:
    if b == 3 and a == 1:
        print('A')
    else:
        print('B')
else:
    if a == 3 and b == 1:
        print('B')
    else:
        print('A')

# 2027. 대각선 출력하기

print('#++++\n+#+++\n++#++\n+++#+\n++++#')

# 2058. 자릿수 더하기

n = int(input())
m = 0
while n > 0:
    m += n % 10
    n //= 10
print(m) 

# 2019. 더블더블

n = int(input())
m = [1]

for i in range(1,n+1):
    m.append(2**i)
print(*m)