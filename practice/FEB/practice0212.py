# 1620 나는야 포켓몬 마스터 이다솜
# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# mon = [input().rstrip('\n') for _ in range(n)]
# mon.insert(0,'')
# monster = {i : mon.index(i) for i in mon}

# for _ in range(m):
#     n = input().rstrip('\n')
#     if n in monster:
#         print(monster.get(n))
#     else:
#         print(mon[int(n)])

# 시간초과

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
mon = {}
mon2 = {}

for i in range(1,n+1):
    p = input().rstrip('\n')
    mon[str(i)] = p
    mon2[p] = i
for i in range(m):
    s = input().rstrip('\n')
    print(mon.get(s,mon2.get(s)))
