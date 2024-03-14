#задание 2 исправление
#добавил инпут, так интереснее

v = int(input('Введите сколько на гашетке: '))
t = int(input ('Введите сколько едет по времени: '))
road = 109
track = v*t
if track > road:
    point = track%road
    print(point)
else:
    print(track)