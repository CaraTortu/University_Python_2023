from random import choices

arr = choices(range(1, 51), k=10)

# Print every element at an even index 
for i in range(int(len(arr) / 2)):
    print(arr[i], end=" ")

print("\n")

# Every even element
evens = list(filter(lambda x: x % 2 == 0, arr))
print(evens, end="\n\n")

# All elements in reverse order
print(list(reversed(arr)), end="\n\n")

# Only the first and last elements
print(f"{arr[0]} {arr[-1]}\n")

