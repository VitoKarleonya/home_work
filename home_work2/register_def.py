
import json

def register(login, password):
    try:
        # Открываем файл с данными пользователей для чтения
        with open('user_data.json', 'r') as f:
            # Загружаем данные из файла в формате JSON
            user_data = json.load(f)
    except FileNotFoundError:
        # Если файл не найден, создаем пустой словарь для данных пользователей
        user_data = {}

    # Проверяем, существует ли пользователь с заданным логином
    if login in user_data:
        print('Пользователь с таким логином уже существует.')
    else:
        # Добавляем нового пользователя в словарь данных пользователей
        user_data[login] = password
        # Записываем обновленные данные пользователей в файл
        with open('user_data.json', 'w') as f:
            json.dump(user_data, f)
        print('Пользователь успешно зарегистрирован.')

# Пример использования
login = input('Введите логин: ')
password = input('Введите пароль: ')
register(login, password)
