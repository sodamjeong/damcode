#  구현

# 1.

# 문자열을 입력받고, e 가 처음 나오는 위치(index)를 출력하세요.
# 만약, 문자열에서 e 가 없으면 -1 을 출력하세요. 단, index() / find() 메서드는 사용하지마세요.

n = input()
m = 0

for i in n:
    m += 1
    if i == 'e':
        print(m - 1)
    if 'e' not in n:
        print(-1)
        break

# 2.

# 문자열을 입력받고, 각 단어의 등장 횟수를 출력하세
# 단, count() 메서드는 사용하지마세요.

n = list(input().split())
m = {}

for i in n:
    if i not in m:
        m[i] = 1
    else:
        m[i] += 1
# 2-1.
for a in m:
    print(a,m[a])

# 2-2.

for k,v in m.items():
    print(k,v)


# 3.

# 문자열을 입력받고, e 를 제거한 결과를 출력하세요.
#단, replace() 메서드는 사용하지 마세요.

n = list(input())
m = []

for i in n:
    if i != 'e':
        m.append(i)

for a in m:
    print(a,end = "")

# 4.
# 문자열과 알파벳을 공백으로 구분해서 입력받고,문자열에서 입력한 알파벳의 개수를 출력하세요.
# 단, count() 메서드는 사용하지마세요.

n,m = input().split()
a = 0

for i in n:
    if i == m:
        a += 1
    
print (a)

# 5. 
# 양의 정수 3개를 입력받고, 3개의 양수를 - 로 연결해서 출력하세요.
# 단, join() 메서드는 사용하지마세요.

a,b,c = list(input().split())


print(a, b, c, sep='-')

# 6.
# 양의 정수를 입력받고, 자리수의 합을 출력하세요.
# 만약, 입력 받은 값이 0보다 작으면 -1을 출력하세요.
# 단, 양의 정수를 문자열로 변경하지마세요. str() 함수를 사용하지마세요.

n = int(input())
m = 0

if n < 0:
    print(-1)
else:
    while n > 0:
        m += n % 10
        n = n//10
    print(m)