# 1085 직사각형에서 탈출
# x,y,w,h = map(int,input().split())
# print(min(x,y,w - x,h - y)) 

# 1259 팰린드롬수

# while 1:
#     n = input()
#     if n == '0':
#         break
#     if n == n[::-1]:
#         print('yes')
#     else:
#         print('no')

# swea 2063 중간값찾기
# t = int(input())
# n = list(map(int,input().split()))
# print(sorted(n)[(t//2)])

# swea 2058. 자릿수 더하기
# print(sum([int(i) for i in input()]))

# swea 2070. 큰 놈, 작은 놈, 같은 놈

for i in range(1,int(input())+1):
    a,b = map(int,input().split())
    if a > b:
        print(f'#{i} >')
    elif a == b:
        print(f'#{i} =')
    else:
        print(f'#{i} <')