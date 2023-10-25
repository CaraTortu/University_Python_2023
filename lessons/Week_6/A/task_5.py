def word_count(s: str) -> dict:
    letter_count = {}

    for c in s.lower():
        if c in letter_count:
            letter_count[c] += 1
            continue
        letter_count[c] = 1

    return letter_count

print(word_count("occurrence"))
