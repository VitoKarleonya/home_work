l = [1, 4, 1, 6, "hello", "a", 5, "hello"]
duplicates = []
#в начале индексируем список, чтобы бы можно было провожить итерацию
for i in range(len(l)):
#сравниваем значение со следующим значением	и если оно равно одному из значений в индексации len и не в дубликатах, добавляется в дубликаты
    for j in range(i + 1, len(l)):
        if l[i] == l[j] and l[i] not in duplicates:
            duplicates.append(l[i])

print("Повторяющиеся значения:", duplicates)
