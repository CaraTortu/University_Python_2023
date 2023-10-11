def freq(n: list) -> int:
    min_word_len = min([len(i) for i in n])
    return sum([1 for i in n if len(i) == min_word_len])

print(freq(["this", "is", "a", "test", "frog", "b"]))
