# 입출력 문제

# 1.

n = list(map(int,input().split()))
print(*n)

# 2.

n = list(input().split())
print(' '.join(n))

# 3.

t = int(input())

for i in range(1,t + 1):
    n = int(input())
    for _ in range(n):
        m = input()
        print(m)

# 4.

t = int(input())

for i in range(1, t + 1):
    n = int(input())
    for a in range(1, n + 1):
        m = input()
        print(m)

# 5.

import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for i in range(1, t + 1):
    n = int(input())
    for a in range(n):
        m = input()
        print(m)

# 6.

t = int(input())

for i in range(1, t + 1):
    n = int(input())
    for a in range(n):
        m = list(map(int,input().split()))
        for b in m:
            print(b, end = ' ')

# 7.

t, w = map(int,input().split())

for i in range(1, t + 1):
    for n in range(w):
        m = input()
        print(m)

# 8.

t, w = map(int,input().split())

for i in range(t, t + 1):
    for _ in range(1 , w + 1):
        m = input()
        print(m)

# 9.

t, w = map(int,input().split())

for i in range(t):
    for _ in range(w):
        m = input()
        print(m)