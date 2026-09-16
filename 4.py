number = int,input()
A = list(map(int, input().split()))
count = 0

def BubbleSort(A):
    n = len(A)
    t = 5
    count = 0
    while t != 0:
        for i in range(n):
            for j in range(n - 1):
                if A[j] > A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j]
                    count += 1
        t -= 1

    return A, count

A, count = BubbleSort(A)

print(count)