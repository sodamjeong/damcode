# 1654 랜선자르기

# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# lst = [int(input()) for _ in range(n)]
# cnt = sum(lst) // m

# while 1:
#     line = 0
#     for x in lst:
#         line += (x // cnt)
#     if line == m:
#         print(cnt)
#         break
#     else:
#         cnt -= 1
# 시간 초과


# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# lst = [int(input()) for _ in range(n)]
# x,y = 1,max(lst)

# while x <= y:
#     mid = (x+y) // 2
#     line = 0
#     for i in lst:
#         line += (i//mid)
#     if line < m:
#         y = mid - 1
#     else:
#         x = mid + 1
# print(y)

# 1874 스택수열
import sys
input = sys.stdin.readline

num = int(input())
n = [i for i in range(num,0,-1)] # 1~num 까지의 숫자 역순 나열
m = [int(input()) for _ in range(num)] # 입력되는 num개의 숫자 리스트 생성
stack = [] # n에서 꺼내 담았다가 m과 같은 수열대로 숫자를 내보내기 위한 빈 리스트 
cnt = [] # 출력 할 기호 쌓아줄 빈 리스트
a = 0 # m의 인덱스 1씩 더해줄 예정

while 1:
    for i in n: # 리스트 n 순회
        stack.append(n.pop()) # n의 마지막 숫자를 꺼내 stack에 담아준다.
        cnt.append('+') # 담을 때는 '+'를 출력해야 함으로 '+' 쌓기
        if stack[-1] == m[a]: # 만약 담아둔 숫자의 마지막 숫자와 m의 a 인덱스와 같다면
            while 1:
                stack.pop() # 담아둔 숫자의 마지막 숫자 꺼내기
                cnt.append('-') # 꺼낼때는 '-'를 출력해야 함으로 '-' 쌓기
                a += 1 # m의 그 다음 인덱스에 있는 수와 비교하기 위해 +1
                if len(stack) == 0: # 만약 담아둔 숫자가 없거나
                    break
                elif stack[-1] != m[a]: # 담아둔 숫자들의 마지막 숫자가 비교 숫자와 다르다면
                    break # break
    if len(n) == 0: # 위의 계산식을 n 리스트에 요소가 남아있지 않을 때 까지 반복
        break
if len(stack) != 0: # n 리스트에 담겨있던 숫자를 모두 꺼냈는데 stack에 담아둔 숫자가 모두 꺼내지지 못했다면
    print('NO') # stack 으로 만들 수 없는 수열 'NO' 출력
else: # stack에 담아뒀던 숫자들이 모두 꺼내졌다면
    print(*cnt,sep='\n') # 쌓아둔 기호를 한개 한개 출력