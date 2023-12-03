import re

power_sum = 0

maxes = dict()
maxes["red"] = 12
maxes["green"] = 13
maxes["blue"] = 14

red_regex = r"[0-9]+ red"
green_regex = r"[0-9]+ green"
blue_regex = r"[0-9]+ blue"


def iterate_matches(matches):
    sum = 0
    for match in matches:
        num = int(match.split()[0])
        sum += num
    return sum


def part_nums(part):
    red_matches = re.findall(red_regex, part)
    green_matches = re.findall(green_regex, part)
    blue_matches = re.findall(blue_regex, part)
    num_red = iterate_matches(red_matches)
    num_green = iterate_matches(green_matches)
    num_blue = iterate_matches(blue_matches)
    return num_red, num_green, num_blue


def get_power(line):
    second_part = line.split(":")[1]

    parts = second_part.split(";")
    max_red, max_green, max_blue = 0, 0, 0
    for part in parts:
        num_red, num_green, num_blue = part_nums(part)
        max_red = max(max_red, num_red)
        max_green = max(max_green, num_green)
        max_blue = max(max_blue, num_blue)
    print(max_red, max_green, max_blue, second_part)
    return max_red * max_green * max_blue


for id, line in enumerate(open("input.txt")):
    power_sum += get_power(line)

print(power_sum)
