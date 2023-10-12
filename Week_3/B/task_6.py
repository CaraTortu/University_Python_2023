def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n

    return fib(n-1) + fib(n-2)

n = int(input("Number of the fib sequence? "))
print(fib(n))
