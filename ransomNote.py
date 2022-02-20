#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def convertListToDictionary(list):
    dic = {}
    for elem in list:
        if elem in dic:
            dic[elem] += 1
        else: dic[elem] = 1
    return dic

def checkMagazine(magazine, note):
    dic = convertListToDictionary(magazine)

    for curNote in note:
        if curNote not in dic: return "No"
        if dic[curNote] == 0: return "No"

        dic[curNote] -= 1

    return "Yes"

if __name__ == '__main__':
    magazine = "two times three is not four".split()
    notes = "two times two is four".split()
    assert checkMagazine(magazine, notes) == "No"

    magazine = "give me one grand today night".split()
    notes = "give one grand today".split()
    assert checkMagazine(magazine, notes) == "Yes"

    magazine = "ive got a lovely bunch of coconuts".split()
    notes = "ive got some coconuts".split()
    assert checkMagazine(magazine, notes) == "No"