# Adds a class for the ticket to avoid structural complexity
class Ticket:
    def __init__(self, user_id: str, ticket_string: str):
        self.user_id = user_id
        self.ticket_string = ticket_string
        self.checked_in = False
