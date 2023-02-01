# 1193 분수찾기

# n = int(input())
# m = 1

# while n > m:
#     n -= m
#     m += 1
# if m % 2 == 0:
#     x = n
#     y = m - n + 1
# else:
#     x = m - n + 1
#     y = n
# print(f'{x}/{y}')

# 2609 최대공약수와 최소공배수

a,b = map(int,input().split())
n = []
for x in range(1,a+b):
    if a % x == 0 and b % x == 0:
        n.append(x)
m = max(n)        
print(m)
print(m*(a//m)*(b//m))