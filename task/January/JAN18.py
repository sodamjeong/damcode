# 10988 팰린드롬인지 확인하기

n = input()

if n[::1] == n[::-1]:
    print(1)
else:
    print(0)

# 2789 유학금지

n = input()
m = []

for x in n:
        if x not in 'CAMBRIDGE':
            m.append(x)
print(''.join(m))

# 2675 문자열 반복

n = []
for i in range(int(input())):
    a,b = input(). split()
    for x in b:
        n.append(x*int(a))
    print(''.join(n))
    n = []

# 17249 태보태보 총난타

n = input().split('(^0^)')
print(n[0].count('@'),n[1].count('@'))

# 2941 크로아티아 알파벳

n = input()
m = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in m:
    n = n.replace(i,'1')
print(len(n))

# 10809 알파벳 찾기

n = input()

for i in map(chr,range(97,123)):
    print(n.find(i),end=' ')