import math

def sort(A):
    if len(A) <= 1:
        return A
    i = math.floor((len(A)/2))
    A1 = sort(A[:i])
    A2 = sort(A[i:])
    return merge(A, A1, A2)

def merge(A, A1, A2):
    i = 0
    j = 0
    while (i < len(A1) and j < len(A2)):
        if (A1[i] <= A2[j]):
            A[i + j] = A1[i]
            i += 1
        else:
            A[i + j] = A2[j]
            j += 1
    while (i < len(A1)):
        A[i + j] = A1[i]
        i += 1
    while (j < len(A2)):
        A[i + j] = A2[j]
        j += 1
    return A
    # Do merge sort here. Use the Sorter's comparison- and swap
    # methods for automatically counting the swaps and comparisons.

    # Use A.swap(i, j) to swap the values at two indices i and j. The swap is
    # counted, when using this method. Comparisons are counted automatically.
