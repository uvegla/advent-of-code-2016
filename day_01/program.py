# Day 1: No Time for a Taxicab

POSITIVE_DIRECTION = 1


def get_direction_facing_y_axis(direction, turn):
    if direction == POSITIVE_DIRECTION:
        return -1 if turn == 'L' else 1
    else:
        return 1 if turn == 'L' else -1


def main():
    steps = open('input.txt').readline().rsplit(', ')

    facing_y_axis = True
    direction = POSITIVE_DIRECTION

    distance_x = 0
    distance_y = 0

    for step in steps:
        turn = step[0:1]
        distance = int(step[1:])

        facing_y_axis = not facing_y_axis

        if facing_y_axis:
            direction = get_direction_facing_y_axis(direction, turn)
            distance_y += direction * distance
        else:
            direction = -1 * get_direction_facing_y_axis(direction, turn)
            distance_x += direction * distance

    print(abs(distance_x) + abs(distance_y))

main()
