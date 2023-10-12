def allTheSame(x: int, y: int, z: int) -> int:
    return x == y and y == z

def allDifferent(x: int, y: int, z: int) -> int:
    return x != y and x != z and y != z

def isSorted(x: int, y: int, z: int) -> int:
    return x <= y <= z


print(allTheSame(2, 2, 2))
print(allDifferent(2, 2, 2))
print(isSorted(4, 5, 6))
