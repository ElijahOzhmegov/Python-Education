def choose_best_sum(t, k, ls):
    def generate_combinations(ls, m: int, prefix=None):
        if m == 0:
            prefix_sum = sum(prefix)
            if prefix_sum <= t:
                warehouse.append(prefix_sum)
            return
        if len(ls) < m: return
        prefix = prefix or []

        for ii in range(len(ls)):
            prefix.append(ls[ii])
            generate_combinations(ls[ii + 1:], m - 1, prefix)
            prefix.pop()

    warehouse = []
    generate_combinations(ls, k)
    warehouse.sort()

    if len(warehouse) == 0: return None
    print(warehouse[-1])
    return warehouse[-1]


if __name__ == '__main__':
    xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
    assert choose_best_sum(230, 4, xs) == 230
    assert choose_best_sum(430, 5, xs) == 430
    assert choose_best_sum(430, 8, xs) == None
