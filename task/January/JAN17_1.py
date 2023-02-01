# 9085 더하기
for i in range(int(input())):
    _ = input()
    print(sum(a := (list(map(int,input().split())))))

# 10824 네수

n = list(input().split())
a = n[0]+n[1]
b = n[2]+n[3]

print(int(a)+int(b))

# 3009 네 번째 점

x = {}
y = {}

for i in range(3):
    a, b = list(map(int,input().split()))
    if a not in x:
        x[a] = 1
    else:
        x[a] +=1
    if b not in y:
        y[b] = 1
    else:
        y[b] += 1

for v in x:
    if x[v] == 1:
        print(v,end=' ')
        for v2 in y:
            if y[v2] == 1:
                print(v2)

# 10952 A+B - 5

while 1:
    a, b = map(int,input().split())
    if a + b > 0:
        print(a+b)
    if a + b == 0:
        break

# 1110 더하기 사이클

n = int(input())
m = n
cnt = 0

while 1:
    a = m // 10
    b = m % 10
    m = (b * 10) + ((a + b) % 10)
    cnt += 1
    if m == n:
        print(cnt)
        break