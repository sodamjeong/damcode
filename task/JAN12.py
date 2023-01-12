# 클래스 생성하기

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def plus(self):
        return self.x + self.y
    def minus(self):
        return self.x - self.y
    def multiply(self):
        return self.x * self.y
    def division(self):
        return self.x // self.y
    def __str__(self):
        return f'합 : {self.x + self.y}\n빼기 : {self.x - self.y}\n곱 : {self.x * self.y}\n몫 : {self.x // self.y}'

calculator = Calculator(10, 5)
print(calculator.plus())

calculator.x = -2
calculator.y = 2
print(calculator.plus())

calculator = Calculator(10, 5)
print(calculator.minus())

calculator.x = -2
calculator.y = 2
print(calculator.minus())

calculator = Calculator(10, 5)
print(calculator.multiply())

calculator.x = -2
calculator.y = 2
print(calculator.multiply())

calculator = Calculator(10, 5)
print(calculator.division())

calculator.x = -2
calculator.y = 2
print(calculator.division())


calculator = Calculator(10, 5)
print(calculator)

calculator.x = -2
calculator.y = 2
print(calculator)




