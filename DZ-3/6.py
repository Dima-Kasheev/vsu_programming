import math
def is_prime1(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if not n % i: 
            return False
    return True
a = int(input())
print(is_prime1(a))
