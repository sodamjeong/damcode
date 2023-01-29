# 1427 소트인사이드

# print(*sorted([int(i) for i in input()])[::-1],sep='')

# 11650 좌표정렬하기
# import sys
# import heapq
# input = sys.stdin.readline
# n = int(input())
# heap = []

# for _ in range(n):
#     x, y = map(int,input().split())
#     heapq.heappush(heap,(x,y))
# for _ in range(n):
#     print(*heapq.heappop(heap))

# 11651 좌표 정렬하기 2
import sys
imput=sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    x, y = map(int,input().split())
    lst.append((x,y))
lst2 = sorted(lst, key=lambda x:x[1])
print(lst2)