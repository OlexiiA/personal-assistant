import modules.Errors as AppErrors

def note_input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me note please"
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command."
        except AppErrors.IncorrectNoteText:
            return "Length for note has to be more then 0."
        except AppErrors.IncorrectNoteId:
            return "Note with such ID is not found."
        except AppErrors.IncorrectTextLength:
            return "Minimum search length for notes is 3 characters."

    return inner