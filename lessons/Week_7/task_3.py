def find_word_in_line(filename: str, target: str) -> None:
    with open(filename) as file:
        lines = file.readlines()
    
    for line in lines:
        if line.count(target) != 0:
            print(line.strip())

find_word_in_line("test.txt", "so")

