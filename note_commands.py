from decorators.Note_input import note_input_error
from modules.NoteBook import NoteBook
import modules.Errors as AppErrors

@note_input_error
def add_note(args: list[str], note: NoteBook) -> str:
    text = args[0] if args else ""
    note.add_note(text)
    return "Note added."

@note_input_error
def show_all_notes(note: NoteBook) -> str:
    if not note:
        return "No notes saved."

    return "\n".join(f"{id}: {text}" for id, text in note.show_notes())

@note_input_error
def search_note(args: list[str], note: NoteBook) -> str:
    if not note.notes:
        return "No notes saved."

    text = " ".join(args)
    matches = note.search_notes_by_text(text)

    if not matches:
        return "No notes found."

    return "\n".join(f"{note_id}: {note}" for note_id, note in matches)

@note_input_error
def edit_note(args: list[str], note: NoteBook) -> str:
    note_id, *text = args
    updated_note = note.edit_note_by_id(int(note_id), " ".join(text))

    return "Note is updated." if updated_note else "Nothing changed. Note is not found."

@note_input_error
def remove_note(args: list[str], note: NoteBook) -> str:
    note_id = args
    try:
        note.remove_note_by_id(int(note_id))
        return f"Note {note_id} was deleted successfullly."
    except:
        AppErrors.IncorrectNoteId()