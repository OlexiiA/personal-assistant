import perso.modules.errors as AppErrors
from perso.utils.text import error_message


def note_input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return error_message("Invalid arguments. Check note ID and/or text.")
        except KeyError:
            return error_message("Note not found.")
        except IndexError:
            return error_message("Please provide the required arguments for the command.")
        except AppErrors.IncorrectNoteText:
            return error_message("Note text cannot be empty.")
        except AppErrors.IncorrectNoteId:
            return error_message("Note with this ID was not found.")
        except AppErrors.IncorrectTextLength:
            return error_message("Search text must be at least 3 characters long.")

    return inner
