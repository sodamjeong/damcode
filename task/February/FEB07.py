# 17608 막대기
import sys
input = sys.stdin.readline

sticks = [int(input()) for _ in range(int(input()))]
stick = 0
cnt = 0
for i in sticks[::-1]:
    if i > stick:
        cnt += 1
        stick = i
print(cnt)

# 17608 덩치
import sys
input = sys.stdin.readline
physical = [list(map(int,input().split())) for _ in range(int(input()))]

for i in physical:
    rank = 1 
    for j in physical:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank,end=' ')

# 1063 킹

import sys
input = sys.stdin.readline
site = {
    "R": (0, 1),
    "L": (0, -1),
    "B": (1, 0),
    "T": (-1, 0),
    "RT": (-1, 1),
    "LT": (-1, -1),
    "RB": (1, 1),
    "LB": (1, -1)
}
 # 이동명령 알파벳 : (이동 좌표) 딕셔너리 생성

king, stone, n = input().split() # 킹의 위치, 돌의 위치, 이동횟수
kx, ky = 8-int(king[1]), ord(king[0])-ord("A") # 킹의 세로좌표, 가로좌표
sx, sy = 8-int(stone[1]), ord(stone[0])-ord("A") # 돌의 세로좌표, 가로좌표
for _ in range(int(n)):
    move = input().strip() # 이동 명령 알파벳 입력
    dx, dy = site[move] # 입력값의 세로좌표, 가로좌표
    if not (0 <= kx+dx < 8 and 0 <= ky+dy < 8):
        continue # 킹의 좌표에 세로좌표와 가로좌표 더해서 범위를 벗어나면 다음으로 넘어가기
    kx += dx # 범위 안에 있으면 킹의 좌표에 세로, 가로 좌표 더해줌 
    ky += dy
    if (kx, ky) == (sx, sy): # 킹을 이동시켰는데 돌의 위치와 같다면
        if not (0 <= sx+dx < 8 and 0 <= sy+dy < 8): # 돌의 위치에 세로좌표,가로좌표 더했을때 범위를 벗어나면
            kx -= dx # 킹의 위치를 원래 자리로 되돌리고
            ky -= dy
            continue # 다음 명령으로 넘어가기
        sx += dx # 돌의 위치가 범위를 벗어나지 않으면 돌을 이동시켜주기
        sy += dy
# 이동횟수가 끝나면      
print(chr(ord("A")+ky)+str(8-kx)) # 다시 가로좌표를 알파벳으로 바꿔주고
print(chr(ord("A")+sy)+str(8-sx)) # 세로좌표도 다시 8 역순으로 바꿔줘서 킹의 위치 돌의 위치 출력