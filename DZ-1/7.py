x = int(input('x: '))
y = int(input('y: '))
a = 0
for f in range(x, y + 1):
    if not f % 5:
        a += x
print(a)
