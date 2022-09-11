def Number(num):
    try:
        int(num)
        return True
    except:
        return False
def Factorial(num):
    first_num = num
    fact = 1
    list_fact = []
    while Number(num) == False and num < 0: 
        num = input("Значение неверно! Введите число: ")
    else:
        for i in range(2, num + 1):
            if i == 0:
                fact = [1]
            else:
                list_fact.append(fact)
                fact *= i
    return print(f'Факториал числа {first_num} = {fact}')  
Factorial(int(input('введите число: ')))
