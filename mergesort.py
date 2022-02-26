"""
MergeSort
 1. Find the middle point to divide the array into two halves:
         middle m = l + (r-l)/2
 2. Call mergeSort for first half:
         Call mergeSort(arr, l, m)
 3. Call mergeSort for second half:
         Call mergeSort(arr, m+1, r)
 4. Merge the two halves sorted in step 2 and 3:
"""

def merge(left, right):
    i_left = 0
    i_right = 0
    res = []

    while i_left < len(left) and i_right < len(right):
        if left[i_left] > right[i_right]:
            res.append(right[i_right])
            i_right += 1
        else:
            res.append(left[i_left])
            i_left += 1
    if i_left < len(left):
        res.extend(left[i_left:])
    elif i_right < len(right):
        res.extend(right[i_right:])

    return res


def mergesort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left = mergesort(array[:middle])
        right = mergesort(array[middle:])
        array = merge(left, right)
    return array

array = [3,5,2,1]
assert [1, 2, 3, 5] == mergesort(array)

array = [38, 27, 43, 3, 9, 82, 10]
assert [3, 9, 10, 27, 38, 43, 82] == mergesort(array)