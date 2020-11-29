def reverse_array(arr):

    reversed_list = arr[::-1]
    arr = reversed_list # not necessary , but just to change the original list
    return arr

print(reverse_array([1,2,3,4,5]))


print('---------------------------------------------------------')

'''
PS
I got this way from a website, but I didn't understand it well
so that, i wrote it here , to save it and study it later
'''

def reverse_array2(arr): 
   arr = [arr[n] for n in range(len(arr)-1,-1,-1)]
   return arr

print(reverse_array2([1,2,3,4,5]))

print('---------------------------------------------------------')

def reverse_array3(arr): 
   for item in range(len(arr)//2): 
      arr[item], arr[len(arr)-1-item] = arr[len(arr)-1-item], arr[item]
   return arr

print(reverse_array3([1,2,3,4,5]))


print('---------------------------------------------------------')

'''
PS
this way is still under progress
even it seems sense for me,I don't know yet why it didn't work !!
'''

# def reverse_array3(arr):
#     print(arr)
#     i = len(arr)
#     for element in range(len(arr)):
#         arr.index(arr[element]) = arr.index(arr[element+i-1])
#         print(arr.index(arr[element]))
#         i -= 1
#         if i < 0 :
#             break
#     return arr

# reverse_array3([1,2,3,4,5])



