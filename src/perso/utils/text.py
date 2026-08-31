from colorama import Fore, Style


def error_message(text: str) -> str:
    return Fore.RED + text + Style.RESET_ALL

def success_message(text: str) -> str:
    return Fore.GREEN + text + Style.RESET_ALL

def warning_message(text: str) -> str:
    return Fore.YELLOW + text + Style.RESET_ALL
