def insertShiftArray(arr,value ):
    if (len(arr) == 0):
        arr.append(value)
        return arr
    elif len(arr)%2 == 0:
        first_half = list(  arr[:len(arr)//2] )
        second_half = list( arr[len(arr)//2:] )
        middel_num = [value]
        new_arr = first_half + middel_num+  second_half
        arr = new_arr
        return arr
    else:
        first_half = list(  arr[:(len(arr)//2)+1] )
        second_half = list( arr[(len(arr)//2)+1:] )
        middel_num = [value]
        new_arr = first_half + middel_num+  second_half
        arr = new_arr
        return arr

def generate_list_items (size):
    user_list = []
    for i in range(size):
        item = int(input(f'Enter element No-{i+1}: '))
        user_list.append(item)
    return user_list

if __name__ == "__main__":
    lise_size = int(input('Enter the size of your list: '))
    user_list = generate_list_items(lise_size)
    middel_num = int(input('Enter the value that you want to add it to the center of your list: '))
    result = insertShiftArray(user_list,middel_num)
    print(result)
