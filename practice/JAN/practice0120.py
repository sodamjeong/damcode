# 1712번 손익분기점

# a,b,c = map(int,input().split())

# if b >= c:
#     print('-1')
# else:
#     print((a//(c-b))+1)

# 2292번 벌집

a,b,n =0,1,int(input())
while 1:
    b += (6*a)
    if n <= b:
        print(a + 1)
        break
    else:
        a += 1