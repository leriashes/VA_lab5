import numpy as np
import matplotlib.pyplot as plt
import math
import getch

#вычисление значений функции
def count_function(xs, func):
    ys = []

    for i in range(len(xs)):
        x = xs[i]
        ys.append(eval(func))
    return ys

def rectangleRight(ys, h):

    result = 0

    for i in range (len(ys) - 1):
        result += ys[i]

    result *= h

    return result

def rectangleMiddle(func, a, b, h):
    return

def rectangleLeft(func, a, b, h):
    return


while True:
    print('Введите функцию: y = ', end='')
    func = input()
    print('\n')

    print('Введите левую границу отрезка: a = ', end='')
    a = float(input())
    print('\n')

    while True:
        print('Введите правую границу отрезка: b = ', end='')
        b = float(input())
        print('\n')

        if b > a:
            break

    print('Введите шаг: h = ', end='')
    h = float(input())
    print('\n')

    xs = np.arange(a, b + h, h)
    ys = count_function(xs, func)

    print('Метод правых прямоугольников: ', rectangleRight(ys, h))

    print('\n\nЧтобы продолжить нажмите Enter. Для выхода из программы нажмите любую другую клавишу. ', end='')
    cont = getch.getch()
   
    if cont == '\n' or cont == b'\r':
        print('\n\n')
    else:
        break
