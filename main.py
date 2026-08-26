import commands

from modules.AddressBook import AddressBook
from modules.PersistStorage import PersistStorage


def parse_input(user_input: str) -> tuple[str, list[str]]:
    parts = user_input.split()
    if not parts:
        return "", []

    cmd, *args = parts
    return cmd.lower(), args


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
            print(commands.add_contact(args, book))
        elif command == "change":
            print(commands.change_contact(args, book))
        elif command == "phone":
            print(commands.show_phone(args, book))
        elif command == "all":
            print(commands.show_all(book))
        elif command == "add-birthday":
            print(commands.add_birthday(args, book))
        elif command == "show-birthday":
            print(commands.show_birthday(args, book))
        elif command == "birthdays":
            print(commands.birthdays(book))
        else:
            print("Invalid command. Available commands: hello, add, change, phone, all, add-birthday, show-birthday, birthdays, close, exit")

    storage.save(book)


if __name__ == "__main__":
    main()
