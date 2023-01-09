# my_list= ['서울', '서울', '대전', '광주', '서울', '대전', '부산', '부산']
# n = {}

# for i in my_list:
#     if i not in n:
#         n[i] = 1
#     else:
#         n[i] += 1


# print(len(n))


n = list(map(int,input().split()))

print(*n) # 숫자만 나옴

for m in n:
    print(m, end=" ")