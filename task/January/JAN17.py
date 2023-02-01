# 최소,최대

n = int(input())
a=list(map(int,input().split()))
print(min(a), max(a))

# 숫자의 합

n = input()
# 1 
print(sum([int(i) for i in (input())]))
# 2
print(sum(map(int,input())))

# 수 정렬하기
n = [int(input()) for i in range(int(input()))]
print(*sorted(n),sep='\n')

# 최댓값
print(m := max(a := [int(input()) for i in range(9)]))
print(a.index(m)+1)