# 문제 1
n = int(input()) # 5

print(n)

# 문제 2

n = input().split()

print(' '.join(n))


# 문제 3

t = int(input())

for i in range(1,t+1):
    print(i)


# 문제 4

n = list(map(int,input().split()))

print(*n)

# 문제 5

a,b = list(map(int,input().split()))

print(a,b)

# 문제 6

n = input(). split()

print(*n)

# 문제 7

t = int(input())

for i in range(t):
    n = list(map(int,input().split()))
    print(*n)

#문제 8

t = int(input())


for i in range(t):
    n = list(map(int,input().split()))
    for a in n:
        print(a , end = ' ')