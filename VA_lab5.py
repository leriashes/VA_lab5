import numpy as np
import matplotlib.pyplot as plt
import math
import getch

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


    print('\n\nЧтобы продолжить нажмите Enter. Для выхода из программы нажмите любую другую клавишу. ', end='')
    cont = getch.getch()
   
    if cont == '\n' or cont == b'\r':
        print('\n\n')
    else:
        break
