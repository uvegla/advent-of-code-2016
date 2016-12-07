# Day 7: Internet Protocol Version 7

import re

PALINDROME_LENGTH = 4


def supports_tls(sequences):
    is_valid = False

    for sequence in sequences:
        hypernet = is_hypernet_sequence(sequence)
        raw_sequence = sequence[1:-1] if hypernet else sequence

        has_abba = is_abba_sequence(raw_sequence)

        if hypernet and has_abba:
            return False

        if not is_valid and has_abba:
            is_valid = True

    return is_valid


def is_hypernet_sequence(sequence):
    return sequence.startswith('[')


def is_abba_sequence(sequence):
    for i in range(0, len(sequence) - PALINDROME_LENGTH + 1):
        partial = sequence[i:i + PALINDROME_LENGTH]

        if partial == partial[::-1] and partial[0] != partial[1]:
            return True

    return False


def main():
    result = 0

    for ip_address in open('input.txt').readlines():
        sequences = re.findall('[a-z]+|\[[a-z]+\]', ip_address)

        if supports_tls(sequences):
            result += 1

    print(result)

main()
