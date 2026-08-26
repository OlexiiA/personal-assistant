class IncorrectPhoneNumber(Exception):
    pass

class IncorrectPhoneLength(Exception):
    pass

class IncorrectBirthday(Exception):
    pass

class IncorrectNoteId(Exception):
    def __init__(self, message="Note with ID not found"):
        self.message = message
        super().__init__(self.message)