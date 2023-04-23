# 1916
# import heapq
# import sys
# input = sys.stdin.readline

# n, m = int(input()), int(input())
# bus = [[] for _ in range(n+1)]
# for _ in range(m):
#     x, y, z = map(int,input().split())
#     bus[x].append((y,z))
# start, end = map(int,input().split())

# def dijkstra(bus, start):
#     dist = [int(1e9)] * (n+1)
#     dist[start] = 0
#     queue = []
#     heapq.heappush(queue, [dist[start], start])

#     while queue:
#         cd, cn = heapq.heappop(queue)
#         if dist[cn] < cd:
#             continue
        
#         for tn,td in bus[cn]:
#             cost = cd + td
#             if dist[tn] > cost:
#                 dist[tn] = cost
#                 heapq.heappush(queue,(cost,tn))
#     return dist[end]

# print(dijkstra(bus,start))



# 4485
# import heapq
# import sys
# input = sys.stdin.readline

# def dijkstra():
#     direct = [(1,0),(-1,0),(0,1),(0,-1)]
#     rupee = [[int(1e9)] * n for _ in range(n)]
#     rupee[0][0] = field[0][0]
#     queue = []

#     heapq.heappush(queue,(0,0,rupee[0][0]))
#     while queue:
#         x,y,cost = heapq.heappop(queue)

#         if rupee[x][y] < cost:
#             continue
#         for d in direct:
#             xd, yd = x + d[0], y + d[1]
#             if 0 <= xd < n and 0 <= yd < n:
#                 pay = field[xd][yd] + cost
#                 if pay < rupee[xd][yd]:
#                     rupee[xd][yd] = pay
#                     heapq.heappush(queue,(xd,yd,pay))
#     return rupee


# case = 0
# while 1:
#     case += 1
#     n = int(input())
#     if n == 0:
#         break

#     field = [list(map(int,input().split())) for _ in range(n)]
#     print(f'Problem {case}: {dijkstra()[-1][-1]}')
    
# swea 9700
# import heapq

# for t in range(1,int(input())+1):
#     p, q = map(float,input().split())
#     a= [((1-p) * q, 'YES'), (p * (1-q) * q, 'NO')]
#     heapq.heapify(a)
#     print(f'#{t} {heapq.heappop(a)[1]}')

# 11726

import sys
input = sys.stdin.readline
n = int(input())
tile = [0, 1, 2]
for i in range(3,n+1):
    tile.append((tile[i-1]+tile[i-2])%10007)
print(tile[n])

