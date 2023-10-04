import re
s = input("String: ")

print("".join([i for i in s if i.isupper()]))
print("".join([s[i] for i in range(0, len(s), 2)]))
print(re.sub(r"[aeiou]", "_", s))
print(" ".join([str(i) for i in range(len(s)) if s[i].lower() in "aeiou"]))
