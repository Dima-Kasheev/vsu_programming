def fib(n):
    f1 = 0
    f2 = 1
    i = 0
    print(f1)
    print(f2)
    for i in range(n-2):
        i += 1
        s = f1 + f2
        f1 = f2
        f2 = s
        print(s)
a = int(input())

fib(a)
