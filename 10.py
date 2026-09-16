def SelectionSort(A):
    n = len(A)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if A[j] + A[max_index] > A[max_index] + A[j]:
                max_index = j
        A[i], A[max_index] = A[max_index], A[i]

A = []

while True:
    try:
        s = input()
        if s == "":
            break
        A.append(s)
    except EOFError:
        break

SelectionSort(A)

print("".join(A))