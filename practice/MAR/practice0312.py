# 11729 하노이 탑 이동순서

# def hanoi(n,start,end,assi):
#     if n == 1:
#         print(start,end)
#         return
#     hanoi(n-1,start,assi,end)
#     print(start,end)
#     hanoi(n-1,assi,end,start)
# n = int(input())
# print(2**n-1)
# hanoi(n,1,3,2)  

# n = int(input())
# m = 1
# while n > 0:
#     m *= n
#     n -= 1
# print(m)


# 2444 별찍기 -7

n = int(input())
m = 0
for i in range(1,n+1):
    print((' '*(n-i))+(i+m)*'*')
    m += 1
m-=1
for j in range(n-1,0,-1):
    m -= 1
    print((' '*(n-j))+(j+m)*'*')
