
# # 수 정렬하기

# t = int(input())
# m = []

# for i in range(t):
#     n = int(input())
#     m.append(n)

# for x in sorted(m):
#     print(x)

# # 대표값 2
# m = []

# for i in range(5):
#     n = int(input())
#     m.append(n)

# print(sum(m)//5)
# print(sorted(m)[2])

# 커트라인

# n, k = map(int,input().split())
# x = list(map(int,(input().split())))

# if k == 1:
#     print(*sorted(x)[-k:])
# else:
#     print(*sorted(x)[-k:-k+1])

# 소수 찾기

# n = int(input())
# m = list(map(int,input().split()))
# a = 0


# for x in m:
#     cnt = 0
#     if x == 1:
#         pass
#     else:
#         for y in range(2,x + 1):
#             if x % y == 0:
#                 cnt += 1
#         if cnt == 1:
#             a += 1

# print(a)

# 소수

# m = int(input())
# n = int(input())
# a = []

# for i in range(m,n + 1):
#     cnt = 0
#     if i == 1:
#         pass
#     else:
#         for j in range(2, i + 1):
#             if i % j == 0:
#                 cnt += 1
#         if cnt == 1:
#             a.append(i)
# if len(a) == 0:
#     print(-1)
# else:
#     print(sum(a))
#     print(min(a))

# 소인수분해

# n = int(input())

# for x in range(2, n + 1):
#     if n == 1:
#         print(-1)
#     else:
#         while n % x == 0:
#             print(x)
#             n /= x
#             if n / x == 1 and n % x == 0:
#                 print(x)
#                 break
#         if n == 1:
#             break

# moo

print('''
(___)
(o o)____/
 @@      \\
  \ ____,/
  //   //
 ^^   ^^
 ''')