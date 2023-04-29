# 2167
# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# num = [list(map(int,input().split())) for _ in range(n)]

# for _ in range(int(input())):
#     x,y,i,j = map(int,input().split())
#     cnt = 0
#     for a in range(x-1,i):
#         for b in range(y-1,j):
#             cnt += num[a][b]
#     print(cnt)


# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# num = [list(map(int,input().split())) for _ in range(n)]
# cnt = [[0 for _ in range(m+1)] for _ in range(n+1)]

# for x in range(1,n+1):
#     for y in range(1,m+1):
#         cnt[x][y] = num[x-1][y-1] + cnt[x-1][y] + cnt[x][y-1] - cnt[x-1][y-1]

# for _ in range(int(input())):
#     x,y,i,j = map(int,input().split())
#     print(cnt[i][j]-cnt[i][y-1]-cnt[x-1][j]+cnt[x-1][y-1])

# 1302 
# from collections import Counter
# book = [input() for _ in range(int(input()))]
# books = Counter(book)
# cnt = max(books.values())
# best = []

# for k,v in books.items():
#     if v == cnt:
#         best.append(k)
# print(sorted(best)[0])


# 1406
# import sys
# input = sys.stdin.readline

# word = list(input().strip())
# word2 = []

# for _ in range(int(input())):
#     order = input().strip()
#     if order == 'L':
#         if len(word) == 0:
#             continue
#         word2.append(word.pop())
#     elif order == 'D':
#         if len(word2) == 0:
#             continue
#         word.append(word2.pop())
#     elif order == 'B':
#         if len(word) == 0:
#             continue
#         word.pop()
#     elif order[0] == 'P':
#             word.append(order[2])
# word.extend(word2[::-1])
# print(''.join(word))

# 14425
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = [input().strip() for _ in range(n)]
lst2 = [input().strip() for _ in range(m)]
cnt = 0

for i in lst2:
    if i in lst:
        cnt += 1
print(cnt)