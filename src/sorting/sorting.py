# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):

    merged_arr = []

    while (len(arrA) + len(arrB)) > 0:
        if len(arrA) == 0:
            merged_arr.append(arrB.pop(0))
        elif len(arrB) == 0:
            merged_arr.append(arrA.pop(0))
        elif arrA[0] < arrB[0]:
            merged_arr.append(arrA.pop(0)) 
        else:
            merged_arr.append(arrB.pop(0))
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr)//2
        arr1 = merge_sort(arr[:middle])
        arr2 = merge_sort(arr[middle:])
        return merge(arr1,arr2)


    #return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here


#def merge_sort_in_place(arr, l, r):
    # Your code here

