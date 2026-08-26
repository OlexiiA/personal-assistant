from decorators.Input import input_error
from modules.AddressBook import AddressBook
from modules.Record import Record
from modules.NoteBook import NoteBook, Note

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

@input_error
def add_note(args: list[str], note: NoteBook) -> str:
    text = args[0] if args else ""
    note.add_note(text)
    return "Note added."

@input_error
def show_all_notes(note: NoteBook) -> str:
    if not note:
        return "No notes saved."

    return "\n".join(f"{id}: {text}" for id, text in note.show_notes())

@input_error
def search_note(args: list[str], note: NoteBook) -> str:
    if not note.notes:
        return "No notes saved."

    text = " ".join(args)
    matches = note.search_notes_by_text(text)

    if not matches:
        return "No notes found."

    return "\n".join(f"{note_id}: {note}" for note_id, note in matches)