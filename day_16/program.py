# Day 16: Dragon Checksum


def dragon_curve(seed):
    curve = seed
    while True:
        yield curve
        curve = ''.join([curve, '0', ''.join(['1' if i == '0' else '0' for i in curve[::-1]])])


def generate_data(seed, length):
    curve_generator = dragon_curve(seed)
    for value in curve_generator:
        if len(value) > length:
            return value[:length]


def checksum(data):
    result = ''
    for chunk in zip(data[0::2], data[1::2]):
        result += '1' if chunk[0] == chunk[1] else '0'

    if len(result) % 2 == 0:
        return checksum(result)

    return result


def main(seed, length):
    print(checksum(generate_data(seed, length)))


main('10000', 20)
main('00111101111101000', 272)
main('00111101111101000', 35651584)
