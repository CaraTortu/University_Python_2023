def find_word_in_line(filename: str, target: str) -> None:
    with open(filename) as file:
        lines = file.readlines()
    
    to_write = "".join(filter(lambda x: x.count(target) != 0, lines))
    
    with open("results.txt", "w") as file:
        file.write(to_write)

find_word_in_line("test.txt", "so")

