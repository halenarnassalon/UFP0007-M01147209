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
class Laptop(Equipment):
    def loan_days(self):
        return 7
class Camera(Equipment):
    def loan_days(self):
        return 14 