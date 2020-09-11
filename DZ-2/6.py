s = input("Strochka vasha: ")
chislo = int(input("Chislo? "))
m = []
for a in s:
    if "0" <= a <= "9":
        m.append(a)
print(m)
print(m[chislo - 1])
