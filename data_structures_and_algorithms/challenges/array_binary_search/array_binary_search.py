# def BinarySearch_even(arr):
#     left_half = list(  arr[:len(arr)//2] )
#     rigth_half = list( arr[len(arr)//2:] )
#     return {'left_half':left_half,'rigth_half':rigth_half}

# def BinarySearch_odd(arr):
#     left_half = list(  arr[:(len(arr)//2)+1] )
#     rigth_half = list( arr[(len(arr)//2)+1:] )
#     return {'left_half':left_half,'rigth_half':rigth_half}

# def BinarySearch (arr,target):
#     if (len(arr) == 0):
#         return -1
#     elif len(arr)%2 == 0:
#         arr_2 = BinarySearch_even(arr)
#         pass

#     elif len(arr)%2 != 0:
#         arr_2 = BinarySearch_odd(arr)
#         if arr_2['left_half'] == 0:


# def binarySearch (arr,target):
#     index = 0
#     mid = len(arr)//2
#     if mid == target:
#         index = arr.index(target)
#         return index
#     if mid < target:
#         pass

# def binary_search(Array, Search_Term):
#     n = len(Array)
#     L = 0
#     R = n-1
    
#     while L <= R:
#         mid = floor((L+R)/2)
#         if Array[mid] < Search_Term:
#             L = mid + 1
#         elif Array[mid] > Search_Term:
#             R = mid - 1
#         else:
#             return mid
#     return -1

def generate_list_items (size):
    user_list = []
    for i in range(size):
        item = int(input(f'Enter element No-{i+1}: '))
        user_list.append(item)
    return user_list


def binary_search(arr, target):  
    low = 0  
    high = len(arr) - 1  
    mid = 0  
  
    while low <= high:  
        # for get integer result   
        mid = (high + low) // 2  
  
        # Check if target is present at mid   
        if arr[mid] < target:  
            low = mid + 1  
  
        # If target is greater, compare to the right of mid
        elif arr[mid] > target: 
            high = mid - 1  
  
        # If target is smaller, compared to the left of mid
        else:  
            return mid  
  
            # element was not present in the list, return -1  
    return -1  






if __name__ == "__main__":
    lise_size = int(input('Enter the size of your list: '))
    user_list = generate_list_items(lise_size)
    print(f'Here is your list: {user_list}')
    user_target = int(input('Now enter the number that you want to find its index it? '))
    index = binary_search(user_list, user_target)
    if index >= 0:
        print("{} is at index {}".format(user_list[index], index))
    else:
        print("Search term not found")