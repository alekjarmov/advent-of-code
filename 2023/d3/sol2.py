def read_input():
    with open('input.txt') as f:
        return f.read().splitlines()


def get_number(mat, i, x):
    s = e = x
    while s >= 0 and mat[i][s].isdigit():
        s -= 1
    while e < len(mat) and mat[i][e].isdigit():
        e += 1

    return i, s, e


def get_adjacent(mat, i, j):
    combinations = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    adj = []
    for x, y in combinations:
        if 0 <= i + x < len(mat) and 0 <= j + y < len(mat):
            if mat[i + x][j + y].isdigit():
                adj.append(get_number(mat, i + x, j + y))
    adj = set(adj)
    return list(adj)


if __name__ == '__main__':
    mat = read_input()
    n = len(mat)
    sum = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j] == '*':

                nums = get_adjacent(mat, i, j)
                actual_nums = [int(mat[i][s + 1: e]) for i, s, e in nums]
                if len(nums) != 2:
                    continue
                sum += actual_nums[0] * actual_nums[1]
    print(sum)
