l = []
while len(l) < 10:
    i = input("Thing to add: ")

    if i in l:
        print(f"'{f}' is already in the list, add another one")
        continue

    l.append(i)

print(l)
