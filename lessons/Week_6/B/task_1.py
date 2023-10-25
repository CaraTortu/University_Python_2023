def name_lookup(phone_book: dict) -> None:
    # Get the number for the input
    while True:
        number_input = int(input("Enter the phone number: "))

        # Break if the number exists as a key in the dictionary
        if number_input in phone_book:
            # Print the first and last name
            print(f"The person with the phone number {number_input} is {' '.join(phone_book[number_input])}")
            continue

        print("[-] ERROR: Number does not exist in the phone book. Please try again.")


name_lookup({
    9122123: ["Bob", "Dylan"],
    9122134: ["Isaac”, “Newton"],
    9128021: ["Mary", "Robinson"]
})
