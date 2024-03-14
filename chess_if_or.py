
#Модуль 2
#задание 2

# Задаем положение шахматы
horizontal_rook = int(input('Введите номер клетки для ладьи по горизонтали: '))
vertical_rook = int(input('Введите номер клетки для ладьи по вертикали: '))
# Вводим возможный или невозможный ход
horizontal_move = int(input('Введите номер клетки хода по горизонтали: '))
vertical_move = int(input('Введите номер клетки хода по вертикали: '))
# Сравнение сопадает ли хотя бы одно из условий расположения ладьи и номера клетки
if horizontal_rook == horizontal_move or vertical_rook == vertical_move:
    print("YES")
else:
    print("NO")
