def bubble_sort(A):
    for i in range(len(A)):
        swapped = False

        for j in range(len(A) - i - 1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swapped = True
        
        if not swapped:
            break

A = [10,9,8,7,6,5,4,3,2,1,500,-1]
bubble_sort(A)
print(A)