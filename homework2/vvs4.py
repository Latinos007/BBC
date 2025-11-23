import math as m

class calculator():
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def calc(self, sign):
        if sign == '+':
            print(self.a + self.b)
        elif sign == '-':
            print(self.a - self.b)
        elif sign == '*':
            print(self.a * self.b)
        elif sign == '/':
            print(self.a / self.b)
        elif sign == '^':
            print(self.a ** self.b)

    def ing(self, sign, operand):
        if operand == 'a':
            if sign == 'sin':
                print(m.sin(self.a))
            elif sign == 'cos':
                print(m.cos(self.a))
        elif operand == 'b':
            if sign == 'sin':
                print(m.sin(self.b))
            elif sign == 'cos':
                print(m.cos(self.b))

main = calculator(input("введите первое число: "), input("введите второе число: "))

main.calc('+')
main.calc('-')
main.calc('/')
main.calc('*')
main.calc('^')

main.ing('sin', 'a')
main.ing('cos', 'a')
main.ing('sin', 'b')
main.ing('cos', 'b')