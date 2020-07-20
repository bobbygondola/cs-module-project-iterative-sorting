

# go index ++ until we find the target
pos = -1

def linear_search(arr, target):
    # 1. create a loop and counter
    i = 0
    
    # make a while loop
    while i < len(arr):
        if arr[i] == target:
            globals()['pos'] = i
            return arr[i]
        i = i + 1
    
    return -1   # not found



'''
Returns either the index of the target in the arr 
or, if the target isn't in the arr, return -1
 '''

def binary_search(arr, target):
    # 1. compare the target element to the midpoint
        # how do we find mid
            # len()/2 or range(leftmost, rightmost) OR  floor(mid = ( rightmost + leftmost )/2)
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (high + low) // 2
            
    # 2. determine which half to go in, discard other half
        # reassign either left or right index to point to the element past midpoint
        if target == arr[mid]:
            return mid

        if target < arr[mid]:
            high = mid - 1
            
        if target > arr[mid]:
            low = mid + 1
        
    # 3. if halfpoint matches target, SUCCESS, return midpoint index

    # 4. Repeat process: we need to loop this:
        # if low and high are the same element 
            # target isnt in the array, return -1

    return -1  # not found

arr = [3,4,6,16,26,52,55]
print(binary_search(arr, 55))