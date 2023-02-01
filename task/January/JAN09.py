# 입출력 문제


# 1.

n = int(input()) # 5
print(n)

# 2.

a,b = list(map(int,input().split())) # 2 5
print(a,b)

# 3.

n = list(map(int,input().split())) # 1 2 3
print(*n)

# 4.

n = list(map(int,input().split())) # word1 word2 word3
m = []

for i in n:
    a = (f'word{i}')
    m.append(a)

print(*m)

# 5.
n = list(input().split()) # 1 2 3 4 5
print(' '.join(n))

# 6.

a = int(input()) # 10

print(-a, a)

# 7.

a = list(input().split()) # a b c d e
print(*a)

# 8.

print(*list(map(int,input().split()))) # 3 17 1 39 8 41 2 32 99 2

# 9.

n = list(map(int,input().split())) # 1 4 0 10 2 3 9

for i in n:
    print(i, end=' ')
