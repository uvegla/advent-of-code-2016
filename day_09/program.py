# Day 9: Explosives in Cyberspace


def read_marker(file):
    marker = ''

    character = file.read(1)
    while character != ')':
        marker += character
        character = file.read(1)

    return (int(i) for i in marker.split('x'))


def main():
    decompressed_length = 0

    with open('input.txt') as file:
        while True:
            character = file.read(1)

            if not character:
                break

            if character == '(':
                length, times = read_marker(file)

                decompressed_length += length * times
                file.read(length)
            else:
                decompressed_length += 1

    print(decompressed_length)


main()
