sum = 0
for line in open("input.txt"):
    first, last = None, None
    for i, char in enumerate(line):

        if not char.isdigit():
            continue
        if first is None:
            first = char
        last = char

    num = int(f'{first}{last}')
    sum += num

print(sum)