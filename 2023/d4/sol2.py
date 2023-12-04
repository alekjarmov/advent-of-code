def read_input():
    with open('input.txt') as f:
        return f.read().splitlines()


if __name__ == '__main__':
    lines = read_input()

    n = len(lines)
    counter = {i: 1 for i in range(n)}
    print(counter)
    print("-----------------")
    for i, line in enumerate(lines):
        print(line)
        main_part = line.split(':')[1]
        fp, sp = main_part.split('|')
        winning_nums = [int(x) for x in fp.split()]
        my_nums = [int(x) for x in sp.split()]
        curr_correct = len(set(winning_nums).intersection(set(my_nums)))

        for j in range(i + 1, i + curr_correct + 1):
            print("j:", j)
            if j in counter.keys():

                counter[j] = counter[j] + counter[i]

        print("correct nums for card ", i + 1, ":", curr_correct)
        print(counter)

    print(counter)
    print(sum(counter.values()))
