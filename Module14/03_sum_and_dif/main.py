def count_of_digits(n):
    return len(str(n))

def sum_of_digits(n):
    return sum(int(i) for i in str(n))

num = int(input("Введите число: "))

sums = sum_of_digits(num)
counts = count_of_digits(num)
print("\nСумма чисел:", sums)
print("\nКол-во цифр в числе:", counts)

print("\nРазность суммы и количества цифр:", sums - counts)