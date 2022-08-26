"""" """

def fizbuz(num):
    retstr = ""
    for k, v in ((5, "Fiz"), (7, 'Buz')):  # Проверка на кратность
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