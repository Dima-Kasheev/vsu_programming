class Matrix:

    def __init__(self, elem):
        self.strok = None
        self.stolb = None
        self.elem = elem	
    
    def __str__(self): 
        f = ''
        for x in self.elem:
            f += '\n'
            for i in x:
                f += f'{i}  '
        return f
    
    def izmena(self, a, c, g):
        self.elem[a][c] = g

    def proverka(self):
        if not isinstance(g, int):
            print('Eto ne chislo')


b = [[1, 2] , [3, 4]]
alo = Matrix(b)
alo.izmena(1, 1, 7)
print(alo)
