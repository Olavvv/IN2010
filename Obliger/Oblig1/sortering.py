import math
# Insertion_sort metoden tar inn Array 'A' og bruker insertion_sort algoritmen for aa sortere den.
def insertion_sort(A):
    for i in range(1, len(A)):
        j = i
        while (j > 0 and A[j-1] > A[j]):
            A[j-1], A[j] = A[j], A[j-1]
            j = j-1
    return A

def merge_sort(A):
    if len(A) <= 1:
        return A
    i = math.floor((len(A)/2))
    A1 = merge_sort(A[:i])
    A2 = merge_sort(A[i:])
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

"""
fileName = input()
A = []
with open(fileName, 'r') as file:
    for line in file:
        A.append(int(line))
"""



example = [2,3,6,1,4,5]
print(insertion_sort(example))
print(merge_sort(example))