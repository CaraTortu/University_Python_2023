from classes.user import User
from classes.ticket import Ticket

COLUMNS = 8
ROWS = 5
STADIUM_LETTER = "P"

class Stadium:
    def __init__(self):
        # Define the seats with constant proportions
        
        self.seats = []

        for i in range(ROWS):
            self.seats.append(["O", "O", "O", "O", "O", "O", "O", "O"])
        
        # Ticket HashMap<ticket_string, Ticket>
        self.tickets = {}

        # Users that exist
        self.users = []

    def __str__(self) -> str:
        # Add column numeration
        s = "    1 2 3 4 5 6 7 8\n"
        s += "--------------------\n"

        # Add rows and columns with their respective number
        for i in range(ROWS):
            s += f"{i+1} | "
            for j in range(COLUMNS):
                s += self.seats[i][j] + " "

            s += "\n"

        # Return the string
        return s

    # Returns whether the seat is taken or not
    def is_position_available(self, column: int, row: int) -> bool:
        return self.seats[row][column] == "O"

    def calculate_check_digit(self, user_pin: str, column: int, row: int) -> str:
        # Set the user pin from a string to a list of digits
        user_pin = [int(digit) for digit in user_pin]
        
        # check_digit = d4 + 2d3 + 3d2 + 4d1 + 5c + 6r
        check_digit = user_pin[3]
        check_digit += 2 * user_pin[2]
        check_digit += 3 * user_pin[1]
        check_digit += 4 * user_pin[0]
        check_digit += 5 * column
        check_digit += 6 * row

        # Return the calculated check digit
        return str(check_digit)
 
    # Create new ticket and return it
    def add_ticket(self, row: int, column: int, user: User) -> str:
        # Get the check digit
        check_digit = self.calculate_check_digit(user.pin, column, row)

        # Ticket number in form of PrcddddX
        ticket_number = STADIUM_LETTER
        ticket_number += f"{row}{column}"
        ticket_number += user.pin
        ticket_number += check_digit

        # Create ticket class
        ticket = Ticket(user.id, ticket_number)

        # Add the ticket to our list
        self.tickets[ticket_number] = ticket

        # Add ticket to the user
        user.tickets.append(ticket)

        # Set the seat as taken
        self.seats[row][column] = "X"

        # Return the ticket
        return ticket_number


    # Verify that the ticket exists [0] and if it has been checked in [1]
    def verify_ticket(self, ticket_string: str) -> (bool, bool):
        if ticket_string in self.tickets:
                return (True, self.tickets[ticket_string].checked_in)

        return (False, False)

    # Checks in a ticket
    # Returns whether successful or not
    def check_in_ticket(self, ticket_string: str) -> bool:
        ticket_exists, ticket_checked_in = self.verify_ticket(ticket_string)
        
        # Check if the ticket exists and is not checked in
        if not ticket_exists or ticket_checked_in:
            return False
       
        # Set the ticket to checked in
        self.tickets[ticket_string].checked_in = True

        # Return success
        return True

    # Delete Ticket
    def delete_ticket(self, ticket_string: str):
        # Delete it from our internal list
        ticket = self.tickets[ticket_string]
        self.tickets.pop(ticket_string)

        # Delete it from the users list
        for user in self.users:
            if ticket.user_id == user.id:
                user.delete_ticket(ticket)
        
        # Refresh the seats
        self.seats[int(ticket_string[1])][int(ticket_string[2])] = "O"
    
        print(f"[+] Ticket {ticket_string} has been deleted!")

