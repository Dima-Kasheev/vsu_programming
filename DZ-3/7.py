stroka = input().split()
a = list(map(len, stroka))
print(stroka[a.index(max(a))])
a = [stroka.count(x) for x in set(stroka)]
print(list(set(stroka))[a.index(max(a))])
