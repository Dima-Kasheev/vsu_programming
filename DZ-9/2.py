class Matrix:

    def __init__(self):
        self.strok = 0
        self.stolb = 0
        self.elem = []	
    def input(self):
        self.strok = int(input())
        self.stolb = int(input())
        for a in range(self.stolb):
            self.elem.append([input() for b in range(self.strok)])
        print()

class Matrix2x2(Matrix):

    def proverka(self):
        if  self.strok * self.stolb != 4:
            print("Matrix isn't 2x2")
        else:
            print("Matrix is 2x2")
            
            
example = Matrix2x2()
example.input()
example.proverka()
