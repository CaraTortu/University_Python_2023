def removeHighest(n: list) -> list:
    n.sort()
    n.pop()
    
    return n

print(removeHighest([3, 5, 2, 7, 4, 9]))

