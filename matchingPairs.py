import math


# Add any extra import statements you may need here


# Add any helper functions you may need here

# s = 'abcd'
# t = 'adcb'
def matching_pairs(s, t):
    if s == t: return len(s) - 2 # required swaps

    # Write your code here
    matching_pairs = 0
    s_non_matching = set()
    t_non_matching = set()
    s_partial_swap = False
    t_partial_swap = False
    # Time Complexity : O(n)
    # Space Complexity: O(1) worst case of unmatched chars
    for i in range(0, len(s)):

        if s[i] == t[i]:
            matching_pairs += 1
        elif not s_partial_swap and not t_partial_swap:
            if not s_partial_swap and s[i] in t_non_matching:
                matching_pairs += 1
                t_non_matching.remove(s[i])
                s_partial_swap = True
            if not t_partial_swap and t[i] in s_non_matching:
                matching_pairs += 1
                s_non_matching.remove(t[i])
                t_partial_swap = True
            else:
                s_non_matching.add(s[i])
                t_non_matching.add(t[i])

    return matching_pairs



# Write your code here


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
    s_1, t_1 = "abcde", "adcbe"
    expected_1 = 5
    output_1 = matching_pairs(s_1, t_1)
    check(expected_1, output_1)

    s_2, t_2 = "abcd", "abcd"
    expected_2 = 2
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

    # Add your own test cases here
    s,t = "mno", "mno"
    expected = 1
    output = matching_pairs(s,t)
    check(expected, output)

    s, t = "mnogra", "mnorga"
    expected = 6
    output = matching_pairs(s, t)
    check(expected, output)

    s, t = "mnogra", "mnorpa"
    expected = 5
    output = matching_pairs(s, t)
    check(expected, output)

    s, t = "asdasdsa", "asdadsad"
    expected = 6
    output = matching_pairs(s, t)
    check(expected, output)

    s, t = "abxce", "abcdx"
    expected = 3
    output = matching_pairs(s, t)
    check(expected, output)


