def read_input():
    with open('input.txt') as f:
        return f.read().splitlines()


if __name__ == '__main__':
    lines = read_input()

    n = len(lines)
    sum = 0

    for line in lines:
        main_part = line.split(':')[1]
        fp, sp = main_part.split('|')
        winning_nums = [int(x) for x in fp.split()]
        my_nums = [int(x) for x in sp.split()]
        curr_correct = len(set(winning_nums).intersection(set(my_nums)))
        if curr_correct > 0:
            sum += pow(2, curr_correct - 1)

    print(sum)
