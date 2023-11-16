try:
    age = int(input("What's your age?: "))
    print(f"You are {age} years old.")
except ValueError:
    print("ERROR: Value supplied was not a valid number")
