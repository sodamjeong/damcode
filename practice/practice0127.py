# 2108 통계학
from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
m = [int(input()) for _ in range(n)]
m.sort()
dic = Counter(m).most_common(2)
# 제일 많이 나온 값 두개 까지만 정렬
print(round(sum(m)/n))
print(m[n//2])
if len(m) > 1:
    if dic[0][1]==dic[1][1]:
        print(dic[1][0])
    else:
        print(dic[0][0])
else:
    print(dic[0][0])
print(m[-1]-m[0])