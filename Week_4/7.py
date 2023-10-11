def readIntBtw(x: int, y: int) -> int:
    res = x-1
    while res not in range(x, y):
        res = input(f"Enter a value from {x} to {y}: ")

    return res

print(readIntBtw(2, 6))
