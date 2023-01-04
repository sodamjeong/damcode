# 문제 1
list_variable = [0, 1, 2, 3, 4, 5, 6]
list_variable.pop()
list_variable.append(7)
list_variable.append(8)

for element in list_variable[2:]:
    print(element, end=" ")

# 2 3 4 5 7 8 

# 문제 2

for element in range(-2, 10, 2):
    print(element, end=" ")

# -2 0 2 4 6 8

# 문제 3

a, b, c, d = 0, 0, 0, 0
n = 10

for number in range(n):
    if number % 2 == 0:
        a = a + 1
    
    if number % 3 == 0:
        b = b + 1

    if number % 4 == 0:
        c = c + 1
    
    if number % 5 == 0:
        d = d + 1

print(a, b, c, d) # 5 4 3 2 

# 문제 4

i = 0
while i <= 10:
    print(i)
    i = i + 1

# 0 1 2 3 4 5 6 7 8 9 10 (세로)

# 문제 5

i = 0
while i <= 10:
    i = i + 1
    print(i)

# 1 2 3 4 5 6 7 8 9 10 11 (세로)

# 문제 6

i = 0
while i <= 10:
    i = i + 2
    print(i)

# 2 4 6 8 10 12  (세로)

# 문제 7

i = 0 
while True:
    print(i)
    i = i + 1
    if i > 10:
        break
# 0 1 2 3 4 5 6 7 8 9 10 (세로)

# 문제 8

i = 0
while True:
    print(i)
    if i > 10:
        break
    i = i + 1

# 0 1 2 3 4 5 6 7 8 9 10 11 (세로)

# 문제 9

list_variable = [0, 1, 2, 3, 4, 5, 6]
print(len(list_variable)) # 7

# 문제 10 

list_variable = [0, 1, 2, 3, 4, 5, 6]
print(sum(list_variable)) # 21

# 문제 11

list_variable = [3, 1, 4, -3, 9, 7]
print(min(list_variable) - max(list_variable)) # -12