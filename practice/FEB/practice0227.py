# 1966 프린터 큐

for _ in range(int(input())): # 테스트 케이스
    n,m = map(int,input().split()) # 출력대기수, 타겟문서
    num = list(map(int,input().split())) # 출력 대기 문서들의 중요도 리스트
    lst = [(i, idx) for idx, i in enumerate(num)] # (중요도, 각 문서들의 위치) 리스트
    cnt = 0 # 몇 번째 출력인지 카운팅

    while 1:
        if max(lst)[0] == lst[0][0]: # 리스트에서 중요도가 가장 높은 문서가 첫번째 순서일 때
            cnt += 1 # 출력 차례 + 1
            if lst[0][1] == m: # 내가 찾고자 하는 타겟문서이면
                print(cnt) # 몇 번째 출력인지 출력
                break
            else:
                lst.pop(0) # 찾는 문서가 아니면 삭제
        else: # 중요도가 가장 높은 문서가 첫번째가 아니면 맨 뒤로 보냄
            lst.append(lst.pop(0))
