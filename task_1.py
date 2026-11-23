from datetime import datetime


def get_days_from_today(date: str) -> int | None:
    """
    Розраховує кількість днів між заданою датою та поточною датою.

    :param date: Рядок дати у форматі 'РРРР-ММ-ДД'.
    :return: Ціле число днів (від'ємне, якщо дата в майбутньому) або None у разі помилки формату.
    """
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        current_date = datetime.today().date()
        delta = current_date - target_date
        return delta.days
    except ValueError:
        print(f"Помилка: Неправильний формат дати '{date}'. Очікується 'РРРР-ММ-ДД'.")
        return None


# Приклад перевірки:
if __name__ == "__main__":
    print(get_days_from_today("2021-10-09"))
    print(get_days_from_today("невірна-дата"))
