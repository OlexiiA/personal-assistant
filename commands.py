from decorators.Input import input_error
from modules.AddressBook import AddressBook
from modules.Record import Record


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

    return "Contact updated." if res else "Nothing changed. Phone not found."


@input_error
def show_phone(args: list[str], book: AddressBook) -> Record | str:
    name = args[0]
    record = book.find(name)

    return record if record else "Contact not found."


@input_error
def show_all(book: AddressBook) -> str:
    if not book:
        return "No contacts saved."
    result = []
    for name, record in book.items():
        phones = [phone.value for phone in record.phones]
        result.append(f"{name}: {', '.join(phones)}, Birthday: {record.birthday}, Email: {record.email}, Address: {record.address}")
    return "\n".join(result)

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

@input_error
def add_email(args: list[str], book: AddressBook) -> str:
    name, email = args

    record = book.find(name)
    if not record:
        return "Contact not found."

    record.add_email(email)

    return "Email added."

@input_error
def edit_email(args: list[str], book: AddressBook) -> str:
    name, email = args

    contact = book.find(name)

    if not contact:
        return "Contact not found."

    try:
        res = contact.edit_email(email)
    except:
        return "Enter the email to update."

    return "Contact updated." if res else "Nothing changed. Email not found."

@input_error
def add_address(args: list[str], book: AddressBook) -> str:
    name, *address = args

    record = book.find(name)
    if not record:
        return "Contact not found."

    record.add_address(address)

    return "Address added."

@input_error
def edit_address(args: list[str], book: AddressBook) -> str:
    name, *address = args

    contact = book.find(name)

    if not contact:
        return "Contact not found."

    res = contact.edit_address(address)

    return "Contact updated." if res else "Nothing changed. Address not found."
