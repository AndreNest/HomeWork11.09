import datetime
def Number(input_string):
    try:
        num = int(input(input_string))
        return num
    except(ValueError):
        print('Ошибка ввода!')
        return Number(input_string)
def Random_Numb(min_numb, max_numb):
    num = int(datetime.datetime.now().strftime('%f')) / 10**6
    num = int(num * (max_numb - min_numb) + min_numb)
    return print(f'Случайное число = {num}')
min_numb = Number("Введите минимальное значение: ")
max_numb = Number("Введите максимальное значение: ")
result = Random_Numb(min_numb, max_numb)


