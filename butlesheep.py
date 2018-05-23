from random import randint
import copy

 
"""Вывод поля<
прием координат от юзера<
Перадавать аргументы (коорд())
"""


def commander(self):
    x , y = input('введите координаты: ').split()
    OCEAN = "O"
    FIRE = "X"
    HIT = "*"
    SIZE = 10
    SHIPS = [ 4, 3, 2, 1]
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #print(numbers.join(""))
    print("  0 1 2 3 4 5 6 7 8 9 ")
    i = 0
    for row in range(SIZE):
        print(i, " ".join(player_radar[row]),)
        i += 1
