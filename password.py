# Задание 3
# выполнил с помощью чат гпт, логику понял, повторить сам смогу, он рассказал мне что означает команада any(char.isupper(),any(char.lower), перебор списка я уже тоже знаю
#дальше идет проверка на True через if ,это было описано в уроке, если проходит проверку выводит принт и окнчивает программу с помощью break, если нет через else выводит принт что пароль не подходит
while True:
    password = input("Введите пароль: ")
    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    length_at_least_eight = len(password) >= 8

    if has_upper and has_lower and length_at_least_eight:
        print("Пароль удовлетворяет условиям.")
        break
    else:
        print("Пароль не удовлетворяет условиям. Попробуйте снова.")
