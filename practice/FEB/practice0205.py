# 7568 덩치
# import sys
# input=sys.stdin.readline
# n = int(input())
# m = [list(map(int,input().split())) for _ in range(n)]
# rank = m[:]
# rank.sort(key=lambda x:(x[0],x[1]),reverse=1)
# for i in range(1,n+1):
#     rank[i-1].insert(0,i)
# for i in range(n-1):
#     if rank[i][1] < rank[i+1][1] or rank[i][2] < rank[i+1][2]:
#         rank[i+1][0] = rank[i][0]
# for i in m:
#     print(i[0],end=' ')

# 틀림

# people = [list(map(int,input().split())) for _ in range(int(input()))]
# rank = []
# for x in people:
#     cnt = 1
#     for y in people:
#         if x[0]<y[0] and x[1]<y[1]:
#             cnt += 1
#     rank.append(cnt)
# print(*rank)

# 1018 체스판 다시 칠하기
n,m = map(int,input().split())
board = [list(input()) for i in range(n)]
color = []

for a in range(n-7):
    for b in range(m-7):
        cnt = 0
        for x in range(a,a+8):
            for y in range(b,b+8):
                if ((x+y) % 2 == 0 and board[x][y]=='W') or \
                ((x+y) % 2 == 1 and board[x][y]=='B'):
                    cnt += 1
        color.append(min(cnt,64-cnt))
print(min(color))
        