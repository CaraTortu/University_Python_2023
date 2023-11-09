
def copy_file(input_file: str, output_file: str, to_remove: str) -> None:
    with open(input_file, "r") as input_reader:
        contents = input_reader.readlines()

    with open(output_file, "a") as output_writer:
        for line in contents:
            output_writer.write(line.replace(to_remove, ""))

copy_file("test.txt", "test2.txt", input("To remove: "))
