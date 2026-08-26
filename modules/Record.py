from modules.Fields import Name, Phone, Birthday


class Record:
    def __init__(self, name):
        self.name: Name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday | None = None

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def edit_phone(self, phone: str, new_phone: str):
        for i, p in enumerate(self.phones):
            if p.value == phone:
                self.phones[i] = Phone(new_phone)
                return True
        
        return False

    def remove_phone(self, phone: str):
        self.phones = [p for p in self.phones if p.value != phone]

    def find_phone(self, phone: str) -> Phone | None:
        for p in self.phones:
            if p.value == phone:
                return p

        return None

    def add_birthday(self, date: str):
        self.birthday = Birthday(date)

    def __str__(self):
        birthday_part = f", birthday: {self.birthday}" if self.birthday else ""

        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}{birthday_part}"