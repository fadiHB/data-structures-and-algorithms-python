arr = [9,7,8,3,2,1]
mergeSort(arr1)
len(arr) = 6  > 1 -> True
    mid = len(arr)//2 = 6 // 2 = 3
    L = arr[:mid] = [9,7,8]
    R = arr[mid:] = [3,2,1]

mergeSort(L)
L = [9,7,8]
len(L) = 3  > 1 -> True
    mid = len(L)//2 = 3 // 2 = 1
    L = L[:mid] = [9]
    R = L[mid:] = [7,8]

mergeSort(L)
L = [9]
len(L) = 1  > 1 -> False

mergeSort(R)
R = [7,8]
len(R) = 2 > 1 -> True
    mid = len(R) //2 = 2 //2  = 1
    L = L[:mid] = [7]
    R = R[mid:] = [8]

mergeSort(L)
    L = [7]
    len(L) = 1  > 1 -> False
mergeSort(R)
    R = [8]
    len(L) = 1  > 1 -> False

i = j = k = 0
i < len(L) and j < len(R) == 0 < 1 and 0 < 1 -> True
    L[i=0]=7 < R[j=0]=8 -> True
        arr[k=0] = L[i=0] = 7  #[7,7,8,3,2,1]
        i += 1 -> i=0+1=1

    k += 1 -> k=0+1=1

    i < len(L)  ==  1 < 1- > False

    j < len(R)  ==  0 < 1 -> True
            arr[k] = R[j] -> arr[1] = 8 #[7,8,8,3,2,1]
            j += 1 -> j=0+1=1
            k += 1 -> k=1+1=2
            
            j < len(R) == 1<1 -> False




