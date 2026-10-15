number = int,input()
A = list(map(int, input().split()))

def QuickSort(A):
    if len(A) <= 1:
        return A
    pivot = A[len(A) // 2]
    left = []
    middle = []
    right = []
    for x in A:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return QuickSort(left) + middle + QuickSort(right)

A = QuickSort(A)

for i in range(len(A)):
    print(A[i],end=' ')