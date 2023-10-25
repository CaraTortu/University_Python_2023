from copy import deepcopy


def phone_lookup(phone_book: dict) -> None:
    while True:
        lastname_input = input("Enter the last name: ")
        # Remove the items in the dictionary without the last name we are looking for
        people_with_same_lastname = filter(lambda x: x[1] == lastname_input, phone_book.keys())

        # Join the names of the people we have found from ('x', 'y') to "x y"
        people_with_same_lastname = list(map(lambda x: ' '.join(x), people_with_same_lastname))

        # Print the people if we found any
        if len(people_with_same_lastname) != 0:
            print(f"The people with the last name {lastname_input} are {', '.join(people_with_same_lastname)}")
            continue

        print("[-] ERROR: There are no other people in the phone book with this last name. Please try again.")


phone_lookup({("Bob", "Dylan"): 9122123,
              ("Isaac”, “Newton"): 9122134,
              ("Albert", "Einstein"): 9123473
              })
