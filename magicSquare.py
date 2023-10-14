def pretty_print(matrix):
    for row in matrix:
        print(*row, sep='\t')


def check_if_magic(matrix):
    t_matrix = list(zip(*matrix))
    s = sum(matrix[0])
    n = len(matrix)
    flag = True
    for i in range(n):
        if (
            sum(matrix[i]) != s
            or sum(t_matrix[i]) != s
            or sum(matrix[i][i] for i in range(n)) != s
            or sum(matrix[i][-(i + 1)] for i in range(n)) != s
        ):
            flag = False
            break
    return flag


def magic_square_odd(n):
    # siam_magic
    matrix = [[0] * n for i in range(n)]
    x, y = 0, n // 2
    for i in range(1, n ** 2 + 1):
        matrix[x][y] = i
        if matrix[(x - 1) % n][(y + 1) % n]:
            x += 1
        else:
            x, y = (x - 1) % n, (y + 1) % n
    return matrix


def magic_square_even_even(n):
    matrix = [[0] * n for i in range(n)]
    for i in range(n**2):
        matrix[i // n][i % n] = i + 1

    for i in range(0, n // 4):
        for j in range(0, n // 4):
            matrix[i][j] = n ** 2 + 1 - matrix[i][j]

        for j in range(3 * n // 4, n):
            matrix[i][j] = n ** 2 + 1 - matrix[i][j]

    for i in range(3 * n // 4, n):
        for j in range(3 * n // 4, n):
            matrix[i][j] = n ** 2 + 1 - matrix[i][j]
        for j in range(0, n // 4):
            matrix[i][j] = n ** 2 + 1 - matrix[i][j]

    for i in range(n // 4, 3 * (n // 4)):
        for j in range(n // 4, 3 * (n // 4)):
            matrix[i][j] = n ** 2 + 1 - matrix[i][j]

    return matrix


def magic_square_even_odd(n):
    matrix = [[0] * n for i in range(n)]
    k = (n - 2) // 4
    delta = 2 * k + 1
    mini = magic_square_odd(delta)
    for i in range(delta):
        for j in range(delta):
            matrix[i][j] = mini[i][j]
            matrix[i + delta][j + delta] = mini[i][j] + n ** 2 // 4
            matrix[i + delta][j] = mini[i][j] + n ** 2 // 4 * 3
            matrix[i][j + delta] = mini[i][j] + n ** 2 // 2

    for j in range(k - 1):
        for i in range(n // 2):
            matrix[i][j], matrix[i + delta][j] = matrix[i +
                                                        delta][j], matrix[i][j]
            matrix[i][-j - 1], matrix[i + delta][-j -
                                                 1] = matrix[i + delta][-j - 1], matrix[i][-j - 1]

    for i in range(n // 2):
        if i == (n // 2) // 2:
            continue
        matrix[i][k - 1], matrix[i + delta][k -
                                            1] = matrix[i + delta][k - 1], matrix[i][k - 1]
    matrix[n // 4][k], matrix[n // 4 + delta][k] = matrix[n //
                                                          4 + delta][k], matrix[n // 4][k]

    return matrix


def make_magic_square(n):
    if n % 2:
        return magic_square_odd(n)
    elif n % 4 == 2:
        return magic_square_even_odd(n)
    elif n % 4 == 0:
        return magic_square_even_even(n)


if __name__ == '__main__':
    n = int(input())
    pretty_print(make_magic_square(n))