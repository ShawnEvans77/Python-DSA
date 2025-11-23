def binary_search(A, x):
    start = 0
    end = len(A)

    while start <= end:
        mid = (start + end) // 2

        if A[mid] == x:
            return mid
        elif A[mid] < x:
            start = mid + 1
        elif A[mid] > x:
            end = mid - 1

A = [1,2,3,4,5,6,7,100]

print(binary_search(A, 100))