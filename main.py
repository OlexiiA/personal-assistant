from collections import UserDict
from datetime import datetime, timedelta
import pickle


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError(
                "Phone number must contain exactly 10 digits"
            )

        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            birthday = datetime.strptime(
                value,
                "%d.%m.%Y"
            ).date()

            super().__init__(birthday)

        except ValueError:
            raise ValueError(
                "Invalid date format. Use DD.MM.YYYY"
            )

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                self.phones.remove(item)
                return

    def edit_phone(self, old_phone, new_phone):
        old = self.find_phone(old_phone)

        if old is None:
            raise ValueError("Phone number not found.")

        new = Phone(new_phone)
        old.value = new.value

    def find_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                return item

        return None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones = "; ".join(
            phone.value for phone in self.phones
        )

        birthday = (
            str(self.birthday)
            if self.birthday
            else "Not set"
        )

        return (
            f"Contact name: {self.name.value}, "
            f"phones: {phones}, "
            f"birthday: {birthday}"
        )


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name, None)

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.today().date()

        for record in self.data.values():

            if record.birthday is None:
                continue

            birthday = record.birthday.value

            try:
                birthday_this_year = birthday.replace(
                    year=today.year
                )

            except ValueError:
                birthday_this_year = birthday.replace(
                    year=today.year,
                    day=28
                )

            if birthday_this_year < today:
                try:
                    birthday_this_year = birthday.replace(
                        year=today.year + 1
                    )

                except ValueError:
                    birthday_this_year = birthday.replace(
                        year=today.year + 1,
                        day=28
                    )

            days_until_birthday = (
                birthday_this_year - today
            ).days

            if 0 <= days_until_birthday <= 7:
                congratulation_date = birthday_this_year

                day_of_week = congratulation_date.weekday()

                if day_of_week == 5:
                    congratulation_date += timedelta(days=2)

                elif day_of_week == 6:
                    congratulation_date += timedelta(days=1)

                upcoming_birthdays.append(
                    {
                        "name": record.name.value,
                        "congratulation_date":
                            congratulation_date.strftime(
                                "%d.%m.%Y"
                            )
                    }
                )

        return upcoming_birthdays


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(book, file)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)

    except FileNotFoundError:
        return AddressBook()


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ValueError as error:
            return str(error)

        except KeyError:
            return "Contact not found."

        except IndexError:
            return "Enter the correct arguments."

    return inner


def parse_input(user_input):
    parts = user_input.split()

    if len(parts) == 0:
        return "", []

    command = parts[0].lower()
    args = parts[1:]

    return command, args


@input_error
def add_contact(args, book):
    if len(args) < 2:
        raise ValueError("Enter name and phone number.")

    name = args[0]
    phone = args[1]

    new_phone = Phone(phone)

    record = book.find(name)

    if record is None:
        record = Record(name)
        record.phones.append(new_phone)
        book.add_record(record)

        return "Contact added."

    record.phones.append(new_phone)

    return "Contact updated."


@input_error
def change_contact(args, book):
    if len(args) < 3:
        raise ValueError(
            "Enter name, old phone and new phone."
        )

    name = args[0]
    old_phone = args[1]
    new_phone = args[2]

    record = book.find(name)

    if record is None:
        raise KeyError

    record.edit_phone(
        old_phone,
        new_phone
    )

    return "Contact updated."


@input_error
def show_phone(args, book):
    if len(args) < 1:
        raise ValueError("Enter contact name.")

    name = args[0]

    record = book.find(name)

    if record is None:
        raise KeyError

    if len(record.phones) == 0:
        return "No phone numbers."

    return "; ".join(
        phone.value
        for phone in record.phones
    )


@input_error
def show_all(book):
    if len(book.data) == 0:
        return "No contacts saved."

    result = []

    for record in book.data.values():
        result.append(str(record))

    return "\n".join(result)


@input_error
def add_birthday(args, book):
    if len(args) < 2:
        raise ValueError(
            "Enter name and birthday in DD.MM.YYYY format."
        )

    name = args[0]
    birthday = args[1]

    record = book.find(name)

    if record is None:
        raise KeyError

    record.add_birthday(birthday)

    return "Birthday added."


@input_error
def show_birthday(args, book):
    if len(args) < 1:
        raise ValueError("Enter contact name.")

    name = args[0]

    record = book.find(name)

    if record is None:
        raise KeyError

    if record.birthday is None:
        return "Birthday is not set."

    return str(record.birthday)


@input_error
def birthdays(args, book):
    upcoming = book.get_upcoming_birthdays()

    if len(upcoming) == 0:
        return "No upcoming birthdays."

    result = []

    for item in upcoming:
        result.append(
            f"{item['name']}: "
            f"{item['congratulation_date']}"
        )

    return "\n".join(result)


def main():
    book = load_data()

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(
                add_contact(
                    args,
                    book
                )
            )

        elif command == "change":
            print(
                change_contact(
                    args,
                    book
                )
            )

        elif command == "phone":
            print(
                show_phone(
                    args,
                    book
                )
            )

        elif command == "all":
            print(
                show_all(
                    book
                )
            )

        elif command == "add-birthday":
            print(
                add_birthday(
                    args,
                    book
                )
            )

        elif command == "show-birthday":
            print(
                show_birthday(
                    args,
                    book
                )
            )

        elif command == "birthdays":
            print(
                birthdays(
                    args,
                    book
                )
            )

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()