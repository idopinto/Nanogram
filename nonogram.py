BLACK = 1
X = 0
UNKNOWN = -1

import ex8_helper


def constraint_satisfactions(n, blocks):
    solution_base = [(-1) for i in range(n)]

    solution_array = []
    _helper_constraint_satisfactions(solution_base, 0, blocks, 0, solution_array)
    return solution_array


def _helper_constraint_satisfactions(current_array, ind_arr, blocks, ind_b, solution_array):
    current_array_copy = current_array[:]
    # base base
    if ind_b >= len(blocks):
        # if we finished the blocks array put zeros and append to sol list and return
        for j in range(ind_arr, len(current_array_copy)):
            current_array_copy[j] = 0
        solution_array.append(current_array_copy)
        return
    elif ind_arr >= len(current_array_copy):
        # if we passed the current_array length it means the current solution is not good
        return

    else:
        current_array_copy[ind_arr] = 0
        _helper_constraint_satisfactions(current_array_copy, ind_arr + 1, blocks, ind_b, solution_array)
        if blocks[ind_b] > len(current_array_copy) - ind_arr:
            return
        else:
            for j in range(ind_arr, blocks[ind_b] + ind_arr):
                current_array_copy[j] = 1
            if ind_arr + blocks[ind_b] < len(current_array_copy):
                current_array_copy[ind_arr + blocks[ind_b]] = 0
            _helper_constraint_satisfactions(current_array_copy, ind_arr + blocks[ind_b] + 1, blocks, ind_b + 1,
                                             solution_array)


def row_variations(row, blocks):
    solution = []
    _helper_row_variations(row, 0, blocks, [], solution)
    return solution

def _helper_row_variations(row, ind_row, blocks, suspect, solution_array):

    if len(suspect) == len(row) and is_valid_row(suspect, blocks):
        suspect_copy = suspect[:]
        solution_array.append(suspect_copy)
        return

    if ind_row >= len(row):
        return

    if row[ind_row] == 0 or row[ind_row] == 1:
        suspect.append(row[ind_row])
        _helper_row_variations(row, ind_row + 1, blocks, suspect, solution_array)
        suspect.pop()
        return

    if row[ind_row] == -1:
        for option in [0, 1]:
            suspect.append(option)
            _helper_row_variations(row, ind_row + 1, blocks, suspect, solution_array)
            suspect.pop()
        return


def is_valid_row(row, blocks):
    """this function gets suspect for valid row and return true or false"""
    str_row = ""
    for i in range(len(row)):
        str_row += str(row[i])
    str_row_no_zero = str_row.split("0")
    index = 0

    for block in str_row_no_zero:
        if block == "":
            continue
        elif index < len(blocks):
            if block.count("1") == blocks[index]:
                index += 1
            else:
                return False
        else:
            return False
    return len(blocks) == index
