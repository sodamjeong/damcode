# 문제 1
a = 1
b = 2
print(a < b) # True

# 문제 2
a = bool("")
b = False
print(a == b) # True

# 문제 3
a = 1
result = ""

if a == 1:
    result = True
else:
    result = False
print(result) # True

# 문제 4 
a = 90

if a == 90:
    a = a + 10

elif a == 100:
    a = a + 10

elif a == 110:
    a = a + 10

else:
    a = a + 10

a = a + 10

print(a) # 110

# 문제 5
string = 'hello world!'

for element in string:
    print(element)

'''
h
e
l
l
o

w
o
r
l
d
!
'''

# 문제 6
list_variable = [0, 1, 2, 3, 4, 5, 6]

for element in list_variable:
    print(element, end=" ")

'''0 1 2 3 4 5 6'''

# 문제 7
n = 10 

for element in range(-n, n):
    print(element, end=" ")

'''-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9'''

# 문제 8
n = 10

for element in range(1, n+1, 3):
    print(element, end=" ")

'''1 4 7 10'''

# 문제 9
list_variable = [6, 5, 4, 3, 2, 1, 0]

for index, element in enumerate(list_variable):
    print(index, element)

'''
0 6
1 5
2 4
3 3
4 2
5 1
6 0
'''

# 문제 10 

n = 10

for element in range(n, -n , -1):
    print(element ,end = " ")
    if n < 0:
        break

'''10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 '''

# 문제 11
list_variable = [-1, 3, 5, -2, 1, 9, 21, -3, -5]

for element in list_variable:
    if element < 0:
        continue
    
    print(element, end=" ")

'''3 5 1 9 21'''

# 문제 12
N = 3
M = 4

for n in range(N):
    for m in range(M):
        print(f'{n}, {m}')

'''
0, 0
0, 1
0, 2
0, 3
1, 0
1, 1
1, 2
1, 3
2, 0
2, 1
2, 2
2, 3
'''
