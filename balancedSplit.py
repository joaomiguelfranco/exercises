import math


# Add any extra import statements you may need here


# Add any helper functions you may need here


def balancedSplitExists(arr):
    arr.sort()  # O(nlogn)

    for i in range(0, len(arr) - 1):
        a = arr[0:i + 1]
        b = arr[i + 1:]
        if a[i] == b[0]:
            continue
        if sum(a) == sum(b):
            return True
    return False


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
    print('[\"', string, '\"]', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    arr_1 = [2, 1, 2, 5]
    expected_1 = True
    output_1 = balancedSplitExists(arr_1)
    check(expected_1, output_1)

    arr_2 = [3, 6, 3, 4, 4]
    expected_2 = False
    output_2 = balancedSplitExists(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
    array = [1, 5, 7, 1]
    expected = True
    output = balancedSplitExists(array)
    check(expected, output)

    array = [12, 7, 6, 7, 6]
    expected = False
    output = balancedSplitExists(array)
    check(expected, output)
