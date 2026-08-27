import modules.Errors as AppErrors
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
        return self.notes.items()

    def search_notes_by_text(self, text):
        if len(text) < 3:
            raise AppErrors.IncorrectTextLength()

        search_text = text.lower()
        return [
            (note_id, note)
            for note_id, note in self.notes.items()
            if search_text in note.value.lower()
        ]
        
    def edit_note_by_id(self, note_id, new_text):
        if note_id not in self.notes:
            raise AppErrors.IncorrectNoteId()

        updated_note = Note(new_text)
        self.notes[note_id] = updated_note
        return updated_note

    def remove_note_by_id(self, note_id):
        if note_id not in self.notes:
            raise AppErrors.IncorrectNoteId()

        del self.notes[note_id]
        return self.notes
