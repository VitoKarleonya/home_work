import json

def user_login():
    # Ввод логина и пароля от пользователя
    login_input = input('Введите логин: ')
    password_input = input('Введите пароль: ')

    # Попытка открыть файл с данными пользователей
    try:
        with open('user_data.json', 'r') as file:
            # Загрузка данных из файла JSON
            user_data = json.load(file)
            # Проверка соответствия введенных данных данным из файла
            if user_data['login'] == login_input and user_data['password'] == password_input:
                print('Вход выполнен успешно.')
                return
    except FileNotFoundError:
        # Если файл не найден, предложим пользователю зарегистрироваться
        print('Файл с данными пользователей не найден. Создайте новый аккаунт.')
        choice = input('Хотите зарегистрироваться? (yes/no): ')
        if choice.lower() == 'yes':
            # Запросим у пользователя логин и пароль для регистрации
            new_login = input('Введите новый логин: ')
            new_password = input('Введите новый пароль: ')
            # Регистрация нового пользователя
            with open('user_data.json', 'w') as file:
                json.dump({'login': new_login, 'password': new_password}, file)
            print('Пользователь успешно зарегистрирован.')
            return

    # Если вход не удался и регистрация не требуется, сообщим об ошибке
    print('Ошибка входа.')

# Пример использования:
user_login()
