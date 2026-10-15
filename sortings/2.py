A = list(map(int, input().split()))

def InsertionSort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

    return a

InsertionSort(A)

for i in range(len(A)):
    print(A[i],end=' ')