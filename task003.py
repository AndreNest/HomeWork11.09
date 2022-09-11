def Number():
    try:
        num = int(input('Введите число: '))
        return num
    except(ValueError):
        return Number()

def Palindrom(num):
    count = 0
    if int(num) < 0 or int(num) == 196:
        print(f'Полиндрома для числа "{num}" не существует')
    elif num != num[:: -1]:
        num = str(int(num)+int(num[::-1]))
        return Palindrom(num) 
    else: 
        return print(f'Палиндром = {num}')
number = str(Number())
Palindrom(number)


