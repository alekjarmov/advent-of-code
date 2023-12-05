import numpy as np


def read_input():
    with open('input') as f:
        return f.read().split("\n\n")


def get_mapping(value_start, key_start, range, key):
    if key_start <= key < key_start + range:
        return value_start + key - key_start
    return key


def get_map(part: str):
    part = part.split(":\n")[1]
    parts = part.splitlines()

    map = []
    for part in parts:
        vs, ks, length = (int(x) for x in part.split())
        map.append((vs, ks, length))

    return map


if __name__ == '__main__':
    lines = read_input()

    our_seeds = [int(x) for x in lines[0].split(":")[1].split()]
    intervals = [[our_seeds[i], our_seeds[i + 1]] for i in range(0, len(our_seeds), 2)]
    print(intervals)
    maps = [get_map(part) for part in lines[1:]]
    for m in maps:
        mapped_intervals = []
        for interval in intervals:
            is_mapped = False
            for vs, ks, length in m:
                if ks < interval[0] + interval[1] and interval[0] < ks + length:
                    ns = max(interval[0], ks)
                    nl = min(interval[0] + interval[1], ks + length) - ns
                    mapped_intervals.append([ns - ks + vs, nl])
                    if ns > interval[0]:
                        intervals.append([interval[0], ns - interval[0]])
                    if ns + nl < interval[0] + interval[1]:
                        intervals.append([ns + nl, interval[0] + interval[1] - ns - nl])
                    is_mapped = True
                    break

            if not is_mapped:
                mapped_intervals.append(interval)
        intervals = mapped_intervals
        print(intervals)

    print(min(i[0] for i in intervals))
