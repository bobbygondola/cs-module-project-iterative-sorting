def selection_sort(arr):
    # 1. exterior for loop, which we use to compare neighbors
    for i in range(len(arr) -1):
        lowest = i
        # 2. neighbor for loop
        for j in range(i + 1,len(arr)):
            # 3. compare neighbors if greator
            if arr[j] < arr[lowest]:
                lowest = j
        # 4. swap
        arr[i], arr[lowest] = arr[lowest], arr[i]
    return arr
arr = [5,10,15]
print(selection_sort(arr))

'''BUBBLE SORT'''

def bubble_sort(arr):
    # exterior for loop, through array
    for i in range(len(arr) -1):
        # interior for loop, through array
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
    
    '''first approach'''
    # swaps_occured = True
    # while swaps_occured:
    #     swaps_occured = False
    #     for i in range(0, len(arr)-1):
    #         # compare elements
    #         if arr[i] > arr[i+1]:
    #             # swap elements
    #             arr[i], arr[i+1] = arr[i+1], arr[i]
    #             # if a swap can happen, set swaps_occured to TRUE to run again
    #             swaps_occured = True
    # return arr
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
