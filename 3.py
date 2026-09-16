A = list(map(int, input().split()))

def BubbleSort(A):
    n = len(A)
    t = 5
    while t != 0:
        for i in range(n):
            for j in range(n - 1):
                if A[j] < A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j]
        t -= 1

    return A

BubbleSort(A)

for i in range(len(A)):
    print(A[i],end=' ')