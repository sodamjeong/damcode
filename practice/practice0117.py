# 1157 단어공부

# n = input().upper()
# m = {}
# value = []
# key =[]
# for i in n:
#     if i not in m:
#         m[i] = 1
#     else:
#         m[i] += 1

# for a in m:
#     value.append(m[a])

# for b in m:
#     if m[b] == max(value):
#         key.append(b)

# if len(key) > 1:
#     print('?')
# else:
#     print(*key)

# 1152  단어의 개수

# print(len(input().split()))

# 2475 검증수
# print(sum(n := [i ** 2 for i in map(int,input().split())]) % 10)
# print(sum(int(a)**2 for a in input()[::2])%10)

# 2577 숫자의 개수
# a = int(input())
# b = int(input())
# c = int(input())
# n = str(a*b*c)

# for x in range(10):
#     for y in n:
#         print(n.count(str(x)))
#         break

# 2741 n 찍기

# for i in range(1,int(input())+1):
#     print(i)

# 2742 기찍 n

# print(*reversed(range(1,int(input())+1)),sep='\n')

# 2908 상수

a, b = input().split()
print(max(int(a[::-1]),int(b[::-1])))