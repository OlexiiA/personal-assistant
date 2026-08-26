from decorators.Input import input_error
from modules.AddressBook import AddressBook
from modules.PersistStorage import PersistStorage
from modules.Record import Record


def parse_input(user_input: str) -> tuple[str, list[str]]:
    parts = user_input.split()
    if not parts:
        return "", []

    cmd, *args = parts
    return cmd.lower(), args

@input_error
def add_contact(args: list[str], book: AddressBook) -> str:
    name, phone, *_ = args

    record = book.find(name)
    message = "Contact updated."

    if record is None:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return "Contact added."

    record.add_phone(phone)
    return message


@input_error
def change_contact(args: list[str], book: AddressBook) -> str:
    name, phone, new_phone = args

    contact = book.find(name)

    if not contact:
        return "Contact not found."

    res = contact.edit_phone(phone, new_phone)

    return "Contact updated." if res else "Nothin' changed. Phone not found."


@input_error
def show_phone(args: list[str], book: AddressBook) -> Record | str:
    name = args[0]
    record = book.find(name)

    return record if record else "Contact not found."


@input_error
def show_all(book: AddressBook) -> str:
    if not book:
        return "No contacts saved."

    return "\n".join(f"{name}: {record}" for name, record in book.items())


@input_error
def add_birthday(args: list[str], book: AddressBook) -> str:
    name, birthday = args

    record = book.find(name)
    if not record:
        return "Contact not found."

    record.add_birthday(birthday)

    return "Birthday added."


@input_error
def show_birthday(args: list[str], book: AddressBook) -> str:
    name = args[0]

    record = book.find(name)
    if not record:
        return "Contact not found."

    if not record.birthday:
        return "Birthday not set."

    return str(record.birthday)


@input_error
def birthdays(book: AddressBook) -> str:
    upcoming = book.get_upcoming_birthdays()

    if not upcoming:
        return "No birthdays in the next week."

    return "\n".join(f"{u['name']}: {u['congratulation_date']}" for u in upcoming)


def main():
    storage = PersistStorage()
    book: AddressBook = storage.load()
    print("Welcome to the assistant bot!")

    while True:
        try:
            user_input = input("Enter a command: ")
        except (EOFError, KeyboardInterrupt):
            print("\nGood bye!")
            break

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        else:
            print("Invalid command. Available commands: hello, add, change, phone, all, add-birthday, show-birthday, birthdays, close, exit")

    storage.save(book)


if __name__ == "__main__":
    main()
