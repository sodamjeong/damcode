#백준 셀프넘버


# def d(n):
#     return i + sum(map(int,str(i)))

# a = []

# for i in range(1, 10001):
#         a.append(d(i))

# a.sort()

# for n in range(1,10001):
#     if n not in a:
#         print(n)


# 한수


# def han(x):
#     a = str(x)
#     if int(a[0]) - int(a[1]) == int(a[1]) - int(a[2]):
#         return x

# N = int(input())
# n = []

# for i in range(1,N+1):
#     if i >= 100:
#         n.append(han(i))
#     else:
#         n.append(i)

# print(len(n)-n.count(None))

# 알파벳 찾기

# a = input()
# for i in map(chr,range(97,123)):
#     print(a.find(i), end =' ')

# 크로아티아 알파벳

# a = input()
# b = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
# n = 0
# m = 2

# x = a.replace('=','')
# y = x.replace('-','')
# z = 1

# while m < (len(y) + 1):
#     if y[n:m] not in b:
#         z += 1
#     n += 1
#     m += 1

# z -= a.count('dz=')

# print(z)

# a = input()
# b = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# for i in b:
#     a = a.replace(i,'1')

# print(len(a))

# 문자열 반복

t = int(input())
x = []
y = []

for i in range(t):
    a,b = input().split()
    for n in b:
        x.append(n)
    for m in x:
        y.append(m*int(a))
    print(''.join((y)))
    x.clear()
    y.clear()
