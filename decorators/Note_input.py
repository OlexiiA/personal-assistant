import modules.Errors as AppErrors

def note_input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Invalid arguments. Check note ID and/or text."
        except KeyError:
            return "Note not found."
        except IndexError:
            return "Please provide the required arguments for the command."
        except AppErrors.IncorrectNoteText:
            return "Note text cannot be empty."
        except AppErrors.IncorrectNoteId:
            return "Note with this ID was not found."
        except AppErrors.IncorrectTextLength:
            return "Search text must be at least 3 characters long."

    return inner