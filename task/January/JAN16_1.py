# 10039 평균 점수

x =[]
for i in range(5):
    n = int(input())
    if n < 40:
        n = 40
    x.append(n)

print(sum(x)//5)

# 10871 x 보다 작은 수 

n, x = map(int,input().split())
a = list(map(int,input().split()))
b = []

for i in a:
    if i < x:
        b.append(i)
print(*b)

# 2480 주사위 세개

a, b, c = map(int,input().split())
x = [a, b, c]
  
if a == b == c:
    print(10000 + 1000 * a)
elif len(set(x)) == 2 :
    print(1000 + (100 * sorted(x)[1]))
else:
    print(100 * max(x))

# 10886 0 = not cute / 1 = cute

n = int(input())
x =[]

for i in range(n):
    a = int(input())
    x.append(a)

if x.count(0) > x.count(1):
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')

# 2506 점수계산

n = int(input())
x = list(map(int,input().split()))
n = 0
m = []

for i in x:
    if i == 1:
        n += 1
        m.append(n)
    else:
        n = 0

print(sum(m))