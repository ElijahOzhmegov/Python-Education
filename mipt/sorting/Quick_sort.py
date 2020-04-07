

def hoare_sort(A):
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []

    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)

    hoare_sort(L)
    hoare_sort(R)

    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1


if __name__ == '__main__':
    aa = [8, 3, 2, 9, 11, 9]
    hoare_sort(aa)
    print(aa)
