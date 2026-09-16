N = int(input())

if N == 1:
    print(1)
else:
    A = [1, 2]

    for n in range(3, N + 1):
        middle = (n - 1) // 2

        x = A[middle]
        A[middle] = n
        A.append(x)

    print(*A)
