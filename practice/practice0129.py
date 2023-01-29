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
# import sys
# imput=sys.stdin.readline

# n = int(input())
# lst = []

# for _ in range(n):
#     x, y = map(int,input().split())
#     lst.append((x,y))
# lst.sort(key=lambda x:(x[1],x[0]))
# for i in lst:
#     print(*i)

# 10814 나이순 정렬

# judge = []
# num = int(input())

# for _ in range(num):
#     a, n = input().split()
#     judge.append((a,n))
# judge.sort(key=lambda x:x[0])
# age = 0
# for _ in range(num):
#     for i in judge:
#         if int(i[0]) > age:
#             print(*i)
#     age = int(i[0])

import sys
input=sys.stdin.readline

judge = []

for i in range(int(input())):
    a, n = input().split()
    judge.append((i,int(a),n))
judge.sort(key=lambda x:(x[1],x[0]))

for i in judge:
    print(*(i[1],i[2]))