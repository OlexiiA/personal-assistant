from colorama import Fore, Style
from tabulate import tabulate

from decorators.Input import input_error
from modules.AddressBook import AddressBook
from modules.Record import Record


def make_contacts_table(records: list[Record]) -> str:
    rows = []

    for record in records:
        phones = ", ".join(phone.value for phone in record.phones)
        birthday = str(record.birthday) if record.birthday else "-"
        email = str(record.email) if record.email else "-"
        address = str(record.address) if record.address else "-"

        rows.append([
            record.name.value,
            phones or "-",
            birthday,
            email,
            address,
        ])

    headers = ["Name", "Phones", "Birthday", "Email", "Address"]
    table = tabulate(rows, headers=headers, tablefmt="grid")

    return Fore.CYAN + table + Style.RESET_ALL


@input_error
def add_contact(args: list[str], book: AddressBook) -> str:
    name, phone, *_ = args

    record = book.find(name)
    message = Fore.GREEN + "Contact updated." + Style.RESET_ALL

    if record is None:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return Fore.GREEN + "Contact added." + Style.RESET_ALL

    record.add_phone(phone)
    return message


@input_error
def change_contact(args: list[str], book: AddressBook) -> str:
    name, phone, new_phone = args

    contact = book.find(name)

    if not contact:
        return Fore.RED + "Contact not found." + Style.RESET_ALL

    res = contact.edit_phone(phone, new_phone)

    if res:
        return Fore.GREEN + "Contact updated." + Style.RESET_ALL

    return Fore.RED + "Nothing changed. Phone not found." + Style.RESET_ALL


@input_error
def edit_name(args: list[str], book: AddressBook) -> str:
    old_name, new_name = args

    contact = book.find(old_name)
    if not contact:
        return Fore.RED + "Contact not found." + Style.RESET_ALL

    if book.find(new_name):
        return Fore.RED + "Contact with this name already exists." + Style.RESET_ALL

    book.delete(old_name)
    contact.edit_name(new_name)
    book.add_record(contact)

    return Fore.GREEN + "Contact name updated." + Style.RESET_ALL


@input_error
def remove_contact(args: list[str], book: AddressBook) -> str:
    name = args[0]

    contact = book.find(name)
    if not contact:
        return Fore.RED + "Contact not found." + Style.RESET_ALL

    book.delete(name)
    return Fore.GREEN + "Contact deleted." + Style.RESET_ALL


@input_error
def show_phone(args: list[str], book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)

    if not record:
        return Fore.RED + "Contact not found." + Style.RESET_ALL

    return make_contacts_table([record])


@input_error
def show_all(book: AddressBook) -> str:
    if not book:
        return Fore.RED + "No contacts saved." + Style.RESET_ALL

    records = list(book.values())
    return make_contacts_table(records)

@input_error
def add_birthday(args: list[str], book: AddressBook) -> str:
    name, birthday = args

    record = book.find(name)
    if not record:
        return Fore.RED + "Contact not found." + Style.RESET_ALL

    record.add_birthday(birthday)

    return Fore.GREEN + "Birthday added." + Style.RESET_ALL


@input_error
def show_birthday(args: list[str], book: AddressBook) -> str:
    name = args[0]

    record = book.find(name)
    if not record:
        return Fore.RED + "Contact not found." + Style.RESET_ALL

    if not record.birthday:
        return Fore.RED + "Birthday not set." + Style.RESET_ALL

    return Fore.GREEN + str(record.birthday) + Style.RESET_ALL


@input_error
def birthdays(book: AddressBook) -> str:
    upcoming = book.get_upcoming_birthdays()

    if not upcoming:
        return Fore.RED + "No birthdays in the next week." + Style.RESET_ALL

    rows = []
    for birthday in upcoming:
        rows.append([birthday["name"], birthday["congratulation_date"]])

    headers = ["Name", "Congratulation date"]
    table = tabulate(rows, headers=headers, tablefmt="grid")
    return Fore.MAGENTA + table + Style.RESET_ALL

@input_error
def add_email(args: list[str], book: AddressBook) -> str:
    name, email = args

    record = book.find(name)
    if not record:
        return Fore.RED + "Contact not found." + Style.RESET_ALL

    record.add_email(email)

    return Fore.GREEN + "Email added." + Style.RESET_ALL

@input_error
def edit_email(args: list[str], book: AddressBook) -> str:
    name, email = args

    contact = book.find(name)

    if not contact:
        return Fore.RED + "Contact not found." + Style.RESET_ALL

    res = contact.edit_email(email)

    if res:
        return Fore.GREEN + "Contact updated." + Style.RESET_ALL

    return Fore.RED + "Nothing changed. Email not found." + Style.RESET_ALL

@input_error
def add_address(args: list[str], book: AddressBook) -> str:
    name, *address = args

    record = book.find(name)
    if not record:
        return Fore.RED + "Contact not found." + Style.RESET_ALL

    record.add_address(" ".join(address))

    return Fore.GREEN + "Address added." + Style.RESET_ALL

@input_error
def edit_address(args: list[str], book: AddressBook) -> str:
    name, *address = args

    contact = book.find(name)

    if not contact:
        return Fore.RED + "Contact not found." + Style.RESET_ALL

    res = contact.edit_address(" ".join(address))

    if res:
        return Fore.GREEN + "Contact updated." + Style.RESET_ALL

    return Fore.RED + "Nothing changed. Address not found." + Style.RESET_ALL
