
class BankAccount:
    def __init__(self, balance: float = 0.0) -> None:
        self._balance = balance

    def deposit(self, amount: float) -> None:
        """
        Deposit money into account

        Parameters:
            amount: float: Amount to deposit

        Returns:
            None
        """
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraws money from the account. 
        If there is not enough funds, apply 10€ fee

        Parameters:
            amount: float: Amount to withdraw

        Returns:
            None
        """
        
        if amount > self._balance:
            self._balance -= 10
            return

        self._balance -= amount

    def add_interest(self, interest: float) -> None:
        """
        Adds the interest to the account
        
        Parameters:
            interest: float: Interest to substract from account balance (From 0 to 100)

        Returns: 
            None
        """
        
        self._balance -= self._balance * interest/100
    
    def get_balance(self) -> float:
        """
        Returns the account balance.

        Parameters:
        Returns:
            float
        """

        return self._balance



if __name__ == "__main__":
    account: BankAccount = BankAccount(40.0)
    assert account.get_balance() == 40.0
    
    account.deposit(200.0)
    assert account.get_balance() == 240.0

    account.withdraw(240.0)
    assert account.get_balance() == 0.0

    account.withdraw(2.0)
    assert account.get_balance() == -10.0

    print("[+] All tests passed")

