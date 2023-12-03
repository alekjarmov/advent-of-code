import re

valid_sum = 0

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


def is_valid_part(part):
    red_matches = re.findall(red_regex, part)
    green_matches = re.findall(green_regex, part)
    blue_matches = re.findall(blue_regex, part)
    num_red = iterate_matches(red_matches)
    num_green = iterate_matches(green_matches)
    num_blue = iterate_matches(blue_matches)
    print(num_red, num_green, num_blue, line)
    if num_red > maxes["red"] or num_green > maxes["green"] or num_blue > maxes["blue"]:
        return False
    return True


def is_valid_line(line):
    second_part = line.split(":")[1]
    parts = second_part.split(";")
    for part in parts:
        if not is_valid_part(part):
            return False
    return True


for id, line in enumerate(open("input.txt")):
    if is_valid_line(line):
        valid_sum += id + 1

print(valid_sum)
