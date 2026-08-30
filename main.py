from difflib import get_close_matches

from commands import book_commands, note_commands
from colorama import Fore, Style, init
from tabulate import tabulate

from modules.address_book import AddressBook
from modules.persist_storage import PersistStorage
from modules.note_book import NoteBook


COMMAND_EXAMPLES = [
    ("hello", "hello"),
    ("add", "add Alice 0123456789"),
    ("change", "change Alice 0123456789 0987654321"),
    ("edit-name", "edit-name Alice Alicia"),
    ("remove-contact", "remove-contact Alice"),
    ("phone", "phone Alice"),
    ("all", "all"),
    ("add-birthday", "add-birthday Alice 25.12.2000"),
    ("show-birthday", "show-birthday Alice"),
    ("birthdays", "birthdays 14"),
    ("search-contacts", "search-contacts kyiv"),
    ("add-email", "add-email Alice alice@example.com"),
    ("edit-email", "edit-email Alice new@example.com"),
    ("add-address", "add-address Alice Kyiv Main Street 1"),
    ("edit-address", "edit-address Alice Lviv Shevchenka Street 10"),
    ("add-note", "add-note Buy-milk"),
    ("all-notes", "all-notes"),
    ("search-note", "search-note milk"),
    ("edit-note", "edit-note 1 Buy milk today"),
    ("remove-note", "remove-note 1"),
    ("help", "help"),
    ("close", "close"),
    ("exit", "exit"),
]

COMMANDS = [name for name, _ in COMMAND_EXAMPLES]


def show_help() -> str:
    table = tabulate(COMMAND_EXAMPLES, headers=["Command", "Example"], tablefmt="grid")
    return Fore.CYAN + table + Style.RESET_ALL

def parse_input(user_input: str) -> tuple[str, list[str]]:
    parts = user_input.split()
    if not parts:
        return "", []

    cmd, *args = parts
    return cmd.lower(), args


def main():
    init(autoreset=True)

    book_storage = PersistStorage("addressbook.pkl", AddressBook)
    book: AddressBook = book_storage.load()

    note_storage = PersistStorage("notebook.pkl", NoteBook)
    notebook: NoteBook = note_storage.load()

    print(Fore.CYAN + Style.BRIGHT + "=" * 38)
    print(Fore.CYAN + Style.BRIGHT + "       PERSONAL ASSISTANT")
    print(Fore.CYAN + Style.BRIGHT + "=" * 38)
    print(Fore.GREEN + "Welcome! Type a command to get started.")
    print(Fore.CYAN + "Available commands: " + ", ".join(COMMANDS))

    while True:
        try:
            user_input = input(Fore.YELLOW + "\nEnter a command: " + Style.RESET_ALL)
        except (EOFError, KeyboardInterrupt):
            print(Fore.MAGENTA + "\nGood bye!")
            break

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(Fore.MAGENTA + "Good bye!")
            break
        elif command == "hello":
            print(Fore.GREEN + "How can I help you?")
        elif command == "help":
            print(show_help())
        elif command == "add":
            print(book_commands.add_contact(args, book))
        elif command == "change":
            print(book_commands.change_contact(args, book))
        elif command == "edit-name":
            print(book_commands.edit_name(args, book))
        elif command == "remove-contact":
            print(book_commands.remove_contact(args, book))
        elif command == "phone":
            print(book_commands.show_phone(args, book))
        elif command == "all":
            print(book_commands.show_all(book))
        elif command == "add-birthday":
            print(book_commands.add_birthday(args, book))
        elif command == "show-birthday":
            print(book_commands.show_birthday(args, book))
        elif command == "birthdays":
            print(book_commands.birthdays(args, book))
        elif command == "search-contacts":
            print(book_commands.search_contacts(args, book))
        elif command == "add-email":
            print(book_commands.add_email(args, book))
        elif command == "edit-email":
            print(book_commands.edit_email(args, book))
        elif command == "add-address":
            print(book_commands.add_address(args, book))
        elif command == "edit-address":
            print(book_commands.edit_address(args, book))
        elif command == "add-note":
            print(note_commands.add_note(args, notebook))
        elif command == "all-notes":
            print(note_commands.show_all_notes(notebook))
        elif command == 'search-note':
            print(note_commands.search_note(args, notebook))
        elif command == 'edit-note':
            print(note_commands.edit_note(args, notebook))
        elif command == 'remove-note':
            print(note_commands.remove_note(args, notebook))
        else:
            print(Fore.RED + "Invalid command.")

            suggestions = get_close_matches(command, COMMANDS, n=1)
            if suggestions:
                print(Fore.YELLOW + f"Did you mean '{suggestions[0]}'?")
            else:
                print(Fore.YELLOW + "Type 'help' to see available commands.")

    book_storage.save(book)
    note_storage.save(notebook)


if __name__ == "__main__":
    main()
