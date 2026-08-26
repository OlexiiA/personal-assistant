from modules.Errors import IncorrectNoteId
from modules.Fields import Note

class NoteBook:
    def __init__(self):
        self.notes = {}
        self.next_id = 1

    def add_note(self, text):
        note = Note(text)
        self.notes[self.next_id] = note
        self.next_id += 1
        return note

    def show_notes(self):
        return list(self.notes.values())

    def search_notes_by_text(self, text):
        if len(text) < 3:
            raise ValueError("Search text must be at least 3 characters long.")
        return [note for note in self.notes.values() if text.lower() in note.text.lower()]

    def edit_note_by_id(self, note_id, new_text):
        if note_id in self.notes:
            self.notes[note_id].text = new_text
        else:
            raise IncorrectNoteId(f"Note with ID {note_id} not found.")

    def remove_note_by_id(self, note_id):
        if note_id in self.notes:
            del self.notes[note_id]
        else:
            raise IncorrectNoteId(f"Note with ID {note_id} not found.")
