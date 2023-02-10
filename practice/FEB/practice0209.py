# 1085 직사각형에서 탈출
# x,y,w,h = map(int,input().split())
# print(min(x,y,w - x,h - y))

# 1264 모음의 개수

n = ['a','e','i','o','u']

while 1:
    cnt = 0
    for i in (m:=input().lower()):
        if i in n:
            cnt += 1
    if m == '#':
        break
    print(cnt)
