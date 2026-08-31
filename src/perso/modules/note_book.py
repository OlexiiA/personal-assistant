from collections import UserDict

import perso.modules.errors as AppErrors
from perso.modules.fields import Note


class NoteBook(UserDict):
    def __init__(self):
        super().__init__()
        self.next_id = 1

    def add_note(self, text):
        note = Note(text)
        note.id = self.next_id
        self.data[self.next_id] = note
        self.next_id += 1
        return note

    def show_notes(self):
        return self.data.items()

    def search_notes_by_text(self, text):
        if len(text) < 3:
            raise AppErrors.IncorrectTextLength()

        search_text = text.lower()
        return [
            (note_id, note)
            for note_id, note in self.data.items()
            if search_text in note.value.lower()
        ]

    def edit_note_by_id(self, note_id, new_text):
        if note_id not in self.data:
            raise AppErrors.IncorrectNoteId()

        updated_note = Note(new_text)
        updated_note.id = note_id
        self.data[note_id] = updated_note
        return updated_note

    def remove_note_by_id(self, note_id):
        if note_id not in self.data:
            raise AppErrors.IncorrectNoteId()

        del self.data[note_id]
        return self.data
