"""
Quicksort uses partition
#[3, 1, 5, 2]
1. chooses a pivot -> '2'
2. partition array based on pivot
3. quicksort left array on the pivot
4. quicksort right array on the pivot

"""
def swap(arr, low, high):
    tmp = arr[low]
    arr[low] = arr[high]
    arr[high] = tmp

def partition(array):
    left = []
    right = []
    pivot = array[0]
    for i in array[1:]:
        if i > pivot:
            right.append(i)
        else: left.append(i)
    return left, pivot, right

def print_stage(res):
    for i in res: print(f"{i} ", end="")
    print()

def quicksort(array):
    if len(array) <= 1:
        return array

    left,pivot,right = partition(array)
    left = quicksort(left)
    right = quicksort(right)

    res = left + [pivot] + right
    print_stage(res)
    return res




a = [5, 8, 1, 3, 7, 9, 2]
quicksort(a)
#
# a = [1,-2,7,1,8,2,7]
# quicksort(a, 0, len(a)-1)
# assert [-2, 1, 1, 2, 7, 7, 8] == a



