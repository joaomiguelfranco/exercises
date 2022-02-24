import math


# Add any extra import statements you may need here


# Add any helper functions you may need here

# arr = [1, 5, 3, 3, 3]
# k = 6

# arr = [1, 3, 3, 3, 5]

def numberOfWays(arr, k):
    arr.sort()
    res = 0
    head = 0
    tail = len(arr) - 1

    while head < tail:
        tmp = arr[head] + arr[tail]
        if tmp == k:
            res += 1
            tail_tmp = tail - 1
            while head < tail_tmp and arr[tail] == arr[tail_tmp]:
                res += 1
                tail_tmp -= 1
            head += 1

        elif tmp < k:
            head += 1
        else:
            tail -= 1

    return res





# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
    print('[', n, ']', sep='', end='')


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
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    k_1 = 6
    arr_1 = [1, 2, 3, 4, 3]
    expected_1 = 2
    output_1 = numberOfWays(arr_1, k_1)
    check(expected_1, output_1)

    k_2 = 6
    arr_2 = [1, 5, 3, 3, 3]
    expected_2 = 4
    output_2 = numberOfWays(arr_2, k_2)
    check(expected_2, output_2)

    # Add your own test cases here
    k = 11
    arr = [10, 12, 10, 15, -1, 7, 6,5, 4, 2, 1, 1, 1]
    expected = 9
    check(expected, numberOfWays(arr, k))

    k = 2
    arr = [1, 1, 1, 1]
    expected = 6
    check(expected, numberOfWays(arr, k))

    k = 6
    arr = [1, 5, 7, -1, 5]
    expected = 3
    check(expected, numberOfWays(arr, k))
