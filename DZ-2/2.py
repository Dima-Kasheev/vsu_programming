f = input()
num_list = []
while f:
    num_list.append(f)
    f = input()
num_list = sorted(num_list, reverse=True)
print("".join(num_list))
