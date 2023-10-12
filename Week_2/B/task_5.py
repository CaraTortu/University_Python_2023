string = input("String: ")

print(f"Contains only letters: {string.isalpha()}")
print(f"All uppercase: {string.isupper()}")
print(f"All lowercase: {string.islower()}")
print(f"Contains only digits: {string.isdigit()}")
print(f"Contains only letters and digits: {string.isalnum()}")
print(f"Starts with uppercase letter: {string[0].isupper()}")
print(f"Ends with a period: {string.endswith('0')}")

