# 2805 나무자르기

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
tree = (list(map(int,input().split())))
x,y = 1,max(tree)

while x <= y:
    mid = (x+y) // 2
    cnt = 0
    for i in tree:
        if i > mid:
            cnt += (i-mid)
    if cnt >= m:
        x = mid + 1
    elif cnt < m:
        y = mid - 1
print(y)