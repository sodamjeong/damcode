# 10845 큐

# from collections import deque
# import sys
# input = sys.stdin.readline

# queue = deque()
# for _ in range(int(input())):
#     x = input().rstrip('\n')
#     n = x[:5]
#     if n == 'push ':
#         queue.append(int(x[5:]))
#     elif x == 'pop':
#         if len(queue) > 0:
#             print(queue.popleft())
#         else:
#             print(-1)
#     elif x == 'size':
#         print(len(queue))
#     elif x == 'empty':
#         if len(queue) > 0:
#             print(0)
#         else:
#             print(1)
#     elif x == 'front':
#         if len(queue) > 0:
#             print(queue[0])
#         else:
#             print(-1)
#     elif x == 'back':
#         if len(queue) > 0:
#             print(queue[-1])
#         else:
#             print(-1)

# 10866 덱

from collections import deque
import sys
input = sys.stdin.readline

d = deque()

for _ in range(int(input())):
    n = input().split()
    if n[0] == "push_front":
        d.appendleft(n[1])
    elif n[0] == "push_back":
        d.append(n[1])
    elif n[0] == "pop_front":
        if d:
            print(d[0])    
            d.popleft()
        else:
            print("-1")
    elif n[0] == "pop_back":
        if d:
            print(d[len(d) - 1])    
            d.pop()
        else:
            print("-1")
    elif n[0] == "size":
        print(len(d))
    elif n[0] == "empty":
        if d:
            print("0")
        else:
            print("1")
    elif n[0] == "front":
        if d:
            print(d[0])
        else:
            print("-1")
    elif n[0] == "back":
        if d:
            print(d[len(d) - 1])
        else:
            print("-1")