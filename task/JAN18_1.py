# 9498 시험성적
# grade = int(input())

# if grade < 60:
#     print('F')
# elif grade < 70:
#     print('D')
# elif grade < 80:
#     print('C')
# elif grade < 90:
#     print('B')
# else:
#     print('A')

print('FFFFFFDCBAA'[int(input())//10])

# 9093 단어 뒤집기

import sys
input = sys.stdin.readline

for i in range(int(input())):
    print(*[s[::-1] for s in input().split()])


# 11721 열 개 씩 끊어 출력하기

n = [i for i in input()]

while len(n) > 0:
    print(''.join(n[0:10]))
    del(n[0:10])

# 2안 
S = input()

for i in range(0, len(S), 10):
    print(S[i:i+10])

# 2947 나무 조각

n = [1, 2, 3, 4, 5]
m = list(map(int,input().split()))

while n != m:
    a = 1
    for i in m:
        try:
            if i > m[a]:
                m.remove(i)
                m.insert(a,i)
                a += 1
                print(*m)
            elif i < m[a]:
                a += 1
        except:
            pass

#2안

import sys
input = sys.stdin.readline
m = list(map(int, input().split()))

while m != [1, 2, 3, 4, 5]:
    for i in range(4):
        if m[i] > m[i+1]:
            m[i], m[i+1] = m[i+1], m[i] 
            print(*m)