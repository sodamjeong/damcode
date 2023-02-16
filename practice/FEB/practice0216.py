# 2386 도비의 영어 공부

# while 1:
#     n = input().lower()
#     if n == '#':
#         break
#     print (n[0], n[1:].count(n[0]))

# 10816번 숫자카드 2

from collections import Counter
import sys
input = sys.stdin.readline

input()
n = list(map(int,input().split()))
input()
card = Counter(n)
for i in list(map(int,input().split())):
    print(card.get(i,0),end=' ')
