def left_bound(A, key):
    left = -1
    right = len(A)

    while right - left > 1:
        middle = (right + left) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle

    return left


if __name__ == '__main__':
    ss = [2, 3, 8, 9, 9, 11]
    print(left_bound(ss, 12))
