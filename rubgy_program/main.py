from classes.stadium import Stadium
from classes.user import User
from utils.test import run_all_tests
from utils.utils import handle_not_logged_in, handle_logged_in, handle_admin

def print_menu():
    global current_user

    # Define the menu
    if current_user == None:
        menu = "\nRugby world cup:\n"
        menu += "1. Register\n"
        menu += "2. Log in\n"

    elif current_user.is_admin:
        menu = f"\nHi {current_user.name}! What would you like to do?: \n"
        menu += "1. List details of all registered users\n"
        menu += "2. Search for ticket by user ID\n"
        menu += "3. Validate Ticket\n"
        menu += "4. Log out\n"

    else:
        menu = f"\nHi {current_user.name}! Choose your option:\n"
        menu += "1. Display ALL Tickets/Seats\n"
        menu += "2. Book a ticket\n"
        menu += "3. Cancel a ticket\n"
        menu += "4. List all tickets booked\n"
        menu += "5. Log out\n"
        
    menu += "0. Quit\n"
         
    # Print the menu
    print(menu)

def main(stadium: Stadium):
    global current_user

    # Print menu
    print_menu()

    # Get the input
    option_chosen = input("Enter option: ")
    
    # Check if option supplied is valid
    if not option_chosen.isdigit() or int(option_chosen) < 0 or int(option_chosen) > 8:
        print("ERROR: invalid option. Please try again")
        return True
   
    # Convert to Int
    option_chosen = int(option_chosen)

    # Check if the user wants to quit, if so, stop loop
    if option_chosen == 0:
        return False

    # Handle user cases
    if current_user == None:
         current_user = handle_not_logged_in(option_chosen, stadium)
    
    elif current_user.is_admin:
        handle_admin(option_chosen, stadium)
        if option_chosen == 4: current_user = None
    
    else: 
        handle_logged_in(current_user, option_chosen, stadium)
        if option_chosen == 5: current_user = None

    # Keep the loop going    
    return True

if __name__ == "__main__":
    # UNCOMMENT TO RUN ALL TESTS
    # run_all_tests()

    stadium = Stadium()
    current_user = None

    # Add admin User
    admin = User("Admin")
    admin.is_admin = True
    admin.id = "0000"
    admin.pin = "1234"

    stadium.users.append(admin)

    # Run main loop
    while main(stadium): pass
