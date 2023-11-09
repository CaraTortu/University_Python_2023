
def copy_file(input_file: str, output_file: str) -> None:
    with open(input_file, "r") as input_reader:
        contents = input_reader.readlines()

    with open(output_file, "a") as output_writer:
        for i, line in enumerate(contents):
            output_writer.write(f"{i} {line}")

copy_file("test.txt", "test2.txt")
