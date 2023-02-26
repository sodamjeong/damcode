# 18115 카드놓기
# from collections import deque

# n = int(input())
# num = list(map(int,input().split()))
# card = deque()
# for i in range(1,n+1):
#     j = num[-i]
#     if j == 1:
#         card.appendleft(i)
#     elif j == 3:
#         card.append(i)
#     else:
#         card.appendleft(i)
#         if len(card)>1:
#             card[0],card[1]=card[1],card[0]
# print(*card)

# 프로그래머스 42587

def solution(priorities, location):
    answer = 0
        
    order = []
    cnt = 0
    l = len(priorities)
    
    while 1:
        while priorities[cnt] != max(priorities):
            cnt = (cnt + 1) % l
            
        priorities[cnt] = 0
        order.append(cnt)
        
        if len(order) == l:
            break
    
    answer = order.index(location) + 1
        
    return answer