def read_input():
    with open('input.txt') as f:
        return f.read().splitlines()


def check_touching(mat, i, j):
    combinations = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for x, y in combinations:
        if 0 <= i + x < len(mat) and 0 <= j + y < len(mat):
            if not mat[i + x][j + y].isdigit() and mat[i + x][j + y] != '.':
                return True
    return False


if __name__ == '__main__':
    mat = read_input()
    n = len(mat)
    sum = 0
    for i in range(n):
        prev_num = False
        num = 0
        touching = False
        for j in range(n):
            if mat[i][j].isdigit():
                touching = touching or check_touching(mat, i, j)
                num = num * 10 + int(mat[i][j])
                prev_num = True
            elif not mat[i][j].isdigit() and prev_num:
                if touching:
                    sum += num
                num = 0
                touching = False
                prev_num = False
        if touching:
            sum += num

    print(sum)
