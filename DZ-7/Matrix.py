class Matrix:

    def __init__(self):
        self.strok = None
        self.stolb = None
        self.elem = []

    def input_this(self):
        self.strok = int(input())
        self.stolb = int(input())
        for _ in range(self.stolb):
            self.elem.append([input() for b in range(self.strok)])

    def __str__(self):
        f = ''
        for x in self.elem:
            f += '\n'
            for i in x:
                f += f'{i} '
        return f


a = Matrix()
a.input_this()
print(a)
