# 18870 좌표 압축
# n = int(input())
# lst = list(map(int,input().split()))
# lst_set = set(lst)
# for x in lst:
#     cnt = 0
#     for y in lst_set:
#         if x > y:
#             cnt += 1
#     print(cnt,end=' ')
# # 시간 초과

# n = int(input())
# lst = list(map(int,input().split()))
# for i in lst:
#     print(sorted(set(lst)).index(i),end=' ')
# # 시간 초과

# import sys
# input=sys.stdin.readline
# input()
# lst = list(map(int,input().split()))
# lst2 = sorted(set(lst))
# dic = {}
# for i in lst2:
#     dic[i]=lst2.index(i)
# for i in lst:
#     print(dic.get(i),end= ' ')
# # 시간초과 

import sys
input=sys.stdin.readline
input()
lst = list(map(int,input().split()))
lst2 = sorted(set(lst))
dic = {lst2[i] : i for i in range(len(lst2))}
for i in lst:
    print(dic[i],end= ' ')