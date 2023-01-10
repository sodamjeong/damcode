# 문제 1
# 2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.


t = int(input())

for i in range(1,t+1):
    a,b = map(int,input().split())
    print(f'#{i}', a // b, a % b)

# 2071. 평균값 구하기

# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)

t = int(input())

for i in range(1,t+1):
    n = list(map(int,input().split()))
    print(f'#{i}', round(sum(n) / len(n)))

# 1938. 아주 간단한 계산기

# 두 개의 자연수를 입력받아 사칙연산을 수행하는 프로그램을 작성하라.

a, b = map(int,input().split())
n = (a + b, a - b, a * b, int(a / b))

for i in n:
    print(i)

# 2046. 스탬프 찍기

# 주어진 숫자만큼 # 을 출력해보세요. 주어질 숫자는 100,000 이하다.

n = int(input())

for i in range(n):
    print('#', end = '')

# 2068. 최대수 구하기

# 10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라

t = int(input())

for i in range(1,t+1):
    n = list(map(int,input().split()))
    print(f'#{i}',max(n))