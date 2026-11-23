from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    """
    Визначає колег, яких потрібно привітати з днем народження протягом наступних 7 днів
    (включаючи поточний день), з переносом привітання з вихідних на понеділок.

    :param users: Список словників із ключами 'name' та 'birthday' ('РРРР.ММ.ДД').
    :return: Список словників із ключами 'name' та 'congratulation_date' ('РРРР.ММ.ДД').
    """
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Обробка випадку народження 29 лютого у невисокосний рік
        try:
            birthday_this_year = birthday.replace(year=today.year)
        except ValueError:
            birthday_this_year = birthday.replace(year=today.year, day=28)

        # Якщо день народження цього року вже минув, переносимо розгляд на наступний рік
        if birthday_this_year < today:
            try:
                birthday_this_year = birthday.replace(year=today.year + 1)
            except ValueError:
                birthday_this_year = birthday.replace(year=today.year + 1, day=28)

        days_until_birthday = (birthday_this_year - today).days

        # Перевіряємо, чи входить дата у діапазон 0..7 днів вперед
        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year

            # Перевірка на вихідні: 5 — субота, 6 — неділя
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            })

    return upcoming_birthdays


# Приклад перевірки:
if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
    ]
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)
