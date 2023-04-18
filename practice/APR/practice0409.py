# 7576

# import sys
# from collections import deque
# input = sys.stdin.readline

# n,m = map(int,input().split())
# tomato = [list(map(int,input().split())) for _ in range(m)]
# direct = [(1,0),(-1,0),(0,1),(0,-1)]
# queue = deque()
# cnt = 0
# zero = 0

# for i in range(m):
#     for j in range(n):
#         if tomato[i][j] == 1:
#             queue.append((i,j))
# while queue:
#     x, y = queue.popleft()
#     for d in direct:
#         xd, yd = x + d[0], y + d[1]
#         if 0 <= xd < m and 0 <= yd < n:
#             if tomato[xd][yd] == 0:
#                 tomato[xd][yd] = tomato[x][y] + 1
#                 queue.append((xd,yd))
# for a in range(m):
#     for b in range(n):
#         if tomato[a][b] > cnt:
#             cnt = tomato[a][b] - 1
#         elif tomato[a][b] == 0:
#             zero += 1
# if zero > 0:
#     print(-1)
# else:
#     print(cnt)

import pprint

direct = [(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1),(-1,1),(1,-1)]
board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
def solution(board):
    answer = 0
    n = len(board)
    visit = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1 and visit[x][y] == 0:
                visit[x][y] = 1
                for d in direct:
                    xd, yd = x + d[0], y + d[1]
                    if 0 <= xd < n and 0 <= yd < n and board[xd][yd] == 0:
                        board[xd][yd] = 1
                        visit[xd][yd] = 1
    for i in board:
        answer += i.count(0)
    pprint.pprint(board)
    pprint.pprint(visit)
    return answer
print(solution(board))