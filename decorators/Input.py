import modules.Errors as AppErrors


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and value please."
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
        except AppErrors.IncorrectEmail:
            return "Incorrect email format. Please enter a valid email address."

    return inner