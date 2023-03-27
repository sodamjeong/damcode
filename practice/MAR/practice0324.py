# 11399 ATM 

# input()
# n = sorted(list(map(int,input().split())))
# m = []
# cnt = 0
# for i in n:
#     cnt += i
#     m.append(cnt)
# print(sum(m))

# 1463 1로 만들기

# n = int(input())
# cnt = [0] * (n+1)

# for i in range(2,n+1):
#     cnt[i] = cnt[i-1] + 1

#     if i % 2 == 0:
#         cnt[i] = min(cnt[i], cnt[i//2]+1)
#     if i % 3 == 0:
#         cnt[i] = min(cnt[i], cnt[i//3]+1)

# print(cnt[n])



# 9375 패션왕 신해빈

# for t in range(int(input())):
#     item = {}
#     cnt = 1
#     for i in range(int(input())):
#         n, m = input(). split()
#         if m not in item:
#             item[m] = 2
#         else:
#             item[m] += 1
#     for v in item.values():
#         cnt *= v
#     print(cnt-1)

# swea 4751 다솔이의 다이아몬드 장식

for t in range(int(input())):
    n = input()
    a = []
    b = []
    c = []
    for i in range(len(n)):
        if i == 0:
            a.append('..#..')
        else:
            a.append('.#..')
    for i in range(len(n)):
        if i == 0:
            b.append('.#.#.')
        else:
            b.append('#.#.')
    for i in range(len(n)):
        if i == 0:
            c.append(f'#.{n[i]}.#')
        else:
            c.append(f'.{n[i]}.#')
    print(''.join(a),''.join(b),''.join(c),''.join(b),''.join(a),sep='\n')
        