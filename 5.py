number = int,input()
A = list(map(int, input().split()))

def MergeSort(A):
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    L = MergeSort(A[:mid])
    R = MergeSort(A[mid:])
    C = []
    i = 0
    j = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            C.append(L[i])
            i += 1
        else:
            C.append(R[j])
            j += 1
    C += L[i:]
    C += R[j:]

    return C


A = MergeSort(A)

for i in range(len(A)):
    print(A[i],end=' ')