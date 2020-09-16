class Fraction:

    def __init__(self, a, b):
        self.a = 0
        self.b = 0


    def InputValue(self):
        self.a = int(input("Введите число 1:\n"))
        self.b = int(input("Введите число 2:\n"))


    def __str__(self):
        return str(self.a) + "/" + str(self.b)


    def __str__(self):
        print(" ")
        print(self.a, "/", "\n", "/", self.b)


program = Fraction(0,0)
program.InputValue()
program.__str__()
