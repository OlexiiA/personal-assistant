import pickle

from modules.AddressBook import AddressBook


class PersistStorage:
    def __init__(self, filename: str = "addressbook.pkl") -> None:
        self.filename = filename

    def save(self, book: AddressBook) -> None:
        with open(self.filename, "wb") as f:
            pickle.dump(book, f)

    def load(self) -> AddressBook:
        try:
            with open(self.filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return AddressBook()
