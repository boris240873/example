
a = int(input('Введите число: '))
b = a - 1
while a < 2:
    a = int(input())
while a % b != 0:
    b = b - 1
if a % b == 0:
    b = a // b
    print('Наименьший делитель, отличный от единицы: ', b)