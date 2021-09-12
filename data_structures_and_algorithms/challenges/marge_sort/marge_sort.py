def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        # into 2 halves

        L = arr[:mid]
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        # Copy data to temp arrays L[] and R[]
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left on the Left(L)
        # move all the remaining elements to the arr list one by one
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        # Checking if any element was left on the Right(R)
        # move all the remaining elements to the arr list one by one
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
 
 
 
# Driver Code
if __name__ == '__main__':
    arr = [9,7,8,3,2,1]
    print("Given list is", end="\n")
    print(arr)
    mergeSort(arr)
    print("Sorted list is: ", end="\n")
    print(arr)