def weird_sum(n: list) -> int:
    
    for i in range(1, len(n), 2):
        n[i] *= -1

    return sum(n)

print(weird_sum([1, 4, 9, 16, 9, 7, 4, 9, 11]))
