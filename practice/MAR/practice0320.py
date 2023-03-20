# swea 1986 지그재그 숫자

# for t in range(1,int(input())+1):
#     num = 0
#     for i in range(1,int(input())+1):
#         if i % 2 == 1:
#             num += i
#         else:
#             num -= i
#     print(f'#{t} {num}')

# 15656 N과 M(7)

# n,m = map(int,input().split())
# num = list(map(int,input().split()))
# num.sort()
# lst = []

# def arr():
#     if len(lst) == m:
#         print(*lst)
#         return
    
#     for i in num:
#             lst.append(i)
#             arr()
#             lst.pop()
# arr()

# swea 1945 간단한 소인수분해

# num = [2, 3, 5, 7, 11]

# def divide(n):

#     if n == 1:
#         print(f'#{t}', *cnt)
#         return
    
#     for i in range(5):
#         if n % num[i] == 0:
#             cnt[i] += 1
#             n //= num[i]
#     divide(n)

# for t in range(1,int(input())+1):
#     cnt = [0, 0, 0, 0, 0]
#     n = int(input())
#     divide(n)

# 15652 N과 M(4)

n,m = map(int,input().split())
num = []

def arr(i):
    if len(num) == m:
        print(*num)
        return
    
    for j in range(i,n+1):
            num.append(j)
            arr(j)
            num.pop()
arr(1)