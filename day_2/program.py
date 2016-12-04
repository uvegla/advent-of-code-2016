# Day 2: Bathroom Security

import numpy as np

# Coordinates : (row, column)
# Upper left is (0, 0) = 1
# Center is (1, 1) = 5
# Bottom right is (2, 2) = 9

START_POSITION = (1, 1)

COMMANDS = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}


def decode(instructions, position):
    for instruction in instructions:
        position = np.add(position, COMMANDS[instruction])
        position = np.clip(position, 0, 2)

    return position


def to_key(position):
    return 3 * position[0] + position[1] + 1


def main():
    position = START_POSITION

    for instructions in open('input.txt').readlines():
        position = decode(instructions.strip(), position)
        print(to_key(position), end="")

main()
