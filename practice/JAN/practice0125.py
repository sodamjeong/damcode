# 9020 골드바흐의 추측


# for i in range(int(input())):
#     n = int(input())
#     prime = []
#     for x in range(2,n):
#         num = []
#         for y in range(2,x+1):
#             if x % y == 0:
#                 num.append(y)
#         if len(num) == 1:
#             prime.append(x)
#     p = {}
#     for a in prime:
#         if n - a in prime and a <= n - a:
#             p[a] = n - a
#     print(max(p),p.get(max(p)))

    # 시간초과

# import sys
# input = sys.stdin.readline

# for i in range(int(input())):
#     n = int(input())
#     m = list(range((n+1)))
#     prime = {}
#     for x in m[2:]:
#         if n - m[x] in m and m[x] <= n - m[x]:
#             prime[m[x]]= n - m[x]
#         m[x::x] = n//x * [0]

#     print(max(prime),prime.get(max(prime)))

# 시간초과


# import sys
# input = sys.stdin.readline

# for i in range(int(input())):
#     n = int(input())
#     m = list(range((n+1)))
#     prime = {}
#     for x in m[2:]:
#         if m[x] <= n - m[x] and m[n - m[x]]:
#             prime[m[x]]= n - m[x]
#         m[x::x] = n//x * [0]

#     print(max(prime),prime.get(max(prime)))

# 시간초과

# import sys
# input = sys.stdin.readline

# def prime(n):
#     m = list(range(n+1))
#     plus = {}
#     for x in m[2:]:
#         if m[x] <= n - m[x] and m[n - m[x]]:
#             plus[m[x]] = n - m[x]
#         m[x::x] = n//x * [0]
    
#     return print(max(plus),plus.get(max(plus)))

# for i in range(int(input())):
#     n = int(input())
#     prime(n)

# 시간초과

# import sys 
# input = sys.stdin.readline

# def prime(n):
#     if n == 2:
#         return True
#     else:
#         for i in range(2,int(n**0.5)+1):
#             if n % i == 0:
#                 return False
#         return True

# for x in range(int(input())):
#     n = int(input())
#     a = b = int(n/2)
#     while True:
#         if prime(a) and prime(b):
#             print(a,b);break
#         elif a == 0: break
#         else:
#             a -= 1
#             b += 1

#  통과

# 2563 색종이

# paper = [[0]*100 for _ in range(101)] # 전체 100 * 100 도화지 생성 
# # 숫자 0 100개로 이루어진 리스트 100줄 

# for i in range(int(input())): # 색종이 장수 입력
#     x,y = map(int,input().split()) # 색종이 좌표 입력

#     for n in range(x,x+10): # 가로 10의길이
#         for m in range(y,y+10): # 세로 10의 길이
#             paper[n][m] = 1 # 색종이 면적 만큼 0 > 1 로 교체
# # 가로좌표 + 10, 세로좌표 + 10 위치에 모두 1을 찍는다 
# # 겹치는 면적은 이미 1이 찍혀있으므로 무시.

# size = 0 
# for cnt in paper: # 한줄 한줄 순회
#     size += cnt.count(1) # 1의 수 카운트 값을 더 해준다
# print(size)

# 2798 블랙잭

n,m = map(int,input().split())
card = list(map(int,input().split()))
ans = []

for x in range(0, n-2):
    for y in range(x+1, n-1):
        for z in range(y+1,n):
            if card[x]+card[y]+card[z] <= m:
                ans.append(card[x]+card[y]+card[z])
print(max(ans))
