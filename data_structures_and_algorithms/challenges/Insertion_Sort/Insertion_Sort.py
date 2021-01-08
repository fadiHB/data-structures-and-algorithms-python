'''
Pseudocode
  InsertionSort(int[] arr)
  
    FOR i = 1 to arr.length
    
      int j <-- i - 1
      int temp <-- arr[i]
      
      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1
        
      arr[j + 1] <-- temp
'''
# ascending order
def insertion_sort(lst):
    for i in range(1,len(lst)):
        j = i - 1
        temp = lst[i]
        while j >= 0 and temp < lst[j]: # for descending order, just change j to i
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = temp
    return lst

        

        

if __name__ == '__main__':
    lst = [8,7,6,5,4,3]
    print(insertion_sort(lst))
