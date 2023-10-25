def frequency(l: list) -> dict:
    names = {}

    for name in l:
        if name in names:
            names[name] += 1
            continue

        names[name] = 1

    return names

print(frequency(["Mary", "Shaun", "Colm", "Paddy", "Brendan", "Colm", "Mary", "Colm"]))
