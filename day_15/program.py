# Day 15: Timing is Everything

import re


def parse_disc(disc):
    order, holes, time, start_position = re.findall('[0-9]+', disc)

    # Input contains discs in order and at t0, no need to normalize
    return int(holes), int(start_position)


def calculate_disc_position(disc, time):
    holes, start_position = disc

    return (start_position + time) % holes


def main():
    discs = [parse_disc(disc) for disc in open('input.txt').readlines()]

    time = 0

    while True:
        positions = [calculate_disc_position(discs[i], time + i + 1) for i in range(0, len(discs))]

        if len(set(positions)) == 1:
            print(time)
            break

        time += 1

main()
