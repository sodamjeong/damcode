# n = input()

# for idx in range(len(n)):
#     print(n[idx])

# for i in range(6):
#     if i % 2  == 0:
#      print(i)

# n = int(input())
# a = 0
# b = 0
# while a < n + 1:
#     b += a
#     a += 1
# print(b)


# n = int(input())
# m = 0
# for i in range(1,n+1):
#     m += i
    
# print(m)

# n = list(map(int,input().split()))
# m = n[0]

# for i in n:
#     if m > i:
#         m = i
# print(m)

# T = int(input())

# for i in range(T):
#     A, B = map(int,input().split())
#     print(A+B)


# x = int(input())
# y = int(input())

# if x > 0 and y > 0:
#     print(1)
# elif x > 0 and y < 0:
#     print(4)
# elif x < 0 and y < 0:
#     print(3)
# else:
#     print(2)   

# id = input()

# for n in id:
#     if n == id[0]:
#         print(id + '??!')

# x = list(map(int,input().split()))
# y = [1,1,2,2,2,8]

# a = y[0] - x[0]
# b = y[1] - x[1]
# c = y[2] - x[2]
# d = y[3] - x[3]
# e = y[4] - x[4]
# f = y[5] - x[5]

# print(a, b, c, d, e, f)

# A, B, C = map(int,input().split())

# print((A + B) % C)
# print(((A % C) + (B % C)) % C)
# print((A * B) % C)
# print(((A % C) * (B % C)) % C)

# A, B = map(int,input().split())
# C = int(input())
# D = B + C
# H = int(((A * 60) + D) / 60)
# M = ((A * 60) + D) % 60

# if H >= 24:
#     H -= 24

# print(H, M)

# A, B, C = map(int,input().split())

# if A == B == C:
#     print((A * 1000) + 10000)
# elif (A == B) or (A == C):
#     print((A * 100) + 1000)
# elif (B == C):
#     print((B * 100) + 1000)
# else:
#     print(max(A,B,C) * 100)

# X = int(input())
# N = int(input())
# d = 0

# for i in range(N):
#     a,b = map(int,input().split())
#     d += (a * b)
# if d == X:
#     print('YES')
# else:
#     print('NO')

# import sys

# T = int(input())


# for i in range(T):
#     a,b = map(int,sys.stdin.readline().split())
#     print(a+b)

# T = int(input())

# for i in range(1,T + 1):
#     a,b = map(int,input().split())
#     print(f'Case #{i}:',(f'{a} + {b} ='),(a+b))

# N = int(input())

# for i in range(N):
#     print(' ' * (N - i - 1) + '*' * (i+1))


# import sys

# while True:
#     try:
#         a,b = map(int,sys.stdin.readline().split())
#         print(a + b)
#     except:
#         break

# X = int(input())
# Y = X
# n = 0

# while True:
#     a = Y // 10
#     b = Y % 10
#     c = (a + b) % 10
#     Y = b * 10 + c
#     n += 1
#     if Y == X:
#         print(n)
#         break

# N, X = map(int,input().split())
# A = list(map(int,input().split()))
# n = {}

# for i in A:
#     if i < X:
#         n[i] = 1

# for key,value in n.items():
#     print(key,end = " ")


# N, X = map(int,input().split())
# A = list(map(int,input().split()))
# n = []

# for i in A:
#     if i < X:
#         n.append(i)

# for a in n:
#     print(a,end=" ")

# def cube(x,y):
#     return x + y, x - y

# print(cube(3,5))

# def cook(parameter):
#     return 'good'

# print(cook('argument'))

# def add(*x):
#         print(x)

# add(1,2,3,4,5)

# def family(**x):
#     for key, value in x.items():
#         print(key, ':', value)

# family(father = 'dong', mother = 'lee', me = 'dami', brother = 'sung')

# def fun():
#     a = 20
#     print(a)

# fun()

a = 10
def fun():
    global a
    print(a)
    a = 3

fun()
print(a)