s = input("String: ")

print(f"Uppercase characters: {len([i for i in s if i.isupper()])}")
print(f"Lowercase characters: {len([i for i in s if i.islower()])}")
print(f"Vowels: {len([i for i in s if i.lower() in 'aeiou'])}")
print(f"Digits: {len([i for i in s if i.isdigit()])}")
