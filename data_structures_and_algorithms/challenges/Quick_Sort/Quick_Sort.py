'''
This function takes last element as pivot, places 
the pivot element at its correct position in sorted 
array, and places all smaller (smaller than pivot) 
to left of pivot and all greater elements to right 
of pivot 
'''

def partition(arr,left,right): 
    i = ( left-1 )         # index of smaller element 
    pivot = arr[right]     # pivot 
  
    for j in range(left , right): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[right] = arr[right],arr[i+1] 
    return ( i+1 ) 

'''
The main function that implements QuickSort 
arr[] --> Array to be sorted, 
left  --> Starting index, 
right  --> Ending index 
'''
# Function to do Quick sort 
def quickSort(arr,left,right): 
    if left < right: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,left,right) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, left, pi-1) 
        quickSort(arr, pi+1, right)
    return arr
  

if __name__ == "__main__":
    # Driver code to test above 
    arr = [10, 7, 8, 9, 1, 5] 
    n = len(arr) 
    quickSort(arr,0,n-1) 
    print ("Sorted array is:") 
    print(arr)
