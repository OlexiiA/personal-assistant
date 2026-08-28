# Personal Assistant

Personal Assistant will manage contacts and notes from the command line.
The current version manages contacts.
This is a team project for the Neoversity Python Programming course.

> Project status: in development. Version 0.1.0 has basic contact features.
> The final project features are not complete yet.

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
- [ ] Add an address and email to a contact.
- [ ] Check the email format.
- [ ] Search contacts by different fields.
- [ ] Edit and delete full contact records.
- [x] Select the number of days for the birthday list.
- [ ] Add, search, edit, and delete text notes.
- [ ] Save contacts and notes in the user's home folder.

Optional features:

- [ ] Add tags to notes.
- [ ] Search and sort notes by tags.
- [ ] Suggest the closest command when the user makes a typing mistake.

## Requirements

- Python 3.14 or newer.
- Git, if you want to clone the project.
- No external Python packages are needed now.

## Installation

Clone the public repository:

```bash
git clone https://github.com/OlexiiA/personal-assistant.git
cd personal-assistant
```

## Run the program

On macOS or Linux:

```bash
python3 main.py
```

On Windows:

```bash
python main.py
```

If you use `uv`, you can run:

```bash
uv run python main.py
```

## Commands

| Command | Example | Result |
|---|---|---|
| `hello` | `hello` | Show a welcome answer. |
| `add` | `add Alice 0123456789` | Add a contact or add a phone to a contact. |
| `change` | `change Alice 0123456789 0987654321` | Change a phone number. |
| `phone` | `phone Alice` | Show a contact and phone numbers. |
| `all` | `all` | Show all contacts. |
| `add-birthday` | `add-birthday Alice 25.12.2000` | Add a birthday. |
| `show-birthday` | `show-birthday Alice` | Show a birthday. |
| `birthdays` | `birthdays 14` | Show birthdays for the selected number of days. |
| `exit` | `exit` | Save data and close the program. |
| `close` | `close` | Save data and close the program. |

## Input rules

- Use one word for a contact name.
- A phone number must have exactly 10 digits.
- Use `DD.MM.YYYY` for a birthday.
- Use a command from the table above.

The program shows an error message for wrong input and continues to work.

## Data storage

The current version saves contacts in `addressbook.pkl`.
The file is created in the folder where you run the program.
Data is saved when you use `exit`, `close`, `Ctrl+C`, or an end-of-file signal.

The final version must save both contacts and notes in the user's home folder.
