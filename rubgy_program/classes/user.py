from classes.ticket import Ticket
import random
import string

class User:
    def __init__(self, name: str):
        self.pin = self.generate_pin()
        self.name = name
        self.id = self.generate_id()
        self.is_admin = False
        # Tickets saved by the user
        self.tickets = []

    def __str__(self) -> str:
        return f"Name: {self.name} | Pin: {self.pin} | User id: {self.id}"

    def generate_id(self) -> str:
        return "".join(random.choices(string.ascii_letters + string.digits, k=8))

    def generate_pin(self) -> str:
        return "".join(random.choices(string.digits, k=4)) 
  
    def delete_ticket(self, ticket: Ticket):
        for i, t in enumerate(self.tickets):
            if t == ticket:
                self.tickets.pop(i)
                return
