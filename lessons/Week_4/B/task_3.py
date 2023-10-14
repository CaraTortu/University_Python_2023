def sumWithoutSmallest(n: list) -> int:
    n.sort()
    n.pop(0)

    return sum(n)


print(sumWithoutSmallest([1, 4, 5, 2, 5, 3]))
