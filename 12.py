A = list(map(int, input().split()))
B = list(map(int, input().split()))

def SelectionSort(A):
    n = len(A)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]

def Calculator(A, B):
    summary = 0
    SelectionSort(A)
    SelectionSort(B)
    n = len(A)
    l = n
    for i in range(0, n):
        summary += A[i] * B[l-1]
        l -= 1

    return summary

summary = Calculator(A, B)

print(summary)