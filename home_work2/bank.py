#модуль 3 задание 1


def bank_system():
    x = float(input('Contribution: '))
    y = float(input('Point profit: '))
    p = float(input('Profit: '))
    amount = 0
    t = 0  
    while amount < y:
        t += 1
        amount = x * (1 + p / 100) ** t 

    print("Number of years:", t)

bank_system()
    



