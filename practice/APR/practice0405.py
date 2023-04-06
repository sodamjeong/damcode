# 프로그래머스 43162 

# def solution(n, computers):
#     answer = 0
#     visited = [0 for i in range(n)]
#     def dfs(computers, visited, start):
#         stack = [start]
#         while stack:
#             j = stack.pop()
#             if visited[j] == 0:
#                 visited[j] = 1
#             for i in range(0, len(computers)):
#                 if computers[j][i] ==1 and visited[i] == 0:
#                     stack.append(i)
#     i=0
#     while 0 in visited:
#         if visited[i] ==0:
#             dfs(computers, visited, i)
#             answer +=1
#         i+=1
#     return answer


# 백준 19532

# a, b, c, d, e, f = map(int,input().split())
# x, y = 0, 0
# for x in range(-999,1000):
#     for y in range(-999,1000):
#         if (a * x + b * y == c) and (d * x + e * y == f):
#             print(x, y)

# 1333


import sys

input = sys.stdin.readline
n = int(input())
m = sorted(list(map(int, input().split())))
for i in range(n,-1,-1):
  if i <= m[-i]:
    print(i)
    break