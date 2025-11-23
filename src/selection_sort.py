def selection_sort(A):
    for i in range(len(A)):
        min = i

        for j in range(i+1, len(A)):
            if A[j] < A[min]:
                min = j

        A[i], A[min] = A[min], A[i]
   
A = [10,9,8,7,6,5,4,3,2,1,500,-1]
selection_sort(A)
print(A)