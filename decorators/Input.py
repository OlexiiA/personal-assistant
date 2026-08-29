from colorama import Fore, Style

import modules.Errors as AppErrors


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return Fore.RED + "Give me name and value please." + Style.RESET_ALL
        except KeyError:
            return Fore.RED + "Contact not found." + Style.RESET_ALL
        except IndexError:
            return Fore.RED + "Enter the argument for the command." + Style.RESET_ALL
        except AppErrors.IncorrectPhoneLength:
            return Fore.RED + "Incorrect phone length. Should be 10 digits." + Style.RESET_ALL
        except AppErrors.IncorrectPhoneNumber:
            return Fore.RED + "Incorrect phone type. Should be digits only." + Style.RESET_ALL
        except AppErrors.IncorrectBirthday:
            return Fore.RED + "Incorrect birthday format. Should be dd.mm.yyyy." + Style.RESET_ALL
        except AppErrors.IncorrectEmail:
            return Fore.RED + "Incorrect email format. Please enter a valid email address." + Style.RESET_ALL

    return inner
