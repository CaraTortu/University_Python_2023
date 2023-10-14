def firstDigit(n: int) -> int:
    return int(str(n)[0])

def lastDigit(n: int) -> int:
    return int(str(n)[-1])

def digits(n: int) -> int:
    return len(str(n))

print(firstDigit(286))
print(lastDigit(3847))
print(digits(3874))

