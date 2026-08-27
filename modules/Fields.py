import re
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


class Email(Field):
    EMAIL_PATTERN = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    def __init__(self, value):
        if not isinstance(value, str):
            raise AppErrors.IncorrectEmail()

        if not re.fullmatch(self.EMAIL_PATTERN, value):
            raise AppErrors.IncorrectEmail()

        super().__init__(value)

    def __str__(self):
        return str(self.value)