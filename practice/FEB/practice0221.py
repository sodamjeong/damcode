# 15649 N과M (1)

# n,m = map(int,input().split())
# lst = []
# cnt = 1

# for i in range(n,0,-1):
#     cnt *= i
#     m -= 1
#     if m == 0:
#         break

n,m = map(int,input().split())
lst = []

def dfs():
    if len(lst) == m:
        print(*lst)
        return
    for i in range(1,n+1):
        if i not in lst:
            lst.append(i)
            dfs()
            lst.pop()
dfs()