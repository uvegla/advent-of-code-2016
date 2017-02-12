# Day 14: One-Time Pad

import re
import hashlib

REGEX_MATCH_3_TIMES = r"([a-f0-9])\1{2}"
REGEX_MATCH_5_TIMES = r"([a-f0-9])\1{4}"


def md5_hexdigest(raw):
    m = hashlib.md5()
    m.update(raw.encode('utf-8'))
    return m.hexdigest()


def generate_hash(salt, index, number_of_rehashes):
    digest = md5_hexdigest(''.join((salt, index)))

    for i in range(number_of_rehashes):
        digest = md5_hexdigest(digest)

    return int(index), digest


def generate_next_n_hash(salt, n, number_of_rehashes):
    next_n_hash = [generate_hash(salt, str(index), number_of_rehashes) for index in range(n)]

    next_index = n
    while True:
        yield next_n_hash

        next_n_hash.pop(0)
        next_n_hash.append(generate_hash(salt, str(next_index), number_of_rehashes))
        next_index += 1


def find_all(regex, hash_str):
    return re.findall(regex, hash_str)


def main(salt, number_of_rehashes):
    keys_found = 0

    for hashes in generate_next_n_hash(salt, 1 + 1000, number_of_rehashes):
        index_0, hash_0 = hashes[0]
        matches_0 = find_all(REGEX_MATCH_3_TIMES, hash_0)

        if matches_0:
            for index_n, hash_n in hashes[1:]:
                matches_n = find_all(REGEX_MATCH_5_TIMES, hash_n)

                if matches_0[0] in matches_n:
                    keys_found += 1

                    if keys_found == 64:
                        print(index_0)
                        exit()

                    break


# main('ihaygndm', 0)
main('ihaygndm', 2016)
