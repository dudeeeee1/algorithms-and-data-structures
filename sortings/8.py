class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = x * x + y * y

def SelectionSort(A):
    n = len(A)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if A[j].distance < A[min_index].distance:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]

n = int(input())
A = []

for _ in range(n):
    x, y = map(int, input().split())
    A.append(Point(x, y))

SelectionSort(A)

for p in A:
    print(p.x, p.y)