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

# 1003 피보나치 함수
# import sys
# input = sys.stdin.readline

# def fibonacci(n):
#         global cnt
#         if n == 0:
#             cnt[n] += 1
#         elif n == 1:
#             cnt[n] += 1
#         else:
#          fibonacci(n-1), fibonacci(n-2)
            
# for _ in range(int(input())):
#     cnt = {0:0,1:0}
#     fibonacci(int(input()))
#     print(cnt[0],cnt[1])
# # 시간초과

# 1920 수 찾기
# import sys
# input = sys.stdin.readline

# input()
# lst = {i : 1 for i in list(map(int,input().split()))}
# input()
# for i in list(map(int,input().split())):
#     print(lst.get(i,0))