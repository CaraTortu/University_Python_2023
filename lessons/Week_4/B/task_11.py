def list_from_m_to_n(l: list, m: int, n: int) -> list:
    return l[m:n]

print(list_from_m_to_n([i for i in input("Input: ").split(" ")], 2, 6))
