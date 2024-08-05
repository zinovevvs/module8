def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for num in numbers:
        try:
            if isinstance(num, (int, float)): # Проверяю, является ли элемент числом
                result += num
            else:
                raise TypeError # Если элемент не число, генерирую исключение
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {num}')
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple)):
            raise TypeError
        result, incorrect_data = personal_sum(numbers)
        total_numbers = len(numbers) - incorrect_data

        return result / total_numbers if total_numbers > 0 else 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average([23, '45', 19, 10])}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average([290, 345])}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать


