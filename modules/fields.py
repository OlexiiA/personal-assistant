from datetime import datetime
import modules.errors as AppErrors
from pydantic import BaseModel, EmailStr, ValidationError


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

class _EmailModel(BaseModel):
    value: EmailStr

class Email(Field):
    def __init__(self, value):
        if not isinstance(value, str):
            raise AppErrors.IncorrectEmail()

        try:
            parsed = _EmailModel(value=value)
        except ValidationError:
            raise AppErrors.IncorrectEmail()

        super().__init__(parsed.value)

    def __str__(self):
        return str(self.value)

class Address(Field):
    pass

class Note(Field):
    def __init__(self, value):
        super().__init__(value)

        if not value:
            raise AppErrors.IncorrectNoteText()
