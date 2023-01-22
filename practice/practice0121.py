# 2738 행렬덧셈

# n,m = map(int,input().split())
# lst = [input().split() for _ in range(n)]

# for x in lst:
#     plus = list(map(int,(input().split())))
#     a = 0
#     for y in x:
#         print(int(y) + plus[a], end = ' ')
#         a += 1

# 2869  달팽이는 올라가고 싶다

import sys
input = sys.stdin.readline

a,b,v = map(int,input().split())

if (v-a)%(a-b) > 0:
    print(((v-a)//(a-b))+2)
else:
    print(((v-a)//(a-b))+1)
