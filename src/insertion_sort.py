def insertion_sort(A):
    for j in range(len(A)):
        key = A[j]
        i = j - 1

        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1

        A[i+1] = key

A = [10,9,8,7,6,5,4,3,2,1,500,-1]
insertion_sort(A)
print(A)