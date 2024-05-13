def reverse_float(num):
    parts = str(num).split('.')
    reversed_parts = [''.join(reversed(part)) for part in parts]

    return float( '.'.join(reversed_parts) )

a = reverse_float(input('Введите первое число: '))
b = reverse_float(input('Введите второе число: '))

print('Первое число наоборот: ', a)
print('Второе число наоборот: ', b)
print('Сумма: ', a + b)