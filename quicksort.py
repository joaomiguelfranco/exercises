"""
Technically, quick sort follows the below steps:
    1 − Make any element as pivot
    2 − Partition the array on the basis of pivot
    3 − Apply quick sort on left partition recursively
    4 − Apply quick sort on right partition recursively
"""

def swap(arr, low, high):
    tmp = arr[low]
    arr[low] = arr[high]
    arr[high] = tmp

def partition(array, low, high):
    pivot = array[high]
    smaller = low
    for j in range(low, high):
        if array[j] < pivot:
            swap(array, smaller, j)
            smaller += 1
    swap(array, smaller, high)
    return smaller

def quicksort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)
    return array

array = [5,1,2,7,234,0,-1,8]
assert [-1, 0, 1, 2, 5, 7, 8, 234] == quicksort(array, 0, len(array)-1)

array = [50, 23, 9, 18, 61, 32]
assert [9, 18, 23, 32, 50, 61] == quicksort(array, 0, len(array) - 1)

array = [1, 2, 3, 18, 32]
assert [1, 2, 3, 18, 32] == quicksort(array, 0, len(array)-1)
