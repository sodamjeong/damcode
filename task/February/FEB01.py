# 2525 오븐시계

# h,m=map(int,(input()).split())
# cook = h*60+m+int(input())
# h2 = cook//60
# m2 = cook% 60
# if h2 >= 24:
#     print((h2)-24,m2)
# else:
#     print(h2,m2)

# 2798 블랙잭

# n,m = map(int,input().split())
# card = list(map(int,input().split()))
# c = []
# for x in range(0, n-2):
#     for y in range(x+1, n-1):
#         for z in range(y+1,n):
#             t = card[x]+card[y]+card[z]
#             if t <= m:
#                 c.append(t)
# print(max(c))