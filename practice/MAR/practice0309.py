# swea 1284 수도 요금 경쟁

# for t in range(1,int(input())+1):
#     p,q,r,s,w = map(int,input().split())
#     if w > r:
#         print(f'#{t}',min(w * p, q + (w - r) * s))
#     else:
#         print(f'#{t}',min(w * p, q))
# 1764 듣보잡

# a,b = map(int,input().split())
# name = {}
# m = []
# cnt = 0

# for i in range(a+b):
#     n = input()
#     if n not in name:
#         name[n] = 1
#     else:
#         name[n] += 1
# for k,v in name.items():
#     if v==2:
#         cnt += 1
#         m.append(k)
# print(cnt)
# print(*sorted(m),sep="\n")

# import sys
# input = sys.stdin.readline

# a,b = map(int,input().split())
# name = {}
# lst = []

# for i in range(a+b):
#     n = input().strip()
#     if n not in name:
#         name[n] = 1
#     else:
#         name[n] += 1
# for k,v in name.items():
#     if v==2:
#         lst.append(k)
# print(len(lst),*sorted(lst),sep='\n')

import sys
input = sys.stdin.readline

a,b = map(int,input().split())
p1 = [input().strip() for _ in range(a)]
p2 = [input().strip() for _ in range(b)]
lst = set(p1)&set(p2)
print(len(lst),*sorted(lst),sep='\n')