def copy_file(input_file: str, output_file: str) -> None:
    with open(input_file, "r") as input_reader:
        contents = input_reader.read()

    with open(output_file, "w") as output_writer:
        output_writer.write(contents)

copy_file("test.txt", "test2.txt")

