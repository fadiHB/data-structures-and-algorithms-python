# insertion  Sort

Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

## Problem Domain:
Write a function that implements the insertion sort algorithm, where the input is a list and the output is the sorted list.

## Algorithm
To sort an array of size n in ascending order:
1: Iterate from arr[1] to arr[n] over the array.
2: Compare the current element (key) to its predecessor.
3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

## Pseudo Code:

InsertionSort(int[] arr)

FOR i = 1 to arr.length

    int j <-- i - 1
    int temp <-- arr[i]
    
    WHILE j >= 0 AND temp < arr[j]
    arr[j + 1] <-- arr[j]
    j <-- j - 1
    
    arr[j + 1] <-- temp

Trace (Visual):
Input: [23, 1, 10, 5, 2]


![trace](inser_sort_blog.jpg)

Time Complexity:

|method|Time|space|
|:--:|:--:|:--|
|marge_sort|O(n ^ 2)|O(1)|