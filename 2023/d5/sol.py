import numpy as np


def read_input():
    with open('input') as f:
        return f.read().split("\n\n")


def get_mapping(value_start, key_start, range, key):
    if key_start <= key < key_start + range:
        return value_start + key - key_start
    return key


def map_numbers(part: str, current_nums: list):
    part = part.split(":\n")[1]
    parts = part.splitlines()

    ranges = []
    for part in parts:
        vs, ks, length = (int(x) for x in part.split())
        ranges.append((vs, ks, length))

    mapped_nums = []
    for num in current_nums:
        is_mapped = False
        for vs, ks, length in ranges:
            mapping = get_mapping(vs, ks, length, num)
            if mapping != num:
                mapped_nums.append(mapping)
                is_mapped = True
                break
        if not is_mapped:
            mapped_nums.append(num)

    return mapped_nums


if __name__ == '__main__':
    lines = read_input()
    our_seeds = [int(x) for x in lines[0].split(":")[1].split()]

    for part in lines[1:]:
        our_seeds = map_numbers(part, our_seeds)

    print(min(our_seeds))
