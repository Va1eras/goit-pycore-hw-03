import random


def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list[int]:
    """
    Генерує відсортований список унікальних випадкових чисел для лотерейного білета.

    :param min_num: Мінімальне можливе число (>= 1).
    :param max_num: Максимальне можливе число (<= 1000).
    :param quantity: Кількість чисел для вибору (між min_num і max_num).
    :return: Відсортований список унікальних чисел або пустий список, якщо параметри невалідні.
    """
    # Перевірка типу та меж вхідних параметрів
    if (
        not (isinstance(min_num, int) and isinstance(max_num, int) and isinstance(quantity, int))
        or min_num < 1
        or max_num > 1000
        or min_num > max_num
        or quantity < 1
        or quantity > (max_num - min_num + 1)
    ):
        return []

    # random.sample одразу повертає список унікальних елементів без повторень
    numbers = random.sample(range(min_num, max_num + 1), quantity)
    return sorted(numbers)


# Приклад перевірки:
if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)
