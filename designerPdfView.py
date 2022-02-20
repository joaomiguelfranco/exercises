
def calculateMaxHeight(heights, word):
    selectedHeights = [heights[ord(letter)-ord('a')] for letter in word]
    return max(selectedHeights)


def calculateArea(heights, word, wide):
    maxHeight = calculateMaxHeight(heights, word)

    return maxHeight * len(word) * wide

# list of heights indexed by ascii code -> 'a' = 0, 'b' = 1
# should we assume that we have a different list for upper case?

heights = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
wide = 1 # assumption
word = "abc"
expected = 9

assert calculateArea(heights, word, wide) == expected

heights = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
word = "zaba"
expected = 28
assert calculateArea(heights, word, wide) == expected




## example:
##
