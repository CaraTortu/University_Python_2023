from classes.user import User
from classes.stadium import Stadium, ROWS, COLUMNS

################ NOT LOGGED IN ################## 

# Registers a new user
def register() -> User:
    # Create user object
    user_name = input("What is your name?: ")   
    user = User(user_name)

    # Show their pin
    print(f"[+] You have been successfully registered! Your user ID id is '{user.id}' and pin to you account is '{user.pin}'")
    
    return user

# Logs in a new user
def log_in(stadium: Stadium) -> User | None:
    user_id = input("Please enter your user ID: ")
    user_pin = input("Please enter your pin: ")
    
    for user in stadium.users:
        if user.id == user_id and user.pin == user_pin:
            print("[+] Success!")
            return user

    print("[-] ERROR: Invalid user ID or pin.")
    return None

# Handles the menu selection for non-authenticated users
def handle_not_logged_in(option_chosen: int, stadium: Stadium) -> User:
    match option_chosen:
        case 1:
            user = register()
            stadium.users.append(user)
            return user
        case 2:
            return log_in(stadium)


################# ADMIN ###################

# Lists all the details for all users registered
def list_user_details(stadium: Stadium):
    for i, user in enumerate(stadium.users):
        # Print user stuff
        print(f"{i}:")
        print(f"\tUser ID: {user.id}")
        print(f"\tUser Pin: {user.pin}")
        print(f"\tUser Name: {user.name}")
        print(f"\tIs user admin?: {user.is_admin}")
        
        # Print tickets
        print(f"\tTickets:")
        for j, ticket in enumerate(user.tickets):
            print(f"\t\t{j}. {ticket.ticket_string}")

        # Newline for format
        print()

# Print the tickets assigned to the user by the supplied ID
def search_ticket_by_user_id(stadium: Stadium):
    user_id = input("What is the user ID: ")
    
    # Search for the user
    user_to_get_tickets = None

    for user in stadium.users:
        if user.id == user_id:
            user_to_get_tickets = user
            break

    # Check if the user was not found 
    if not user_to_get_tickets:
        print("[-] User not found")
        return

    # Check if the user has tickets or not and print them
    if len(user.tickets) == 0:
        print("[+] This user has no tickets.")

    for i, ticket in enumerate(user.tickets):
        print(f"{i}. {ticket.ticket_string}")

# Checks whether a ticket is invalid or not
def validate_ticket(stadium: Stadium):
    ticket = input("Ticket to verify: ")
    does_ticket_exist = stadium.verify_ticket(ticket)[0]

    if not does_ticket_exist:
        print("[+] Ticket is invalid!")
        return

    print("[+] Ticket is valid!")

# Handle the options for admin users.
def handle_admin(option_chosen: int, stadium: Stadium):
    match option_chosen:
        case 1:
            list_user_details(stadium)
        case 2:
            search_ticket_by_user_id(stadium)
        case 3:
            validate_ticket(stadium)

################# LOGGED IN ####################

# Books a new ticket
def book_ticket(stadium: Stadium, user: User):
    print(stadium.__str__(user=user))
    
    # Make sure that the seat isnt taken
    while True: 
        # Get the row
        row = -1
        while row < 0 or row > ROWS-1:
            row = int(input(f"Please select a row [1-{ROWS}]: ")) - 1

        # Get the column
        column = -1
        while column < 0 or column > COLUMNS-1:
            column = int(input(f"Please select a column [1-{COLUMNS}]: ")) - 1

        # Check if ticket is already set for this seat
        if stadium.seats[row][column] == "X":
            print("That seat is already taken, pleas try again!")
            continue

        break

    # Book the ticket
    ticket = stadium.add_ticket(row, column, user)

    print(f"\n[+] Your ticket number is: {ticket}")

# Delete a ticket from this user
def delete_ticket(stadium: Stadium, user: User):
    # Get a valid ticket numer
    ticket_string = ""    
    while ticket_string not in stadium.tickets or stadium.tickets[ticket_string].user_id != user.id:
        ticket_string = input("Please enter your ticket number: ")

    # Remove it
    stadium.delete_ticket(ticket_string)

# Print all the tickets that belong to the user
def print_tickets(user: User): 
    if len(user.tickets) == 0:
        print("[+] You have not booked any tickets!")
        return

    for i, ticket in enumerate(user.tickets):
        print(f"{i+1}. {ticket.ticket_string}")

# Handle menu options for logged in users
def handle_logged_in(current_user: User, option_chosen: int, stadium: Stadium):
    match option_chosen:
        case 1:
            print(stadium.__str__(user=current_user))
        case 2:
            book_ticket(stadium, current_user)
        case 3:
            delete_ticket(stadium, current_user)
        case 4:
            print_tickets(current_user)

