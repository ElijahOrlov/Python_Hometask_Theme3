def sum_distance(start: int, end: int) -> int:
    """
    Суммирует все числа от значения start до величины end включительно
    :param start: начальное значение
    :param end: конечное значение
    :return: результирующая сумма
    """
    if start > end:
        start, end = end, start
    result_sum = 0
    for num in range(start, end + 1):
        result_sum += num
    return result_sum


print(sum_distance(1, 100))
