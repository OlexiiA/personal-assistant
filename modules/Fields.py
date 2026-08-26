from datetime import datetime

import modules.Errors as AppErrors


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Birthday(Field):
    def __init__(self, value):
        try:
            parsed = datetime.strptime(value, "%d.%m.%Y").date()
        except (ValueError, TypeError):
            raise AppErrors.IncorrectBirthday()

        super().__init__(parsed)

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

        if not value.isdigit():
            raise AppErrors.IncorrectPhoneNumber()
        elif len(value) != 10:
            raise AppErrors.IncorrectPhoneLength()

class Note:
    def __init__(self, text):
        self.text = text

        if not text:
            raise AppErrors.IncorrectNoteText

    def __str__(self):
        return self.text