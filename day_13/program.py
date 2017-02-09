# Day 13: A Maze of Twisty Little Cubicles

from queue import Queue

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

NEIGHBOURS = (UP, DOWN, LEFT, RIGHT)


def is_open_space(seed, x, y):
    return bin(x ** 2 + 3 * x + 2 * x * y + y + y ** 2 + seed).count('1') % 2 == 0


def generate_maze(seed, size):
    return [['.' if is_open_space(seed, x, y) else '#' for x in range(size)] for y in range(size)]


def get_neighbours(seed, vertex):
    x0, y0 = vertex

    neighbours = []

    for i, j in NEIGHBOURS:
        x = x0 + i
        y = y0 + j

        if x < 0 or y < 0:
            continue
        elif is_open_space(seed, x, y):
            neighbours.append((x, y))

    return neighbours


def main(seed, target, max_distance):
    maze = generate_maze(seed, max(target) + 1)
    print(maze)

    visited_vertices = []
    finished_vertices = []

    distances = {}
    parents = {}

    start = (1, 1)

    distances[start] = 0
    parents[start] = None

    todo_vertices = Queue()
    todo_vertices.put(start)

    while not todo_vertices.empty():
        vertex = todo_vertices.get()

        for x in get_neighbours(seed, vertex):
            if x not in visited_vertices:
                visited_vertices.append(x)

                distances[x] = distances[vertex] + 1
                parents[x] = vertex

                todo_vertices.put(x)

                if x == target:
                    print("Reached {} in {} steps.".format(x, distances[x]))

        finished_vertices.append(vertex)

    distinct_vertices = 0
    for vertex in visited_vertices:
        if distances[vertex] <= max_distance:
            distinct_vertices += 1

    print("There are {} distinct vertices reachable in at most {} steps.".format(distinct_vertices, max_distance))


main(1352, (31, 39), 50)
