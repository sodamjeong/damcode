# 10828 스택

# import sys
# input = sys.stdin.readline

# stack = []
# for _ in range(int(input())):
#     x = input().rstrip('\n')
#     n = x[:5]
#     if n == 'push ':
#         stack.append(int(x[5:]))
#     elif x == 'pop':
#         if len(stack) > 0:
#             print(stack.pop())
#         else:
#             print(-1)
#     elif x == 'size':
#         print(len(stack))
#     elif x == 'empty':
#         if len(stack) > 0:
#             print(0)
#         else:
#             print(1)
#     elif x == 'top':
#         if len(stack) > 0:
#             print(stack[-1])
#         else:
#             print(-1)

# swea 12368 24시간
# for t in range(1,int(input())+1):
#     a,b = map(int,input().split())
#     if a+b < 24:
#         print(f'#{t} {a+b}') 
#     else:
#         print(f'#{t} {(a+b)-24}')

# swea 13218 조별과제

# for t in range(1,int(input())+1):
#     print(f'#{t} {int(input())//3}')

# swea 3431 준환이의 운동관리

# for t in range(1,int(input())+1):
#     x,y,z = map(int,input().split())
#     if x > z:
#         print(f'#{t} {x-z}')
#     elif z > y:
#         print(f'#{t} -1')
#     else:
#         print(f'#{t} 0')

