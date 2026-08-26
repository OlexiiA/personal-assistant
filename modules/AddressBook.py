from collections import UserDict
from datetime import datetime, timedelta

from modules.Record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        return self.data.get(name)

    def delete(self, name: str):
        del self.data[name]

    def get_upcoming_birthdays(self) -> list[dict[str, str]]:
        today = datetime.today().date()
        upcoming_birthdays = []

        for record in self.data.values():
            if not record.birthday:
                continue

            try:
                birthday_this_year = record.birthday.value.replace(year=today.year)
            except ValueError:
                birthday_this_year = record.birthday.value.replace(
                    year=today.year,
                    day=28,
                )

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            if (birthday_this_year - today).days <= 7:
                congratulation_date = birthday_this_year

                if congratulation_date.weekday() in [5, 6]:
                    congratulation_date += timedelta(days=7 - congratulation_date.weekday())

                upcoming_birthdays.append({
                    "name": record.name.value,
                    "congratulation_date": congratulation_date.strftime("%d.%m.%Y"),
                })

        return upcoming_birthdays

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())
