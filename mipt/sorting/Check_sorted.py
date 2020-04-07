
def check_sorted(A, ascending=True):
    n = len(A)
    s = 2*int(ascending) - 1
    for i in range(1, n):
        if s*A[i] < s*A[i - 1]:
            return False
    return True

if __name__ == '__main__':
    aa = [8, 3, 2, 9, 11, 9]
    ss = [2, 3, 8, 9, 9, 11]

    print(check_sorted(aa))
    print(check_sorted(ss))
