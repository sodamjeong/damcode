# 25192
# import sys
# input = sys.stdin.readline

# n = {}
# cnt = 0

# for _ in range(int(input())):
#     m = input().strip()
#     if m == 'ENTER':
#         cnt += len(n)
#         n.clear()
#     else:
#         if m not in n:
#             n[m] = 1
#         else:
#             n[m] += 1
# cnt += len(n)
# print(cnt)


# 2851

n = [int(input()) for _ in range(10)]
cnt = 0
for i in range(10):
    cnt += n[i]
    if cnt >= 100:
        m =  cnt - n[i]
        if cnt - 100 > 100 - m:
            print(m)
        elif cnt - 100 <= 100 - m:
            print(cnt)
        break
if cnt < 100:
    print(cnt)
