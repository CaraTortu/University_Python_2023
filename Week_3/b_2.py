n = int(input("Number: "))

table = [["Number", "Square", "Cube"]]

for i in range(1, n+1):
    table.append([i, i**2, i**3])

for row in table:
    print("{:<10}{:<10}{:<10}".format(*row))
