
def copy_file(input_file: str, output_file: str) -> None:
    with open(input_file, "r") as input_reader:
        contents = input_reader.readlines()

    with open(output_file, "a") as output_writer:
        for line in contents:
            output_writer.write(line.translate(str.maketrans('aeiou', 5*'@')))

copy_file("test.txt", "test2.txt")
