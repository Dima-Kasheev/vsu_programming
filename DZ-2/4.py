def skobochki(a):
    otkr_s = a.count('(')
    zakr_s = a.count(')')
    if otkr_s > zakr_s:
        return 'Не хватает закрывающих скобок: ', otkr_s - zakr_s
    elif otkr_s < zakr_s:
        return 'Не хватает открывающих скобок: ', zakr_s - otkr_s
    return 'Всех скобок хватает'

print(skobochki(input('Введите пример: ')))
