lst = []
x = input()
while x:
    lst.append(x)
    x = input()
for i in set(lst):
    print(f'{i} | {lst.count(i)}')
