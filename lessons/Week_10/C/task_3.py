from typing import List


class CashRegister:
    def __init__(self) -> None:
        self._items = []
        self._total_in_the_day = []

    def add_item(self, item: str, price: float) -> None:
        """
        Adds an item to the cash register

        Parameters:
            item: str: The name of the product
            price: float: The price of the item

        Returns:
            None
        """
        self._items.append((item, price))

    def get_total(self) -> float:
        """
        Get the total to pay

        Parameters:
        Returns:
            float
        """
        return sum(map(lambda x: x[1], self._items))
    
    def get_items_purchased(self) -> List[str]:
        """
        Get the items that have been scanned

        Parameters:
        Returns:
            List[str]
        """
        return list(map(lambda x: x[0], self._items))

    def clear(self) -> None:
        """
        Clears the cash register for the next use and updates the total 
        for the day
        
        Parameters:
        Returns:
            None
        """
        self._total_in_the_day.append(self.get_total())
        self._items = []


    def display_all(self) -> None:
        """
        Print all the items and their prices

        Parameters:
        Returns:
            None
        """

        for item in self._items:
            print(f"{item[0]}: {item[1]}€")

    def get_sales_total(self) -> float:
        """
        Get the total amount of money made in the day
        
        Parameters:
        Returns: 
            float
        """
        
        return sum(self._total_in_the_day)

    def get_sales_count(self) -> int:
        """
        Get the amount of sales made in the day

        Parameters:
        Returns:
            int
        """

        return len(self._total_in_the_day)

    def reset_sales(self) -> None:
        """
        Resets the sales for the day.

        Parameters:
        Returns:
            None
        """
        
        self.clear()
        self._total_in_the_day = []


if __name__ == "__main__":
    cash_register: CashRegister = CashRegister()

    cash_register.add_item("Banana", 10.0)
    assert cash_register.get_total() == 10.0
    assert cash_register.get_items_purchased() == ["Banana"]

    cash_register.add_item("Apple", 20.0)
    assert cash_register.get_total() == 30.0
    assert cash_register.get_items_purchased() == ["Banana", "Apple"]

    cash_register.display_all()

    cash_register.clear()
    assert cash_register.get_total() == 0
    assert cash_register.get_items_purchased() == []

    print("[+] All test cases passed")
