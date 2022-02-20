

def rotateArray(array, numRotations):
    pivot = numRotations # index = 4
    res = []
    for elem in array:
        res.append(array[pivot])
        pivot = (pivot + 1) % len(array)

    return res


array = [1, 2, 3, 4, 5]
numRotations = 4
assert rotateArray(array, numRotations) == [5, 1, 2, 3, 4]