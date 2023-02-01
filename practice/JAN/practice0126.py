# 10773 제로
import sys
# input = sys.stdin.readline

# n = []
# for i in range(int(input())):
#     m = int(input())
#     if m > 0 :
#         n.append(m)
#     else:
#         n.pop()
# print(sum(n))

# 2161 카드1

# import sys
# input = sys.stdin.readline

# n = [i for i in range(1,int(input())+1)]
# m = []
# while len(n) > 1:
#     m.append(n.pop(0))
#     n.append(n.pop(0))
# print(*m,*n)

# # 라이브러리 사용
# from collections import deque

# n = int(input())
# queue = deque(range(1,n + 1))

# while len(queue) > 1:
#     print(queue.popleft(),end=" ")
#     queue.append(queue.popleft())
# print(queue[0])

# 2108번 통계학

# from collections import Counter
# import sys
# input = sys.stdin.readline

# num = [int(input()) for _ in range(int(input()))]
# cnt = [v for v in Counter(num).values()]
# key = [k for k in Counter(num).keys() if Counter(num)[k] == max(cnt)]

# print(round(sum(num)/len(num)))
# print(sorted(num)[int(len(num)/2)])
# if len(key) > 1:
#     print(sorted(key)[1])
# else:
#     print(*key)
# print(max(num)-min(num))

# 시간초과

# from collections import Counter
# import sys
# input = sys.stdin.readline

# num = [int(input()) for _ in range(int(input()))]

# print(round(sum(num)/len(num)))
# print(sorted(num)[int(len(num)/2)])
# k = sorted(key:= [k for k in Counter(num) if Counter(num)[k] == max(Counter(num).values())])
# if len(k) == 1:
#     print(*k)
# else:
#     print(k[1])
# print(max(num)-min(num))

# 시간초과
from collections import Counter
import sys
input = sys.stdin.readline

def Calculator(n):
    print(round(sum(n)/len(n)))
    print(sorted(n)[int(len(n)/2)])
def Calculator2(n):
    print(max(n)-min(n))

lst = [int(input()) for _ in range(int(input()))]
Calculator(lst)
key = [k for k in Counter(lst) if Counter(lst)[k] == max(Counter(lst).values())]
if len(key) == 1:
    print(*key)
else:
    print(sorted(key)[1])
Calculator2(lst)

# print(sorted(dict(filter(lambda elem:elem[1]>=max(Counter(lst).values()), Counter(lst).items())))[1]) 