import modules.Errors as AppErrors

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command."
        except AppErrors.IncorrectPhoneLength:
            return "Incorrect phone length. Should be 10 digits."
        except AppErrors.IncorrectPhoneNumber:
            return "Incorrect phone type. Should be digits only."
        except AppErrors.IncorrectBirthday:
            return "Incorrect birthday format. Should be dd.mm.yyyy."
        except AppErrors.IncorrectNoteText:
            return "Length for note has to be more then 0."
        except AppErrors.IncorrectNoteId:
            return "Note with such ID is not found."
        except AppErrors.IncorrectTextLength:
            return "Minimum search length for notes is 3 characters."

    return inner