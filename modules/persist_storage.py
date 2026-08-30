import pickle

from pathlib import Path
from typing import Callable, Union

from modules.address_book import AddressBook
from modules.note_book import NoteBook

Storable = Union[AddressBook, NoteBook]

APP_DIR = Path.home() / ".personal-assistant"


class PersistStorage:
    def __init__(self, filename: str, fallback_instance: Callable[[], Storable]) -> None:
        self.filepath = APP_DIR / filename
        self.fallback_instance = fallback_instance

    def save(self, instance: Storable) -> None:
        APP_DIR.mkdir(parents=True, exist_ok=True)

        with open(self.filepath, "wb") as f:
            pickle.dump(instance, f)

    def load(self) -> Storable:
        try:
            with open(self.filepath, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError):
            return self.fallback_instance()
