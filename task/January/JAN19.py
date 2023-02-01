# 2576 홀수
s = []
for i in range(7):
    if (n:=int(input())) % 2 == 1:
        s.append(n)
if len(s)==0:
    print('-1')
else:
    print(f'{sum(s)}\n{min(s)}')

# 10822 더하기
print(sum(map(int,input().split(','))))

# 2754 학점계산

n = list(input())
i = float('FDCBA'.index(n[0]))

if len(n)==1:
    print(i)
else:
    if n[1] == '+':
        print(i+0.3)
    elif n[1] == '-':
        print(i-0.3)
    else:
        print(i)

# 5622 다이얼

n = input()
m = {
    'ABC':3,'DEF':4,'GHI':5,
    'JKL':6,'MNO':7,'PQRS':8,
    'TUV':9,'WXYZ':10
}
time = []
for x in n:
    for y in m:
        if x in y:
            time.append(m.get(y))
print(sum(time))

# 2577 숫자의 개수

n = [int(input())for i in range(3)]
m = str(n[0]*n[1]*n[2])

for i in range(10):
        print(m.count(str(i)))

# 7785 회사에 있는 사람

import sys
input = sys.stdin.readline
office = {}

for i in range(int(input())):
    log = input().split()
    if log[0] not in office:
        office[log[0]] = 1
    else:
        del office[log[0]]

print(*sorted(office)[::-1],sep='\n')