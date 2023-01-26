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

import sys
input = sys.stdin.readline

n = [i for i in range(1,int(input())+1)]
m = []
while len(n) > 1:
    m.append(n.pop(0))
    n.append(n.pop(0))
print(*m,*n)

# 라이브러리 사용
from collections import deque

n = int(input())
queue = deque(range(1,n + 1))

while len(queue) > 1:
    print(queue.popleft(),end=" ")
    queue.append(queue.popleft())
print(queue[0])