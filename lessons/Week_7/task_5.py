import string


def words(filename: str) -> list[str]:
    words_found = set()

    with open(filename) as file:
        contents = file.readlines()

    for line in contents:
        for word in line.strip().split():
            word = word.translate(str.maketrans(
                string.punctuation, len(string.punctuation) * ' '))
            words_found.add(word)

    print(words_found)


words("test.txt")
