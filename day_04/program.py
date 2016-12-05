# Day 4: Security Through Obscurity

from collections import Counter


def main():
    result = 0

    for data in open('input.txt').readlines():
        tokens = data.split('-')
        string = ''.join(''.join(tokens[:-1]))

        common = Counter(string).most_common()
        common = sorted(common, key=lambda x: (-x[1], x[0]))[:5]

        checksum = ''.join([letter[0] for letter in common])

        split = tokens[-1].split('[')

        if checksum == split[1][:-2]:
            result += int(split[0])

    print(result)

main()
