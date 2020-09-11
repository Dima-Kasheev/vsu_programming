import random
b = None
a = random.randint(0, 100)
while b != a:
    b = int(input("Введи число: "))
    if b < a:
        print("Число больше")
    elif b > a:
        print("Число меньше")
    else:
        print("Ты угадал")
