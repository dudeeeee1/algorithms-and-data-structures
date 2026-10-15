A = list(map(int, input().split()))

def CountSort(A):
    count = [0] * 200000
    for x in A:
        count[x] += 1
    k = 0
    for x in range(200000):
        while count[x] > 0:
            A[k] = x
            k += 1
            count[x] -= 1

CountSort(A)

for i in range(len(A)):
    print(A[i],end=' ')