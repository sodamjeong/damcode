# 문제 1

a, b = map(int,input().split())
print(a+b)

# 문제 2

a = int(input())
b = int(input())
print(a + b)

# 문제 3

t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    print(a+b)

# 문제 4
t = int(input())

for i in range(t):
    a,b = map(int,input().split(','))
    print(a+b)

# 문제 5

t = int(input())

for i in range(1,t+1):
    a,b = map(int,input().split())
    print(f'Case #{i}:',a+b)

# 문제 6

t = int(input())

for i in range(1,t+1):
    a,b = map(int,input().split())
    print(f'Case #{i}: {a} + {b} = {a+b}')