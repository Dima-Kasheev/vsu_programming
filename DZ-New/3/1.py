from fractions import Fraction

class Fraction:

def __init__(self, a, b):
self.a = 0
self.b = 0
self.result = ""

def InputValue(self):
self.a = int(input("Введите число 1\n"))
self.b = int(input("Введите число 2\n"))

def ShowResult(self):
res = Fraction(self.a, self.b)
print(res)

program = Fraction(0,0)
program.InputValue()
program.ShowResult()
