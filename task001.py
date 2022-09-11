def Number(num):
    try:
        float(num)
        return True
    except:
        return False
def Sum_Numb(num):
    while Number(num) == False:
        num = input("Значение неверно, введите число: ")
    else:
        if float(num) < 0:
            num = abs(float(num))
        num_str = str(num)
        num_list = list(num_str)
        sum = 0
        for i in range(0, len(num_str)):
            if(num_list[i] != '.'):
                sum += int(num_list[i])
        first_num = num
        return print(f'сумма цифр числа "{first_num}" =  {sum} ')
Sum_Numb(input("Введите число: "))
