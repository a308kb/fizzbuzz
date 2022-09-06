"""
CLI-утилита, которая при запуске будет запрашивать число у пользователя и давать ответ - Fizz, Buzz, FizzBuzz.
Запуск приложения выводит приветствие и спрашивает число.
На каждый ввод числа (ввод чисел происходит, пока пользователь не завершит процесс) утилита выводит ответ:
При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»,
а вместо чисел, кратных пяти — слово «Buzz».
Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz»
"""
from typing import Union


def str2num(in_str: str, ndigit: int = 0) -> Union[int, float]:
    """Преобразует строку в число

    :param in_str: Строка для преобразования
    :param ndigit: Количество цифр для округления
    :return: nan - если не удалось преобразовать,
            целое - если ndidgit == 0,
            float - иначе
    """
    string = in_str.strip()
    try:
        num = float(in_str)
        num = round(num,ndigit)
        return num
    except ValueError:
        return float('nan')


def fizzbuzz(num: int) -> str:
    """Преобразует число в строку содержащую
            "Fizz" если число кратно 3,
            "Buzz" если число кратно 5,
            "FizzBuzz" если число кратно и 3 и 5,
            иначе само число

    :param int num: целое число, которое проверяется на кратнось 3 и 5
    :return str: Результат преобразования
    """
    retstr = ""
    for k, v in ((3, "Fizz"), (5, 'Buzz')):  # Проверка на кратность
        if num % k == 0:
            retstr += v
    if retstr == "":  # Не кратно заданным числам
        retstr = str(num)
    return retstr


if __name__ == '__main__':
    print("Вас приветствует супер-программа FizzBuzz")
    while 1:
        inpstr = input("Введите целое число или пустую строку для выхода: ")
        if not inpstr:  # Если пустая строка - на выход
            break
        num = str2num(inpstr)
        if num == num:
            print(fizzbuzz(num))
        else:
            print("Это не число, попробуйте еще раз")
