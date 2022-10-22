# import requests
# import mysql.connector
# import pandas as pd

"""
We want to talk about altitude maps. One way to think about them is as 2D arrays where at position (i,j) you have an integer representing feet above sea level for latitude=i, longitude=j.

Altitude maps are a great way to represent hilly terrains, especially if we want to understand how to most easily hike on them.
The purpose of this interview is to find out what the “best” path is if we want to move from one point in the map to another.

The first part, to break the ice, is to print an altitude map to the console, one row per line, and space-separated columns - we’ll likely use this method later on.

[[1, 3, 1, 4],
 [4, 0, 2, 0],
 [0, 3, 2, 1],
 [3, 0, 0, 1]]

1 3 1 4
4 0 2 0

--------

Now that we have a way to visualize the map, we can move on the map!
Since we’re moving on the map, we’ll be going through paths.
I’d like to define a useful quantity for a path, namely its elevation gain, that is “the total number of feet climbed uphill (and uphill only) over the path”.

For example, if we were on the top-left corner, walking right until the end of the map, and then down to the bottom-right corner, we’d be traversing:
1 3 1 4 0 1 1 (path)
And its elevation gain would be:
1 3 1 4 0 1 1 (path)
0 <- no step yet
1 3 1 4 0 1 1 (path)
0 2 <- the 1st step is from 1 to 3, so +2 feet uphill
1 3 1 4 0 1 1 (path)
0 2 2 <- the 2nd step is from 3 to 1, downhill, not affecting the elev gain
1 3 1 4 0 1 1 (path)
0 2 2 5 <- 1 to 4 is +3 feet uphill
1 3 1 4 0 1 1 (path)
0 2 2 5 5 <- downhill, no effect
1 3 1 4 0 1 1 (path)
0 2 2 5 5 6 <- 0 to 1 is +1 foot uphill
1 3 1 4 0 1 1 (path)
0 2 2 5 5 6 6 <- 6 is the total elevation gain!

Now that we’re more familiar with elevation gain, we want to do the following:
walk from the top-left to the bottom-right corner of the map
only walk right or down in each position (never left or up)
That means that there are many different paths we could take, each with its own (different!) elevation gain.

Find out what the minimum elevation gain is (only the number of feet, not the path that realized the minimum elevation gain).
 n * n square = O(n ** 2)
"""


def print_altitude_map(arr):
    for row in arr:
        for column in row:
            print(f"{column} ", end='')
        print()


input = [[1, 3, 1, 4],
         [2, 0, 2, 0],
         [0, 3, 2, 1],
         [3, 0, 0, 1]]
[[1]]


# pivot = (i,j)
# i = 0
# j = 0
# (0,0), (0,1), (0,2), (1,2)
# ()
#
def calculate_minimum_elevation_gain(arr, i, j):
    if i == 0 and j == 0:
        return 0

    # i = 3
    # j = 3
    # upper_value = 1
    # left_value = 0
    upper_value = arr[i - 1][j] if i - 1 > 0 else 0
    print(f"(i,j) = ({i},{j})")
    left_value = arr[i][j - 1] if j - 1 > 0 else 0
    cur_value = arr[i][j]

    elevation_up = cur_value - upper_value if upper_value < cur_value else 0
    elevation_left = (cur_value - left_value) if left_value < cur_value else 0

    # max(elevation_left, elevation_up)

    # if j - 1 > 0
    #     left_value =

    # elevation_gain_up = cur_

    min_elevation_up_to_upper = calculate_minimum_elevation_gain(arr, i - 1, j) if i - 1 >= 0 else float("inf")
    min_elevation_up_to_left = calculate_minimum_elevation_gain(arr, i, j - 1) if j - 1 >= 0 else float("inf")
    return min(min_elevation_up_to_upper + elevation_up, min_elevation_up_to_left + elevation_left)


print_altitude_map(input)
print(calculate_minimum_elevation_gain(input, 3, 3))



