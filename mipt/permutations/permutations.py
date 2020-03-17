def generate_number(n: int, m: int, prefix=None):
    """ Generates all numbers length m in numerical system with
    base = n """
    prefix = prefix or []
    if m == 0:
        print(*prefix, sep='', end='  ')
        return
    for digit in range(n):
        prefix.append(digit)
        generate_number(n, m - 1, prefix)
        prefix.pop()


def generate_permutations(n: int, m: int = -1, prefix=None):
    m = n if m == -1 else m
    prefix = prefix or []
    if m == 0:
        print(*prefix, sep='')
        return
    for number in range(1, n+1):
        if number in prefix:
            continue
        prefix.append(number)
        generate_permutations(n, m-1, prefix)
        prefix.pop()


def generate_combinations(ls, m: int, prefix=None):
    if m == 0:
        print(*prefix)
        return
    if len(ls) < m: return
    prefix = prefix or []

    for ii in range(len(ls)):
        prefix.append(ls[ii])
        generate_combinations(ls[ii + 1:], m - 1, prefix)
        prefix.pop()


if __name__ == '__main__':
    # generate_number(4, 3)
    # generate_permutations(5, 3)
    generate_combinations(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], 3)
