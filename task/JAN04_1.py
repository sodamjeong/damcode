# 문제 1 
# 정수 한 개를 입력 받고, 해당 정수의 절대값을 출력하세요.
# 단, abs() 함수는 사용하지 마세요.

n = int(input())

if n < 0:
    print(-n)
else:
    print(n)

# 문제 2
# 정수만 저장한 리스트가 주어집니다. 리스트 요소의 개수를 출력하세요.
# 단, len() 함수는 사용하지 마세요

number_list = list(map(int, input().split()))
m = 0

for n in number_list:
    m += 1
    
print(m)

# 문제 3

# 정수만 저장한 리스트가 주어집니다. 리스트에 저장된 정수들의 합을 출력하세요.
#단, sum() 함수는 사용하지 마세요.

number_list = list(map(int, input().split()))
m = 0

for n in number_list:
    m += n

print(m)

# 문제 4

# 정수만 저장한 리스트가 주어집니다. 리스트에 저장된 정수들의 평균을 출력하세요.
# 단, len() / sum() 함수는 사용하지 마세요.

number_list = list(map(int, input().split()))
m = 0
i = 0

for n in number_list:
    m += n
    i += 1

print(m/i)

# 문제 5

# 정수만 저장한 리스트가 주어집니다. 리스트에 저장된 정수들의 곱을 출력하세요.

number_list = list(map(int, input().split()))
m = 1

for n in number_list:
    m *= n

print(m)

# 문제 6

# 양의 정수만 저장한 리스트가 주어집니다.리스트에 저장된 정수 중 가장 큰 값을 출력하세요.
#단, max() 함수는 사용하지 마세요.

number_list = [10, 1, 5, 6, 8]
m = number_list[0]

for n in number_list:
    if n > m:
        m = n
print(m)

# 문제 7

# 양의 정수만 저장한 리스트가 주어집니다.리스트에 저장된 정수 중 가장 작은 값을 출력하세요.
#단, min() 함수는 사용하지 마세요.

number_list = [1, 5, 8, 6]
m = number_list[0]

for n in number_list:
    if n < m:
        m = n
print(m)