# 11659 구간 합 구하기 4
# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# num = list(map(int,input().split()))
# for i in range(m):
#     x,y = map(int,input().split())
#     print(sum(num[x-1:y]))

import sys
input = sys.stdin.readline
n,m = map(int,input().split())
num = list(map(int,input().split()))

lst = [0]*(n+1)
cnt = 0

for i in range(1,n+1):
    cnt += num[i-1]
    lst[i] = cnt

for _ in range(m):
    x, y = map(int,input().split())
    print(lst[y] - lst[x-1])


# 1439 뒤집기

# n = input()
# x = [i for i in n.split('0') if len(i)>0]
# y = [i for i in n.split('1') if len(i)>0]
# print(min(len(x),len(y)))