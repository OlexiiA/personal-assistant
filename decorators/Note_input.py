from colorama import Fore, Style

import modules.errors as AppErrors

def note_input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return Fore.RED + "Invalid arguments. Check note ID and/or text." + Style.RESET_ALL
        except KeyError:
            return Fore.RED + "Note not found." + Style.RESET_ALL
        except IndexError:
            return Fore.RED + "Please provide the required arguments for the command." + Style.RESET_ALL
        except AppErrors.IncorrectNoteText:
            return Fore.RED + "Note text cannot be empty." + Style.RESET_ALL
        except AppErrors.IncorrectNoteId:
            return Fore.RED + "Note with this ID was not found." + Style.RESET_ALL
        except AppErrors.IncorrectTextLength:
            return Fore.RED + "Search text must be at least 3 characters long." + Style.RESET_ALL

    return inner
