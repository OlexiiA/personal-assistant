from colorama import Fore, Style
from tabulate import tabulate

from perso.decorators.input import input_error
from perso.modules.address_book import AddressBook
from perso.modules.record import Record
from perso.utils.text import error_message, success_message


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
    message = success_message("Contact updated.")

    if record is None:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return success_message("Contact added.")

    record.add_phone(phone)

    return message


@input_error
def change_contact(args: list[str], book: AddressBook) -> str:
    name, phone, new_phone = args

    contact = book.find(name)

    if not contact:
        return error_message("Contact not found.")

    res = contact.edit_phone(phone, new_phone)

    if res:
        return success_message("Contact updated.")

    return error_message("Nothing changed. Phone not found.")


@input_error
def edit_name(args: list[str], book: AddressBook) -> str:
    old_name, new_name = args

    contact = book.find(old_name)
    if not contact:
        return error_message("Contact not found.")

    if book.find(new_name):
        return error_message("Contact with this name already exists.")

    book.delete(old_name)
    contact.edit_name(new_name)
    book.add_record(contact)

    return success_message("Contact name updated.")


@input_error
def remove_contact(args: list[str], book: AddressBook) -> str:
    name = args[0]

    contact = book.find(name)
    if not contact:
        return error_message("Contact not found.")

    book.delete(name)

    return success_message("Contact deleted.")


@input_error
def show_phone(args: list[str], book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)

    if not record:
        return error_message("Contact not found.")

    return make_contacts_table([record])


@input_error
def show_all(book: AddressBook) -> str:
    if not book:
        return error_message("No contacts saved.")

    records = list(book.values())

    return make_contacts_table(records)

@input_error
def add_birthday(args: list[str], book: AddressBook) -> str:
    name, birthday = args

    record = book.find(name)
    if not record:
        return error_message("Contact not found.")

    record.add_birthday(birthday)

    return success_message("Birthday added.")


@input_error
def show_birthday(args: list[str], book: AddressBook) -> str:
    name = args[0]

    record = book.find(name)
    if not record:
        return error_message("Contact not found.")

    if not record.birthday:
        return error_message("Birthday not set.")

    return success_message(str(record.birthday))


@input_error
def birthdays(args: list[str], book: AddressBook) -> str:
    days = 7

    if args:
        if not args[0].isdigit():
            return error_message("Number of days must be a positive integer.")
        days = int(args[0])

    if days <= 0:
        return error_message("Number of days must be greater than zero.")

    upcoming = book.get_upcoming_birthdays(days)

    if not upcoming:
        return error_message(f"No birthdays in the next {days} days.")

    rows = []
    for b in upcoming:
        rows.append([b["name"], b["congratulation_date"]])

    headers = ["Name", "Congratulation date"]
    table = tabulate(rows, headers=headers, tablefmt="grid")

    return Fore.MAGENTA + table + Style.RESET_ALL

@input_error
def search_contacts(args: list[str], book: AddressBook) -> str:
    text = " ".join(args)

    if not text:
        return error_message("Enter text to search for.")

    matches = book.search_records(text)

    if not matches:
        return error_message("No contacts found.")

    return make_contacts_table(matches)

@input_error
def add_email(args: list[str], book: AddressBook) -> str:
    name, email = args

    record = book.find(name)
    if not record:
        return error_message("Contact not found.")

    record.add_email(email)

    return success_message("Email added.")


@input_error
def edit_email(args: list[str], book: AddressBook) -> str:
    name, email = args

    contact = book.find(name)

    if not contact:
        return error_message("Contact not found.")

    res = contact.edit_email(email)

    if res:
        return success_message("Contact updated.")

    return error_message("Nothing changed. Email not found.")


@input_error
def add_address(args: list[str], book: AddressBook) -> str:
    name, *address = args

    record = book.find(name)
    if not record:
        return error_message("Contact not found.")

    record.add_address(" ".join(address))

    return success_message("Address added.")


@input_error
def edit_address(args: list[str], book: AddressBook) -> str:
    name, *address = args

    contact = book.find(name)

    if not contact:
        return error_message("Contact not found.")

    res = contact.edit_address(" ".join(address))

    if res:
        return success_message("Contact updated.")

    return error_message("Nothing changed. Address not found.")
