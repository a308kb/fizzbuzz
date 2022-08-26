"""
CLI-утилита, которая при запуске будет запрашивать число у пользователя и давать ответ - Fizz, Buzz, FizzBuzz.
Запуск приложения выводит приветствие и спрашивает число.
На каждый ввод числа (ввод чисел происходит, пока пользователь не завершит процесс) утилита выводит ответ:
При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»,
а вместо чисел, кратных пяти — слово «Buzz».
Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz»
"""

def fizbuz(num):
    """
    :param int num: целое число, которое проверяется на кратнось 3 и 5
    :return:
        число кратно 3 - Fizz,
        число кратно 5 - Buzz,
        число кратно 3 и 5 - FizzBuzz,
        иначе само число
     """
    retstr = ""
    for k, v in ((3, "Fizz"), (5, 'Buzz')):  # Проверка на кратность
        if num % k == 0:
            retstr += v
    if retstr == "":  # Не кратно заданным числам
        return num
    return retstr


while __name__ == '__main__':
    inpstr = input("Введите целое число или пустую строку для выхода: ")
    if not inpstr:  # Если пустая строка - на выход
        break
    try:
        inpnum = int(inpstr)  # Попытка преобразовать введенную строку в целое число
    except ValueError:
        print("Это не число")
        continue
    print(fizbuz(inpnum))