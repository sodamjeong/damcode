# 2386 도비의 영어 공부
# from collections import Counter
# while 1 :
#     word = list(input().lower())
#     word_cnt=Counter(word[1:])
#     if '#' in word:
#         break
#     print(word[0],word_cnt[word[0]])

# 왜 틀렸는지 모르겠음

# 11050 이항 계수1

import sys
input = sys.stdin.readline
n, k = map(int,input().split())
up = down = 1
for i in range(k):
    up *= n - i
    down *= (i+1)
print(up//down)

# 다른 방법 (라이브러리)

import math
print(math.comb(*map(int,input().split())))
# math 공부 필요