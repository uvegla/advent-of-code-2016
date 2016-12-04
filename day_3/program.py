# Day 3: Squares With Three Sides


def main():
    possible_triangles = 0

    for triangle in open('input.txt').readlines():
        (a, b, c) = (int(i) for i in triangle.split())
        if a + b <= c or a + c <= b or b + c <= a:
            continue

        possible_triangles += 1

    print(possible_triangles)

main()
