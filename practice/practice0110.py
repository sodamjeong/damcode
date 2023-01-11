# # 
# def mul(a) :
# #     return a ** 3


# print(mul(2))
# print(mul(100))


# sw 2072.
# t = int(input())
# m= []

# for i in range(1,t+1):
#     n = list(map(int,input().split()))
#     for a in n:
#         if a % 2 == 1:
#             m.append(a)
#     print(f'#{i}',sum(m))
#     m = []

# sw 1204.

# t = int(input())
# n ={}

# for i in range(1,t+1):
#     m = list(map(int,input().split()))
#     for a in m:
#         if a not in n:
#             n[a] = 1
#         else :
#             n[a] += 1



# 11654 아스키코드


# ord()함수는 문자에 맞는 아스키코드를 chr()함수는 아스키코드에 해당하는 문자를 반환


# 11720

#1
# n = int(input())
# m = int(input())
# a = 0

# while m > 0:
#     a += m % 10
#     m //= 10

# print(a)

# #2
# input()
# n = map(int,input())

# print(sum(n))

# print(sum(map(int,input())))

# sw 1204.

t = int(input())
n ={}
value = []
key = []

for i in range(1,t+1):
    tt = int(input())
    m = list(map(int,input().split()))
    for a in m:
        if a not in n:
            n[a] = 1
        else :
            n[a] += 1
    for v in n.values():
        value.append(v)
    for k in n:
        if n[k] == max(value):
            key.append(k)
    print(f'#{tt}', max(key))
    n = {}
    value = []
    key = []