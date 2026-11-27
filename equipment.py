from datetime import timedelta
from tracemalloc import start


class Equipment:
    def __init__(self, item_id, name):
        item_id = item_id.strip().upper()
        if not item_id:
            raise ValueError("ID cannot be blank.")

        self.__item_id = item_id
        self.rename(name)
        self.__borrower = ""
        self.__due = None

    def get_item_id(self):
        return self.__item_id

    def get_name(self):
        return self.__name

    def get_borrower(self):
        return self.__borrower

    def get_due(self):
        return self.__due

    def rename(self, name):
        name = name.strip()
        if not name:
            raise ValueError("Name cannot be blank.")
        self.__name = name

    def loan_days(self):
        return 1

    def restore_loan(self, borrower, due):
        if self.__due is not None:
            raise ValueError("Item is already on loan.")
        if borrower == "":
            raise ValueError("Borrower cannot be blank.")
        if type(due) is not date:
            raise ValueError("A date is required.")
        self.__borrower = borrower
        self.__due = due

    def lend(self, borrower, due):
        if type(start) is not date:
            raise ValueError("A start date is required.")

        days = self.loan_days()
        due = start + timedelta(days=days)
        self.restore_loan(borrower, due)

    def resturn_item(self):
        if self.__due is None:
            raise ValueError("Item is already available.")
        self.__borrower = ""
        self.__due = None

    def is_overdue(self, today):
        if self.__due is None:
            return false

        return today > self.__due 
    
class Laptop(Equipment):
    def loan_days(self):
        return 7
    
class Camera(Equipment):
    def loan_days(self):
        return 14 