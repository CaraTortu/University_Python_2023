poem = """Mary had a little lamb,
His fleece was white as snow,
And everywhere that Mary went,
The lamb was sure to go"""

#a
print(poem)

#b
print(poem.upper())

print(poem.title())

print(poem * 4)

print(len(poem))

print(poem.count("Mary"))

print(poem.index("was"))

print(poem.index("was", poem.index("was")+1))

print(f"The word returned is: {poem[5:10]}")

print(poem.replace("Mary", "Javier"))

print("lamb" in poem)

print(poem.split(" "))

print(poem.split("\n"))

print(len(poem.split(" ")))


