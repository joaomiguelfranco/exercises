

[3,2,4,5]
# head = 0
# pivot = head + 1
# multiplication = 0
# iterate from head to len(array)

# i = 3
# j = 2 - 4 - 5
# analyzedNumbers = {2:6, 4:8, 5:15}
# i = 2
# analyzedNumbers = {2:6, 4:{12,8,24}, 5:{15,10,30}}
# i = 4
# analyzedNumbers = {2:6, 4:{12,8,24}, 5:{15,10,30,20,60,40,120}}
def splitNumberIntoHash(num):
    l = {}
    while num % 10 != 0:
        n = num % 10
        num -= n
        num /= 10
        l[n] = set({})
    return l

def isColorful(num):

    analyzedNumbers = splitNumberIntoHash(num)
    keyList = list(analyzedNumbers.keys())
    for i in range(0, len(keyList)):
        for j in range(i+1, len(keyList)):
            for val in list(analyzedNumbers[keyList[j]]):
                if keyList[i] * val in analyzedNumbers.values():
                    return False
                analyzedNumbers[keyList[j]].add(keyList[i] * val)
            if keyList[i] * keyList[j] in analyzedNumbers.values() or keyList[i] * keyList[j] in analyzedNumbers.keys():
                return False
            analyzedNumbers[keyList[j]].add(keyList[i] * keyList[j])
    return True

num = 3245
assert isColorful(num)

num = 326
assert not isColorful(num)
