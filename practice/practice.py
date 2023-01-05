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

A, B, C = map(int,input().split())

print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)