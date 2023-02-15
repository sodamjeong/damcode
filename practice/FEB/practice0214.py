# 5086 배수와 약수

while 1:
    a, b = map(int,input().split())
    if (a,b)==(0,0):
        break
    if b % a == 0:
        print('factor')
    elif a%b == 0:
        print('multiple')
    else:
        print('neither')
# 11866 요세푸스 문제 0
import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
people = deque([i for i in range(1,n+1)])
person = []

while people:
    people.rotate(-(k-1))
    person.append(people.popleft())
print(f'<{", ".join(map(str,person))}>')