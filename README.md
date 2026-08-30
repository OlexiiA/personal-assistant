# Personal Assistant

Personal Assistant will manage contacts and notes from the command line.
The current version manages contacts.
This is a team project for the Neoversity Python Programming course.

> Project status: in development. Version 0.1.0 has basic contact features.

## What the program can do

Main features:

- [x] Add a contact name and phone number.
- [x] Add more phone numbers to a contact.
- [x] Change a phone number.
- [x] Show one contact or all contacts.
- [x] Add and show a birthday.
- [x] Show birthdays for the next 7 days.
- [x] Check that a phone number has 10 digits.
- [x] Check the birthday format.
- [x] Show a clear message for wrong input.
- [x] Save contacts and load them after restart.
- [x] Show contacts, birthdays, and notes in colored tables.
- [x] Add an address and email to a contact.
- [x] Check the email format.
- [x] Search contacts by different fields.
- [x] Edit and delete full contact records.
- [x] Select the number of days for the birthday list.
- [x] Add, search, edit, and delete text notes.
- [x] Save contacts and notes in the user's home folder.
- [x] Show the command menu once at startup.

Optional features:

- [ ] Add tags to notes.
- [ ] Search and sort notes by tags.
- [x] Suggest the closest command when the user makes a typing mistake.

## Requirements

- Python 3.14 or newer.
- Git, if you want to clone the project.
- Dependencies are installed from `pyproject.toml`.

## Installation

Clone the public repository:

```bash
git clone https://github.com/OlexiiA/personal-assistant.git
cd personal-assistant
```

Install dependencies with [`uv`](https://docs.astral.sh/uv/):

```bash
uv sync
```

Without `uv`, install with `pip`:

```bash
pip install colorama "pydantic[email]" tabulate
```

## Run the program

With `uv`:

```bash
uv run main.py
```

Without `uv`, on macOS or Linux:

```bash
python3 main.py
```

Without `uv`, on Windows:

```bash
python main.py
```

## Commands

| Command           | Example                                        | Result |
|-------------------|------------------------------------------------|---|
| `hello`           | `hello`                                        | Show a welcome answer. |
| `add`             | `add Alice 0123456789`                         | Add a contact or add a phone to a contact. |
| `change`          | `change Alice 0123456789 0987654321`           | Change a phone number. |
| `edit-name`       | `edit-name Alice Alicia`                       | Change a contact name. |
| `remove-contact`  | `remove-contact Alice`                         | Delete a full contact record. |
| `phone`           | `phone Alice`                                  | Show a contact and phone numbers. |
| `all`             | `all`                                          | Show all contacts. |
| `add-birthday`    | `add-birthday Alice 25.12.2000`                | Add a birthday. |
| `show-birthday`   | `show-birthday Alice`                          | Show a birthday. |
| `birthdays`       | `birthdays` or `birthdays 14`                  | Show birthdays for 7 days or for the selected number of days. |
| `search-contacts` | `search-contacts kyiv`                         | Find contacts by name, phone, email, or address. |
| `add-email`       | `add-email Alice alice@example.com`            | Add an email to a contact. |
| `edit-email`      | `edit-email Alice new@example.com`             | Change a contact email. |
| `add-address`     | `add-address Alice Kyiv Main Street 1`         | Add an address to a contact. |
| `edit-address`    | `edit-address Alice Lviv Shevchenka Street 10` | Change a contact address. |
| `add-note`        | `add-note Buy-milk`                            | Add a new note. |
| `all-notes`       | `all-notes`                                    | Show all notes. |
| `search-note`     | `search-note milk`                             | Search notes by text. |
| `edit-note`       | `edit-note 1 Buy milk today`                   | Change a note by its ID. |
| `remove-note`     | `remove-note 1`                                | Delete a note by its ID. |
| `help`            | `help`                                         | Show all commands with examples. |
| `exit`            | `exit`                                         | Save data and close the program. |
| `close`           | `close`                                        | Save data and close the program. |

## Input rules

- Use one word for a contact name.
- A phone number must have exactly 10 digits and contain digits only.
- An email must be a valid email address.
- Use `DD.MM.YYYY` for a birthday.
- The number of days for `birthdays` must be a positive integer.
- A note's text cannot be empty.
- Search text for `search-note` must be at least 3 characters long.
- A note ID for `edit-note` and `remove-note` must match an existing note.
- Use a command from the table above.

The program shows an error message for wrong input and continues to work.

## Data storage

Contacts are saved in `addressbook.pkl` and notes in `notebook.pkl`.
Both files are created in the `.personal-assistant` folder in your home directory.
Data is saved when you use `exit`, `close`, `Ctrl+C`, or an end-of-file signal.
