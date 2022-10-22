import pytest


# Game of Life
#
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
#
# It’s a simple 2-dimensional automata where each cell can be either alive or dead.
# Each “clock tick” updates the live/dead status of each cell based on the following rules:
#
#  - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
#  - Any live cell with two or three live neighbors lives on to the next generation.
#  - Any live cell with more than three live neighbors dies, as if by overpopulation.
#  - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

# live - 1
# dead - 0

# input
#  1 0 1
#  0 1 0
#  1 0 0

# output
# 0 1 0
# 1 0 0
# 0 0 0


def calculate_live_neighbours(input, index_row, index_column):
    upper_row_exist = index_row - 1 >= 0
    down_row_exist = index_row + 1 < len(input)
    left_cell_exist = index_column - 1 >= 0
    right_cell_exist = index_column + 1 < len(input[index_row])

    def get_number_of_direct_neighbours():
        upper_neighbour = input[index_row - 1][index_column] if upper_row_exist else 0
        down_neighbour = input[index_row + 1][index_column] if down_row_exist else 0
        left_neighbour = input[index_row][index_column - 1] if left_cell_exist else 0
        right_neighbour = input[index_row][index_column + 1] if right_cell_exist else 0
        return upper_neighbour + down_neighbour + left_neighbour + right_neighbour

    def get_number_of_diagonal_neighbours():
        upper_left_neighbour = input[index_row - 1][index_column - 1] if upper_row_exist and left_cell_exist else 0
        upper_right_neighbour = input[index_row - 1][index_column + 1] if upper_row_exist and right_cell_exist else 0
        down_left_neighbour = input[index_row + 1][index_column - 1] if down_row_exist and left_cell_exist else 0
        down_right_neighbour = input[index_row + 1][index_column + 1] if down_row_exist and right_cell_exist else 0
        return upper_left_neighbour + upper_right_neighbour + down_left_neighbour + down_right_neighbour

    return get_number_of_diagonal_neighbours() + get_number_of_direct_neighbours()


def apply_rules(input, index_row, index_column):
    live_cell = input[index_row][index_column] == 1
    dead_cell = not live_cell
    number_of_live_neighbours = calculate_live_neighbours(input, index_row, index_column)

    if live_cell and number_of_live_neighbours < 2: return 0
    if live_cell and number_of_live_neighbours in (2, 3): return 1
    if live_cell and number_of_live_neighbours > 3: return 0
    if dead_cell and number_of_live_neighbours == 3: return 1

    return input[index_row][index_column]


def update(input):
    res = []
    for index_row in range(0, len(input)):
        res_row = []
        for index_cell in range(0, len(input[index_row])):
            result_of_rule = apply_rules(input, index_row, index_cell)
            res_row.append(result_of_rule)
        res.append(res_row)
    return res


def test_calculate_live_neighbours_with_all_live_neighbours():
    input = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    index_row = 1
    index_cell = 1
    res = calculate_live_neighbours(input, index_row, index_cell)
    assert res == 4


def test_calculate_live_neighbours_with_down_neighbour_live():
    input = [[1, 0, 1], [0, 0, 1], [1, 0, 0]]
    index_row = 0
    index_cell = 2
    res = calculate_live_neighbours(input, index_row, index_cell)
    assert res == 1


def test_calculate_live_neighbours_with_down_neighbour_live_out_of_bounds():
    input = [[1, 0, 0], [0, 0, 0], [1, 0, 1]]
    index_row = 2
    index_cell = 2
    res = calculate_live_neighbours(input, index_row, index_cell)
    assert res == 0


def test_calculate_live_neighbours_with_upper_neighbour_out_of_bounds():
    input = [[1, 0, 1],
             [0, 1, 0],
             [1, 0, 0]]
    index_row = 0
    index_cell = 0
    res = calculate_live_neighbours(input, index_row, index_cell)
    assert res == 1


def test_calculate_live_neighbours_with_upper_neighbour_dead():
    input = [[1, 0, 1],
             [0, 1, 0],
             [1, 0, 0]]
    index_row = 2
    index_cell = 2
    res = calculate_live_neighbours(input, index_row, index_cell)
    assert res == 1


def test_calculate_live_neighbours_with_upper_neighbour_live():
    input = [[1, 0, 1], [0, 0, 1], [1, 0, 0]]
    index_row = 1
    index_cell = 2
    res = calculate_live_neighbours(input, index_row, index_cell)
    assert res == 1


def test_apply_rules_with_live_cell_with_fewer_than_2_live_neighbours():
    input = [[1, 0, 1], [0, 1, 0], [1, 0, 0]]
    index_row = 0
    index_cell = 0
    res = apply_rules(input, index_row, index_cell)
    assert res == 0


def test_apply_rules_with_live_cell_with_two_live_neighbors():
    #  - Any live cell with two or three live neighbors lives on to the next generation.
    input = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
    index_row = 1
    index_cell = 0
    res = apply_rules(input, index_row, index_cell)
    assert res == 1


def test_apply_rules_with_live_cell_with_three_live_neighbors():
    #  - Any live cell with two or three live neighbors lives on to the next generation.
    input = [[1, 0, 0],
             [1, 1, 0],
             [1, 0, 0]]
    index_row = 1
    index_cell = 0
    res = apply_rules(input, index_row, index_cell)
    assert res == 1


def test_apply_rules_with_live_cell_with_three_diagonal_live_neighbors():
    input = [[0, 1, 0],
             [0, 1, 0],
             [0, 1, 0]]
    index_row = 1
    index_cell = 0
    res = apply_rules(input, index_row, index_cell)
    assert res == 1


def test_apply_rules_with_live_cell_with_four_live_neighbors():
    #  - Any live cell with more than three live neighbors dies, as if by overpopulation.
    input = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    index_row = 1
    index_cell = 1
    res = apply_rules(input, index_row, index_cell)
    assert res == 0


def test_apply_rules_with_dead_cell_with_three_live_neighbors():
    #  - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    input = [[0, 1, 0], [1, 0, 0], [0, 1, 0]]
    index_row = 1
    index_cell = 1
    res = apply_rules(input, index_row, index_cell)
    assert res == 1


def test_apply_rules_with_dead_cell_with_three_live_neighbors_for_the_original_input(
):
    #  - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    input = [[1, 0, 1], [0, 1, 0], [1, 0, 0]]

    index_row = 0
    index_cell = 1
    res = apply_rules(input, index_row, index_cell)
    assert res == 1


def test_apply_rules_with_dead_cell_with_four_live_neighbors():
    #  - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    input = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    index_row = 1
    index_cell = 1
    res = apply_rules(input, index_row, index_cell)
    assert res == 0


def test_update_with_small_sample():
    input = [[1, 0, 1],
             [0, 1, 0],
             [1, 0, 0]]
    actual = update(input)
    expected = [[0, 1, 0],
                [1, 1, 0],
                [0, 0, 0]]
    assert actual == expected


# Blinker: [ [0,1,0], [0,1,0], [0,1,0] ]
# Alternates between a vertical line and horizontal line
def test_blinker():
    iteration1 = [[0, 1, 0],
                  [0, 1, 0],
                  [0, 1, 0]]
    iteration2 = update(iteration1)
    iteration3 = update(iteration2)

    assert iteration3 == iteration1


# Beacon: [ [1,1,0,0], [1,1,0,0], [0,0,1,1], [0,0,1,1] ]
# Two 2x2 squares touching on the corners. The touching corners for each square alternate between live and dead.
def test_beacon():
    iteration1 = [[1, 1, 0, 0],
                  [1, 1, 0, 0],
                  [0, 0, 1, 1],
                  [0, 0, 1, 1]]

    iteration2 = update(iteration1)
    iteration3 = update(iteration2)
    assert iteration3 == iteration1


# Glider: [ [0,1,0], [0,0,1], [1,1,1] ]
# This will move down and to the right in the matrix.
def test_glider():
    iteration1 = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]
    iteration2 = update(iteration1)
    expected = [[0, 0, 0], [1, 0, 1], [0, 1, 1]]
    assert iteration2 == expected
