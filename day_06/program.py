# Day 6: Signals and Noise

from collections import Counter

MESSAGE_LENGTH = 8

MOST_COMMON = 0
LEAST_COMMON = -1


def decode(full_text, index):
    error_corrected = ''
    for i in range(0, MESSAGE_LENGTH):
        error_corrected += Counter(full_text[i::MESSAGE_LENGTH]).most_common()[index][0]

    return error_corrected


def main():
    full_text = ''
    for message in open('input.txt').readlines():
        full_text += message[0:MESSAGE_LENGTH]

    print(decode(full_text, MOST_COMMON))
    print(decode(full_text, LEAST_COMMON))

main()
