import modules.errors as AppErrors
from utils.text import error_message


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return error_message("Give me name and value please.")
        except KeyError:
            return error_message("Contact not found.")
        except IndexError:
            return error_message("Enter the argument for the command.")
        except AppErrors.IncorrectPhoneLength:
            return error_message("Incorrect phone length. Should be 10 digits.")
        except AppErrors.IncorrectPhoneNumber:
            return error_message("Incorrect phone type. Should be digits only.")
        except AppErrors.IncorrectBirthday:
            return error_message("Incorrect birthday format. Should be dd.mm.yyyy.")
        except AppErrors.IncorrectEmail:
            return error_message("Incorrect email format. Please enter a valid email address.")

    return inner
