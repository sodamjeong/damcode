# 10818

# N = int(input())
# n = list(map(int,input().split()))

# print(min(n), max(n))


# 2562

# A = []

# for i in range(9):
#     a = int(input())
#     A.append(a)

# print(max(A)) 
# print(A.index(max(A))+1)


# 5597

# n = []
# a = list(range(1,31))

# for i in range(28):
#     b = int(input())
#     n.append(b)

# for num in a:
#     if num not in n:
#         print(num) 

# 3052

# n = []
# m = {}

# for i in range(10):
#     a = int(input())
#     b = a % 42
#     n.append(b)

# for num in n:
#     if num not in m:
#         m[num] = 1
#     else:
#         m[num] += 1

# print(len(m))

# 3052_2

# n = []

# for i in range(10):
#     a = int(input())
#     b = a % 42
#     n.append(b)

# print(len(set(n)))

# 1546

# n = int(input())
# a = list(map(int,input().split()))

# print(round(((sum(a)/n)/max(a))*100,3))

# 8958

# t = int(input())

# for i in range(t):
#     n = 0
#     m = 0
#     ox = list(input())
#     for num in ox:
#         if num == 'O':
#             n += 1
#             m += n
#         else:
#             n = 0
#     print(m)

# 4344

C = int(input())

for i in range(C):
    score = list(map(int,input().split()))
    n = sum(score[1:])/score[0]
    m = 0
    for a in score[1:]:
        if a > n :
            m += 1
    percent = m / score[0] * 100
    print(f'{percent:.3f}%')

