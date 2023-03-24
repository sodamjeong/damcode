# 1543 문서검색

# print(input().count(input()))

# def solution(quiz):
#     answer = []
#     for i in ["3 - 4 = -3", "5 + 6 = 11"]:
#         n,m = i.split('=')
#         print(n)
#         print(eval(n),m)
#         if eval(n) == int(m):
#             answer.append('O')
#         else:
#             answer.append('X')
#     return print(answer)

# print(solution(input()))

# print(eval('5 + 6') == 11)


# swea 1954 달팽이숫자

# move = [(0,1), (1,0), (0,-1), (-1,0)]

# for t in range(1,int(input())+1):
#     n = int(input())
#     snail = [[0] * n for _ in range(n)]
#     x,y = 0,-1
#     i = 1
#     j = 0
#     while i <= n*n:
#         xa = x+move[j][0]
#         yb = y+move[j][1]
#         if xa < n and yb < n and snail[xa][yb] == 0:
#             snail[xa][yb] = i
#             i += 1
#             x, y = xa, yb
#         else:
#             j = (j+1) % 4
#     print(f'#{t}')
#     for num in range(n):
#         print(*snail[num])

# 11047 동전0

n,m = map(int,input().split())
coin = [int(input()) for _ in range(n)][::-1]
cnt = 0

for i in coin:
    cnt += m // i
    m = m % i
print(cnt)