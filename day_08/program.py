# Day 8: Two-Factor Authentication

import re

import numpy as np

PIXEL_OFF = 0
PIXEL_ON = 1

SCREEN_WIDTH = 7
SCREEN_HEIGHT = 3


def rect(screen, columns, rows):
    screen[:rows, :columns].fill(PIXEL_ON)


def rotate_column(screen, column, by):
    screen[:, column:column + 1] = np.roll(screen[:, column:column + 1].flatten(), by).reshape((SCREEN_HEIGHT, 1))


def rotate_row(screen, row, by):
    screen[row:row + 1, :] = np.roll(screen[row:row + 1, :].flatten(), by).reshape((1, SCREEN_WIDTH))


def main():
    screen = np.full((SCREEN_HEIGHT, SCREEN_WIDTH), PIXEL_OFF, np.int8)

    for command in open('input.txt').readlines():
        num1, num2 = (int(x) for x in re.findall('[0-9]+', command))

        if command.startswith('rect'):
            rect(screen, num1, num2)
        elif command.startswith('rotate column'):
            rotate_column(screen, num1, num2)
        else:
            rotate_row(screen, num1, num2)

    print(screen)


main()
