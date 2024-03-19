original_dict = {'a': 1, 'b': 2, 'c': 3}

flipped_dict = {value: key for key, value in original_dict.items()}

print("Оригинальный словарь:", original_dict)
print("Перевернутый словарь:", flipped_dict)
