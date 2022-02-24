import math


# Add any extra import statements you may need here


# Add any helper functions you may need here


def isNum(c):
    return ord('0') <= ord(c) <= ord('9')


def isUpperCase(c):
    return ord('A') <= ord(c) <= ord('Z')


def rotate(c, rotation_factor, ascii_min, ascii_max):
    rotation_factor = rotation_factor % (ascii_max + 1 - ascii_min)
    rotated = ord(c) + rotation_factor
    if rotated > ascii_max:
        rotated = (rotated % ascii_max) + ascii_min - 1
    return chr(rotated)

def isLowerCase(c):
    return ord('a') <= ord(c) <= ord('z')


def rotationalCipher(input, rotation_factor):
    # Write your code here
    # iterate over char in input
    # check if numeric
    # yes, rotate the number using 'mod' or '%'
    # check if lowercase alphabetic
    # check if uppercase alphabetic
    # append tor res

    # input = [Zebra-493?]
    # rotation_factor = 3
    # c = Z

    res = ""
    for c in input:
        if isNum(c):
            res += rotate(c, rotation_factor, ord('0'), ord('9'))
        elif isUpperCase(c):
            res += rotate(c, rotation_factor, ord('A'), ord('Z'))
        elif isLowerCase(c):
            res += rotate(c, rotation_factor, ord('a'), ord('z'))
        else:
            res += c

    return res


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
    input_1 = "All-convoYs-9-be:Alert1."
    rotation_factor_1 = 4
    expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
    output_1 = rotationalCipher(input_1, rotation_factor_1)
    check(expected_1, output_1)

    input_2 = "abcdZXYzxy-999.@"
    rotation_factor_2 = 200
    expected_2 = "stuvRPQrpq-999.@"
    output_2 = rotationalCipher(input_2, rotation_factor_2)
    check(expected_2, output_2)

    # Add your own test cases here
