#модуль 3 задание 3


sum_value = int(input('Введите число сумму чисел которого надо посчитать: '))

for i in range(sum_value):
	sum_value += i
# example with sum_value = 3 : i1 + i2 + i3 = 6

#  чат подсказал метод форматирования, почитал про него отдельно
formatted_total = "{:,}".format(sum_value)

print("Сумма чисел равна", formatted_total)