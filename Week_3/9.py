def is_prime(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

n = int(input("n: "))

for i in range(1, n+1):
    if is_prime(i):
        print(i, end=" ")
