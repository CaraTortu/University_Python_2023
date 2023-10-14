print(sum(i for i in range(2, 101) if i % 2 == 0))

print(sum(i for i in range(1, 11)))

a = int(input("a: "))
b = int(input("b: "))
print(sum(i for i in range(a, b+1) if i % 2 != 0))

n = input("n: ")
print(sum(int(i) for i in n if int(i) % 2 != 0))
