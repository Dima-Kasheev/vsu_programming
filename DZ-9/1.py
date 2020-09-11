
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


b = [[1,2,3] , [4,5,6]]
alo = Matrix(b)
print(alo)
