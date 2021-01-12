from math import pi

figure = input()
a = float(input())
b = a

if figure == 'rectangle' or figure == 'triangle':
    b = float(input())

if figure == 'square' or figure == 'rectangle':
    print(a * b)
elif figure == 'circle':
    print(pi * a ** 2)
elif figure == 'triangle':
    print((a * b) / 2)