# from collections import deque

# direct = [(1,0), (0,1), (-1,0), (0,-1)]
# n = int(input())
# paint = [input() for _ in range(n)]
# paint2 = []

# for i in paint:
#     j = i.replace('R','G')
#     paint2.append(j)

# def bfs(x, y, z):
#     queue.append((x, y))
#     visit[x][y] = 1
#     while queue:
#         x, y = queue.popleft()
#         for d in direct:
#             xd, yd = x + d[0], y + d[1]
#             if 0 <= xd < n and 0 <= yd < n:
#                 if z[xd][yd] == z[x][y] and visit[xd][yd] == 0:
#                     visit[xd][yd] = 1
#                     queue.append((xd,yd))

# cnt = 0
# visit = [[0]*n for _ in range(n)]
# queue = deque()                 
# for x in range(n):
#     for y in range(n):
#         if visit[x][y] == 0:
#             bfs(x, y, paint)
#             cnt += 1


# cnt2 = 0
# visit = [[0]*n for _ in range(n)]
# queue = deque()
# for x in range(n):
#     for y in range(n):
#         if visit[x][y] == 0:
#             bfs(x, y, paint2)
#             cnt2 += 1

# print(cnt, cnt2)

# 1325
# from collections import deque
# import sys
# input=sys.stdin.readline

# N,M=map(int,input().split())
# graph=[[] for _ in range(N+1)]
# for i in range(M):
#     x,y=map(int,input().split())
#     graph[y].append(x)

# def bfs(start):
#     tmp=0
#     dq=deque()
#     dq.append([start,0])
#     visited=[False]*(N+1)
#     visited[start]=True
#     while dq:
#         node,cnt=dq.popleft()
#         for i in graph[node]:
#             if visited[i]==False:
#                 visited[i]=True
#                 dq.append([i,cnt+1])
#                 tmp+=1
#     return tmp

# MAX=0
# answer=[]
# for i in range(1,N+1):
#     if graph[i]:
#         result=bfs(i)
#         if MAX < result:
#             MAX=result
#             answer=[i]
#         elif MAX==result:
#             answer.append(i)

# print(*answer)


# 1417

import heapq
candidate = [[-int(input()),-i] for i in range(int(input()))]
cnt = 0

while 1:
    heapq.heapify(candidate)
    if candidate[0][1] == 0:
        print(cnt)
        break
    else:
        cnt += 1
        n = heapq.heappop(candidate)
        n[0] += 1
        heapq.heappush(candidate,n)
        for i in candidate:
            if i[1] == 0:
                i[0] -= 1