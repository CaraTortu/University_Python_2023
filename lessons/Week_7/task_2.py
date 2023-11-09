def string_count(filename: str, target: str) -> int:
    with open(filename) as file:
        contents = file.read()
        
    return contents.count(target)

filename = input("Provide filename: ")
target_str = input("Provide the target string: ")
print(string_count(filename, target_str))

