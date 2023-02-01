# 10870 피보나치수 5
# n = [0,1]
# for i in range(int(input())):
#         n.append(n[i]+n[i+1])
# print(n[-2])

# 25501 재귀의 귀재

def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)
for _ in range(int(input())):
    cnt = 0
    word = input()
    print(isPalindrome(word),cnt)