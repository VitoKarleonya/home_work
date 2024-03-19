from random import randint

n = 5
m = [[randint(0, 100) for i in range(n)] for j in range(n)]
print(m)
# Инициализация максимального значения
max_value = m[0][0]

# Поиск наибольшего значения в списке
for row in m:
    for value in row:
        if value > max_value:
            max_value = value

print("Наибольшее число из сгенерированного списка:", max_value)
