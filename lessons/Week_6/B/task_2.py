def phone_lookup(phone_book: dict) -> None:
    # Get the number for the input
    while True:
        name_input = input("Enter the name: ")
        name_tuple = tuple(name_input.split(" "))

        # Break if the number exists as a key in the dictionary
        if name_tuple in phone_book:
            # Print the first and last name
            print(f"The person with the name {name_input} is {phone_book[name_tuple]}")
            continue

        print("[-] ERROR: This person does not exist in the phone book. Please try again.")


phone_lookup({("Bob", "Dylan"): 9122123,
              ("Isaac”, “Newton"): 9122134,
              ("Albert", "Einstein"): 9123473
              })
