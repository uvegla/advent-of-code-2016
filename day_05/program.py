# Day 5: How About a Nice Game of Chess?

import hashlib


def main():
    door_id = open('input.txt').readline()

    i = 0
    password = ''

    while True:
        m = hashlib.md5()
        m.update(''.join((door_id, str(i))).encode('utf-8'))

        digest = m.hexdigest()
        if digest.startswith('00000'):
            password += digest[5]
            print(password + ' ' + digest)

        if len(password) == 8:
            break

        i += 1

    print(password)

main()
