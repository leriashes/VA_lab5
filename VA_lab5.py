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

def rectangleMiddle(func, xs, h):

    n = int((xs[len(xs) - 1] - xs[0]) // h)

    result = 0

    for i in range (n):
        x = xs[0] + h/2 + h * i
        result += eval(func)

    result *= h

    return result

def rectangleLeft(ys, h):

    result = 0

    for i in range (1, len(ys)):
        result += ys[i]

    result *= h

    return result

def trapeze(ys, h):

    result = (ys[0] + ys[len(ys) - 1]) / 2

    for i in range (1, len(ys) - 1):
        result += ys[i]

    result *= h

    return result

def Simpson(ys, h):

    if len(ys) % 2 == 0:
        return 'нечётное число отрезков! '
    else:
        result = ys[0] + ys[len(ys) - 1]

        for i in range (1, len(ys), 2):
            result += ys[i] * 4

        for i in range (2, len(ys) - 1, 2):
            result += ys[i] * 2

        result *= h / 3

        return result

def Runge(func, xs, hu, eps):
    h = hu
    k = 1
    n = len(xs - 1)
    ready = False

    while not ready:
        ready = True
        for i in range(n * k - 1):
            xs1 = [xs[0] + h * i, xs[0] + h * i + h]
            if abs(rectangleMiddle(func, xs1, h / 2) - rectangleMiddle(func, xs1, h)) > eps * h / (xs[len(xs) - 1] - xs[0]):
                h /= 2
                k += 1
                ready = False
                break

    return h

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

    while True:
        print('Введите шаг: h = ', end='')
        h = float(input())
        print('\n')

        if h <= b - a:
            break
    
    while True:
        print('Введите допустимую относительную погрешность: eps = ', end='')
        eps = float(input())
        print('\n')

        if eps > 0:
            break

    xs = np.arange(a, b + h, h)
    ys = count_function(xs, func)

    print('Метод правых прямоугольников: ', rectangleRight(ys, h))
    print('\nМетод средних прямоугольников: ', rectangleMiddle(func, xs, h))
    print('\nМетод левых прямоугольников: ', rectangleLeft(ys, h))
    print('\nМетод трапеций: ', trapeze(ys, h))
    print('\nМетод Симпсона: ', Simpson(ys, h))

    hauto = Runge(func, xs, h, eps)
    xs = np.arange(a, b + hauto, hauto)

    print('\nАвтоматический шаг: ', hauto)

    print('\nМетод средних прямоугольников: ', rectangleMiddle(func, xs, hauto))

    print('\n\nЧтобы продолжить нажмите Enter. Для выхода из программы нажмите любую другую клавишу. ', end='')
    cont = getch.getch()
   
    if cont == '\n' or cont == b'\r':
        print('\n\n')
    else:
        break
