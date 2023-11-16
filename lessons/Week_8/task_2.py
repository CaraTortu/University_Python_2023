try:
    number_a = int(input("Number A: "))
    number_b = int(input("Number B: "))

    if number_b == 0:
        print("ERROR: You can't divide by 0")
        exit(1)

    print(number_a / number_b)

except ValueError:
    print("ERROR: Invalid number supplied.")
