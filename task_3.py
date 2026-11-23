import re


def normalize_phone(phone_number: str) -> str:
    """
    Нормалізує телефонний номер до стандартного міжнародного формату (+380...).

    :param phone_number: Рядок із телефонним номером у довільному форматі.
    :return: Очищений рядок номера телефону, що починається з '+38'.
    """
    # Залишаємо лише цифри та символ '+'
    cleaned_number = re.sub(r"[^\d+]", "", phone_number.strip())

    # Якщо номер уже починається з '+', повертаємо його як є
    if cleaned_number.startswith("+"):
        return cleaned_number

    # Якщо номер починається з '380', додаємо лише '+'
    if cleaned_number.startswith("380"):
        return "+" + cleaned_number

    # В усіх інших випадках (наприклад, '050...') додаємо '+38'
    return "+38" + cleaned_number


# Приклад перевірки:
if __name__ == "__main__":
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]
    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
