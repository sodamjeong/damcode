# 2164 카드 2

from collections import deque

card = deque(range(1,int(input())+1))

while len(card) > 1:
    card.popleft()
    card.rotate(-1)
print(*card)