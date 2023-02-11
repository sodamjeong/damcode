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

for _ in range(int(input())):
    x,y = 1,0
    n = int(input())
    if n == 0:
        print(x, y)
    else:
        for _ in range(n):
            x,y = y,x+y
        print(x,y)
