from colorama import Fore, Style
from tabulate import tabulate

from decorators.Note_input import note_input_error
from modules.NoteBook import NoteBook


def make_notes_table(notes) -> str:
    rows = []

    for note_id, note in notes:
        rows.append([note_id, str(note)])

    headers = ["ID", "Note"]
    table = tabulate(rows, headers=headers, tablefmt="grid")

    return Fore.GREEN + table + Style.RESET_ALL

@note_input_error
def add_note(args: list[str], note: NoteBook) -> str:
    text = args[0] if args else ""
    note.add_note(text)
    return Fore.GREEN + "Note added." + Style.RESET_ALL

@note_input_error
def show_all_notes(note: NoteBook) -> str:
    if not note.notes:
        return Fore.RED + "No notes saved." + Style.RESET_ALL

    return make_notes_table(note.show_notes())

@note_input_error
def search_note(args: list[str], note: NoteBook) -> str:
    if not note.notes:
        return Fore.RED + "No notes saved." + Style.RESET_ALL

    text = " ".join(args)
    matches = note.search_notes_by_text(text)

    if not matches:
        return Fore.RED + "No notes found." + Style.RESET_ALL

    return make_notes_table(matches)

@note_input_error
def edit_note(args: list[str], note: NoteBook) -> str:
    note_id, *text = args
    note.edit_note_by_id(int(note_id), " ".join(text))

    return Fore.GREEN + "Note updated." + Style.RESET_ALL

@note_input_error
def remove_note(args: list[str], note: NoteBook) -> str:
    note_id = int(args[0])
    note.remove_note_by_id(note_id)
    return Fore.GREEN + f"Note {note_id} was deleted successfully." + Style.RESET_ALL
