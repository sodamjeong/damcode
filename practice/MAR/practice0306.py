# 10870 피보나치수 5

# n = [0,1]
# m = int(input())
# for i in range(m):
#     n.append(n[-1]+n[-2])
# print(n[m])

# 10810 공넣기

# n,m = map(int,input().split())
# basket = [0 for _ in range(n+1)]
# for i in range(m):
#     x,y,z = map(int,input().split())
#     for j in range(x,y+1):
#         basket[j] = z
# print(*basket[1:])

# 10813 공 바꾸기

# n,m = map(int,input().split())
# basket = [i for i in range(n+1)]

# for j in range(m):
#     x,y = map(int,input().split())
#     basket[x],basket[y] = basket[y], basket[x]
# print(*basket[1:])

# 17478 재귀함수가 뭔가요?

cnt = 0

def question(n):
    under = "____"
    global cnt

    if cnt == n:
        print((under*cnt)+'"재귀함수가 뭔가요?"')
        print((under*cnt)+'"재귀함수는 자기 자신을 호출하는 함수라네"')
        while 1:
            print((under*cnt)+"라고 답변하였지.")
            cnt -= 1
            if cnt < 0:
                break
    else:
        print((under*cnt)+'"재귀함수가 뭔가요?"')
        print((under*cnt)+'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print((under*cnt)+'마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print((under*cnt)+'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        cnt += 1
        question(n)
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
question(int(input()))