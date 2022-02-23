from copy import copy

# Time  O(n2)
# Space O(1)
def icecreamParlor(m, arr):
    for i in range(0, len(arr)):
        remaining = m - arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] == remaining:
                return [i+1, j+1]
    return None
    # Write your code here

# def icecreamParlor(m, arr):
#     arr.sort()
#     head = 0
#     tail = len(arr)-1
#     while head != tail:
#         if arr[head] + arr[tail] == m:
#             return [map[arr[head]], map[arr[tail]]]
#         if m - arr[head] > arr[tail]: head+=1
#         else: tail -= 1
#
#     if arr[head] + arr[tail] == m:
#         return [map[arr[head]], map[arr[tail]]]
#
#     return None

assert [1,4] == icecreamParlor(6, [1,3,4,5,6])
assert [1,5] == icecreamParlor(6, [1,6,2,4,5])
assert [2,4] == icecreamParlor(6, [6,2,1,4,5])
assert [1,4] == icecreamParlor(4, [1,4,5,3,2])
assert [1,2] == icecreamParlor(4, [2,2,4,3])