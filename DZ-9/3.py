class Matrix:

    def __init__(self):
        self.strok = 0
        self.stolb = 0
        self.elem = []	
    def input(self):
        self.strok = int(input())
        self.stolb = int(input())
        for a in range(self.stolb):
            self.elem.append([int(input()) for b in range(self.strok)])
        print()
class Matrix2x2(Matrix):

    def determinant(self):
        if  self.strok * self.stolb != 4:
            print("Matrix isn't 2x2")
        else:
            n1 = 0
            n2 = 0   
            for a in range(self.stolb):
                for b in range(self.strok):
                    n1 = self.elem[0][0] * self.elem[self.strok - 1][self.stolb - 1]
                    n2 = self.elem[0][self.stolb - 1] * self.elem[self.strok - 1][0]
            print("Determinant 2x2:", n1 + n2)                    
            
example = Matrix2x2()
example.input()
example.determinant()
