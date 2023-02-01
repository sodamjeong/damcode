# import random

# import random

# import random

# print(random.sample(range(1,46), 6))

# import datetime

# print(datetime.datetime.now())

# grades = {'john' : 80, 'eric' : 90}
# print(grades.keys())
# print(grades.values())
# print(grades.items())

# for name, score in grades.items():
#     print(name,score)

# n = [1, 5, 6, 6, 12, 5, 123, 5, 4]

# import random

# print(random.randint(4,15))
# print(random.choice(n))
# random.shuffle(n)
# print(n)
# print(random.sample(n, 2))

# import datetime

# print(datetime.date(2023, 1, 5))
# print(datetime.date.today())
# print(datetime.datetime.today())
# print(datetime.datetime.now())



# print('\\     /\\')
# print(' )   ( \')')
# print('(   /  )')
# print(' \\ (__)|')

# print("\\    /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(" \\(__)|")


# print("|\\_/|")
# print("|q p|   /}")
# print("( 0 )\"\"\"\\")
# print("|\"^\"`    |")
# print("||_/=\\\\__|")

# print("         ,r'\"7")
# print("r`-_   ,'  ,/")
# print(" \. \". L_r'") 
# print("   `~\/")
# print("      |")
# print("      |")

# print("         ,r'\"7")
# print("r`-_   ,'  ,/")
# print(" \. \". L_r'")
# print("   `~\/")
# print("      |")
# print("      |")

# a = int(input())
# b = input()

# print(a * int(b[2]))
# print(a * int(b[1]))
# print(a * int(b[0]))
# print(a * int(b))

# a = int(input())
# b = int(input())

# print(a*(b%10))
# print(a*((b%100)//10))
# print(a*(b//100))
# print(a*b)

H,M = map(int,input().split())

# 1
if H in range(24):
    M -= 45
    if M < 0:
        M += 60
        H -= 1
        if H < 0:
            H += 24
print(H,M)

# 2 
A = H* 60 + M - 45

if (A < 60) :
    print(23, 60 + A)
else:
    print(A // 60, A % 60)

# 3

if M >= 45:
    print(H, M - 45)
elif H > 0 and M < 45:
    print(H - 1, M + 15)
else:
    print(23, M + 15)