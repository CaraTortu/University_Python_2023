#
i = 0
while i <= 9:
    print(i)
    i += 1

#b

n = int(input("Number to end with: "))
i = 0
while i <= n:
    print(i)
    i += 1


#

n = int(input("Squares less than: "))
i = 0
while i**2 < n:
    print(i**2)
    i += 1

#

n = int(input("N: "))
i = 0
while i <= n:
    if i % 10 == 0:
        print(i)
    
    i += 1


#

n = int(input("N: "))
i = 1
count = 1
while i <= n:
    print(i)
    i = 1 << count
    count += 1


