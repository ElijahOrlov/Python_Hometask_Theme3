def trim_and_repeat(text: str, offset: int = 0, repetitions: int = 1) -> str:
    """
    Обрабатывает полученную стороку:
        - обрезает стоку слева на указанное количество offset
        - повторяет количество раз указанное в reprtitions
    :param text: текстовая строка для обработки
    :param offset: число символов, на которое нужно обрезать строку слева
    :param repetitions: сколько раз нужно повторить строку перед возвратом
    :return: обработанная строка
    """
    result_text = text
    if 0 < offset < len(text):
        result_text = result_text[offset:]
    if repetitions > 1:
        result_text *= repetitions
    return result_text


print(trim_and_repeat("hello goodbye!", 6, 3))
