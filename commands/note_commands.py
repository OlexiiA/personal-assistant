from tabulate import tabulate
from decorators.note_input import note_input_error
from modules.note_book import NoteBook
from utils.text import error_message, success_message


def make_notes_table(notes) -> str:
    rows = []

    for note_id, note in notes:
        rows.append([note_id, str(note)])

    headers = ["ID", "Note"]
    table = tabulate(rows, headers=headers, tablefmt="grid")

    return success_message(table)

@note_input_error
def add_note(args: list[str], note: NoteBook) -> str:
    text = args[0] if args else ""
    note.add_note(text)

    return success_message("Note added.")

@note_input_error
def show_all_notes(note: NoteBook) -> str:
    if not note:
        return error_message("No notes saved.")

    return make_notes_table(note.show_notes())

@note_input_error
def search_note(args: list[str], note: NoteBook) -> str:
    if not note:
        return error_message("No notes saved.")

    text = " ".join(args)
    matches = note.search_notes_by_text(text)

    if not matches:
        return error_message("No notes found.")

    return make_notes_table(matches)

@note_input_error
def edit_note(args: list[str], note: NoteBook) -> str:
    note_id, *text = args
    note.edit_note_by_id(int(note_id), " ".join(text))

    return success_message("Note updated.")

@note_input_error
def remove_note(args: list[str], note: NoteBook) -> str:
    note_id = int(args[0])
    note.remove_note_by_id(note_id)

    return success_message(f"Note {note_id} was deleted successfully.")
