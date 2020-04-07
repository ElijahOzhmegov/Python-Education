

def merge(A: list, B: list):
    C = [0]*(len(A) + len(B))
    i = k = n = 0

    while (i < len(A)) and (k < len(B)):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
        else:
            C[n] = B[k]
            k += 1
        n += 1

    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1

    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1

    return C


def merge_sort(A):
    if len(A) <= 1:
        return
    middle = len(A) // 2
    L, R = A[:middle], A[middle:]

    merge_sort(L)
    merge_sort(R)

    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]


if __name__ == '__main__':
    aa = [8, 3, 2, 9, 11, 9]
    merge_sort(aa)
    print(aa)

