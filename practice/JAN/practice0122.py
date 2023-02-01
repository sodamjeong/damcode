# 10250 ACM호텔

# for i in range(int(input())):
#     h, w, n = map(int,input().split())
#     for x in range(1,w+1):
#         for y in range(1,h+1):
#             n -= 1
#             if n == 0:
#                 if x < 10:
#                     print(f'{y}0{x}')
#                 else:
#                     print(str(y)+str(x))

# 2775 부녀회장이 될테야

# for _ in range(int(input())):
#     n = [i for i in range(1,15)]
#     h = int(input())
#     r = int(input())
#     for x in range(h):
#         m = []
#         for y in range(1,r+1):
#             m.append(sum(n[0:y]))
#         n = m
#     print(n[-1])

# 10757 큰수 a+b

# import sys
# input = sys.stdin.readline

# a = list(map(int,input().split()))
# print(sum(a))

# 1929 소수 구하기
# import sys
# input = sys.stdin.readline

# def prime(i):
#     if i < 10:
#         if i in [2,3,5,7]:
#             return True
#     else:
#         for x in range(2,int(i**0.5)+1):
#             if i % x == 0:
#                 return False
#         return True

# m,n = map(int,input().split())

# for i in range(m,n+1):
#     if prime(i):
#         print(i)

# n, m = map(int, input().split())
# lst = list(range(m + 1)) # 0~m 까지의 리스트
# for i in lst[2:]: # (0 과 1은 제외)
#     if lst[i] >= n: # (n 보다 큰수만 출력)
#         print(i)
#     lst[i::i] = m//i * [0] 
    # (i의 배수 자리에 있는 수는 소수가 아니므로 0으로 대입하여 출력하지 않도록 함, 
    # 0의 갯수는 제일 큰수를 i로 나눈 몫으로 도출할 수 있다.)
    # 리스트는 2부터 시작하므로 2의 배수, 3의 배수, 5의 배수, 7의 배수 순으로 모두 제거할 수 있다.


# 4948 베르트랑 공준

# import sys
# input = sys.stdin.readline

# def prime(n):
#     m = []
#     lst = list(range((n*2)+1))
#     for i in lst[2:]:
#         if lst[i] > n:
#             m.append(i)
#         lst[i::i] = ((n*2)//i) * [0]
#     print(len(m))

# while 1:
#     n = int(input())
#     if n == 0:
#         break
#     else:
#         prime(n)

# 2566 최댓값

# n = {}
# m = []
# for i in range(1,10):
#     n[i] = list(map(int,input().split()))
#     m.append(max(n[i]))
# print(max(m))
# for x in n:
#     if max(m) in n[x]:
#         print(x,n[x].index(max(m))+1)

# 1316 그룹단어체커
# cnt = 0
# for _ in range(int(input())):
#     n = input()
#     m = []
#     for i in range(len(n)):
#         if n[i] not in m:
#             m.append(n[i])
#         else:
#             if n[i] == n[i-1]:
#                 m.append(n[i])
#             else:
#                 m.clear()
#                 break
#     if len(m) > 0:
#         cnt += 1
# print(cnt)

# 4153 직각삼각형

# while 1:
#     n = list(map(int,input().split()))
#     m = sorted(n)
#     if sum(m) == 0:
#         break
#     if m[2]**2 == (m[0]**2+m[1]**2):
#         print('right')
#     else:
#         print('wrong')

# 10989 수 정렬하기 3
# import sys
# input=sys.stdin.readline

# n = [0] * 10001

# for i in range(int(input())):
#     n[int(input())] += 1
# for i in range (1, 10001):
#     for x in range(n[i]):
#         print(i)

# 2231 분해합

# n = int(input())
# for i in range(n+2):
#     m = list(str(i))
#     num = i + sum(map(int,m))
#     if i > n:
#         print(0)
#     else:
#         if n == num:
#             print(i)
#             break
# 2751 수 정렬하기 2
# import sys
# input=sys.stdin.readline

# print(*sorted([int(input()) for i in range(int(input()))]),sep='\n')

# 1181번 단어정렬

# n = sorted(set([input() for _ in range(int(input()))]))
# m = []
# for x in range(51):
#     for y in n:
#         if len(y) == x:
#             m.append(y)
# print(*(m),sep='\n')

# 9012 괄호

# for i in range(int(input())):
#     n = input()
#     cnt = 0
#     for x in n:
#         if x == '(':
#             cnt += 1
#         elif x == ')':
#             cnt += -1
#             if cnt < 0:
#                 print('NO')
#                 break
#     if cnt == 0:
#         print('YES')
#     elif cnt > 0:
#         print('NO')

# 2798 블랙잭

# n,m = map(int,input().split())
# num = list(map(int,input().split()))
# new_num=[]
# i = 0
# while i < n:
#     for x in num[i:]:
#         for y in num[i+1:]:
#             for z in num[i+2:]:
#                 print(x,y,z)
#     i += 1
    
# #                 a = x+y+z
# #                 if a <= m:
# #                     new_num.append(a)
# # print(max(set(new_num)))

# 블랙잭 다시 생각해보기