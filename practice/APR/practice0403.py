# swea 1859

# for t in range(1,int(input())+1):
#     n = int(input())
#     price = list(map(int,input().split()))
#     sell = 0
#     cnt = 0
#     for i in reversed(price):
#         if sell < i:
#             sell = i
#         else:
#             cnt += (sell-i)
#     print(f'#{t} {cnt}')

# 1715

# import sys
# import heapq

# input = sys.stdin.readline
# num = []
# cnt = 0
# for i in range(int(input())):
#     heapq.heappush(num,int(input()))

# while len(num) != 1:
#     a = heapq.heappop(num)
#     b = heapq.heappop(num)
#     heapq.heappush(num,a+b)
#     cnt += (a+b)
# print(cnt)

# # BFS 큐

# from collections import deque

# graph_list = {1: set([3, 4]),
#               2: set([3, 4, 5]),
#               3: set([1, 5]),
#               4: set([1]),
#               5: set([2, 6]),
#               6: set([3, 5])}
# root_node = 1

# def BFS(graph, root):
#     visited = []
#     queue = deque([root])

#     while queue:
#         n = queue.popleft()
#         if n not in visited:
#             visited.append(n)
#             queue += graph[n] - set(visited)
#     return visited
  
# print(BFS(graph_list, root_node))

# # DFS 스택

# def DFS(graph, root):
#     visited = []
#     stack = [root]

#     while stack:
#         n = stack.pop()
#         if n not in visited:
#             visited.append(n)
#             stack += graph[n] - set(visited)
#     return visited

# print(DFS(graph_list, root_node))


# 1260 

from collections import deque
import sys

input = sys.stdin.readline

def bfs(start):
  queue = deque()
  queue.append(start)       
  visit_list[start] = 1   
  while queue:
    start = queue.popleft()
    BFS.append(start)
    for i in range(1, n + 1):
      if visit_list[i] == 0 and graph[start][i] == 1:
        queue.append(i)
        visit_list[i] = 1

def dfs(start):
  visit_list[start] = 1        
  DFS.append(start)
  for i in range(1, n + 1):
    if visit_list[i] == 0 and graph[start][i] == 1:
      dfs(i)

n, m, num = map(int, input().split())
DFS = []
BFS = []

graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = graph[b][a] = 1

visit_list = [0] * (n + 1)
dfs(num)
visit_list = [0] * (n + 1)
bfs(num)
print(*DFS)
print(*BFS)