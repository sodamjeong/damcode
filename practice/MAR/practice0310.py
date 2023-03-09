# swea 1217 거듭 제곱 

# for _ in range(10):
#     t = int(input())
#     n,m = map(int,input().split())
#     print(f'#{t}',n**m)

# 재귀함수사용


# def power(n,m):
#     global num
#     if m < 2:
#         return num
#     else:
#         num *= n
#         return(power(n,m-1))

# for _ in range(10):
#     t = int(input())
#     n,m = map(int,input().split())
#     num = n
#     print(f'#{t}',power(n,m))


# 17219 비밀번호 찾기
import sys
input=sys.stdin.readline

n,m = map(int,input().split())
memo = {}
for _ in range(n):
    k,v = input().split()
    memo[k] = v
for _ in range(m):
    site = input().strip()
    print(memo[site])