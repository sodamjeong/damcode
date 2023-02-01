# 2525 오븐시계

h,m=map(int,(input()).split())
cook = h*60+m+int(input())
h2 = cook//60
m2 = cook% 60
if h2 >= 24:
    print((h2)-24,m2)
else:
    print(h2,m2)

# 2798 블랙잭

n,m = map(int,input().split())
card = list(map(int,input().split()))
c = []
for x in range(0, n-2):
    for y in range(x+1, n-1):
        for z in range(y+1,n):
            t = card[x]+card[y]+card[z]
            if t <= m:
                c.append(t)
print(max(c))

# 9076 점수 집계

for _ in range(int(input())):
    point = list(map(int,input().split()))
    point.sort()
    if point[3] - point[1] > 3:
        print('KIN')
    else:
        print(sum(point[1:4]))

# 1526 가장 큰 금민수

n = int(input())
while 1:
    num = True
    for i in str(n):
        if i!="4" and i!="7":
            num = False
            n -= 1
    if num :
        print(n)
        break

# 1436 영화감독 숌

part = 666
series = int(input())
cnt = 0
while 1:
    if ('666') in str(part):
        cnt += 1
        if cnt == series:
            break
    part += 1
print(part)