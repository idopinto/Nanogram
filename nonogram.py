BLACK = 1
X = 0
UNKNOWN = -1
import numpy
import matplotlib.pyplot as plt
import time

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# ~~~~~~~~~~~~~~~~~PART I~~~~~~~~~~~~~~~~#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def constraint_satisfactions(n, blocks):
    solution_base = [UNKNOWN for i in range(n)]

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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# ~~~~~~~~~~~~~~~~~PART II~~~~~~~~~~~~~~~#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def row_variations(row, blocks):
    solution_array = []
    _helper_row_variations(row, 0, blocks, 0, solution_array)
    return solution_array


def _helper_row_variations(row, ind_row, blocks, ind_b, solution_array):
    if ind_b >= len(blocks):
        for i in range(ind_row, len(row)):
            if row[i] == -1:
                row[i] = 0
            if row[i] == 1:
                return
        solution_array.append(row)
        return

    elif ind_row >= len(row):
        return
    row_copy = row[:]
    if row_copy[ind_row] == 0:
        _helper_row_variations(row_copy, ind_row + 1, blocks, ind_b, solution_array)
    if row_copy[ind_row] == 1:
        if try_to_put_block(row_copy, ind_row, blocks[ind_b]):
            _helper_row_variations(row_copy, ind_row + blocks[ind_b], blocks, ind_b + 1, solution_array)
        else:
            return
    if row_copy[ind_row] == -1:
        row_copy[ind_row] = 0
        _helper_row_variations(row_copy, ind_row + 1, blocks, ind_b, solution_array)
        row_copy[ind_row] = 1
        if try_to_put_block(row_copy, ind_row, blocks[ind_b]):
            _helper_row_variations(row_copy, ind_row + blocks[ind_b], blocks, ind_b + 1, solution_array)
        else:
            return
        #fasdg


def try_to_put_block(row, index_row, block_size):
    for j in range(index_row, index_row + block_size):
        if j >= len(row):
            return False
        if row[j] == 0:
            return False
        elif row[j] == -1:
            row[j] = 1
    if index_row + block_size == len(row):
        return True
    elif row[index_row + block_size] == 1:
        return False
    elif row[index_row + block_size] == -1:
        row[index_row + block_size] = 0
    return True


def intersection_row(rows):
    row_option = []
    rows_organized = [list(x) for x in zip(*rows)]
    for row in rows_organized:
        if row.count(X) == len(row):
            row_option.append(X)
        elif row.count(BLACK) == len(row):
            row_option.append(BLACK)
        else:
            row_option.append(UNKNOWN)

    return row_option

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# ~~~~~~~~~~~~~~~~~PART III~~~~~~~~~~~~~~#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


def solve_easy_nonogram(constraints):
    board = get_board(constraints)
    board = _helper_solve_easy_nonogram(board, constraints)
    return board


def _helper_solve_easy_nonogram(board, constraints):
    if not board:
        return None

    changed = True
    while changed:
        changed = False
        for i in range(len(board)):
            row_copy = board[i][:]
            board, new_row = update_board_row(i, board, constraints[0][i])
            changed = changed or (row_copy != new_row)
        for j in range(len(board[0])):
            col_copy = [x[j] for x in board]
            board, new_col = update_board_col(j, board, constraints[1][j])
            changed = changed or (col_copy != new_col)
    return board

    # TODO what is means contridiction and how to implement it


def update_board_row(row_index, board, constraint):
    if UNKNOWN not in board[row_index]:
        return board, board[row_index]
    else:
        row_variation = row_variations(board[row_index], constraint)
        board[row_index] = intersection_row(row_variation)
    return board, board[row_index]


def update_board_col(col_index, board, constraint):
    cols_matrix = [list(x) for x in zip(*board)]
    if UNKNOWN not in cols_matrix[col_index]:
        board = [list(x) for x in zip(*cols_matrix)]
        return board, cols_matrix[col_index]
    else:
        cols_matrix[col_index] = intersection_row(row_variations(cols_matrix[col_index], constraint))
    board = [list(x) for x in zip(*cols_matrix)]

    return board, cols_matrix[col_index]


def get_board(constraints):
    board = [[-1] * len(constraints[1])] * len(constraints[0])

    return board


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# ~~~~~~~~~~~~~~~~~PART IV~~~~~~~~~~~~~~~#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def _helper_solve_nonogram():
    pass

# def solve_nonogram(constraints):
#
#     solved = False
#     results = []
#     while not solved:
#         result = solve_easy_nonogram(constraints)
#
#         results.append(result)










start = time.time()
testing = [[[1, 1, 1, 1, 2, 1, 1, 1, 1], [2], [1, 1, 1, 1, 2, 1, 1, 1, 1],
       [1, 1, 1, 6, 1, 1, 1], [1, 1, 1, 2, 1, 1, 1],
       [1, 1, 10, 1, 1],
       [1, 1, 2, 1, 1], [1, 14, 1], [1, 2, 1], [18], [2], [1, 2],
       [5, 2, 1], [3, 4, 5], [1, 6, 3], [8, 1]],
      [[1, 8, 1], [1, 2], [1, 6, 1, 4], [1, 1, 2], [1, 4, 1, 1, 1],
       [1, 1, 1, 1], [1, 2, 1, 1, 1, 2], [1, 1, 1, 1, 3], [16], [16],
       [1, 1, 1, 1, 3], [1, 2, 1, 1, 1, 2], [1, 1, 1, 1],
       [1, 4, 1, 1, 1], [1, 1, 2], [1, 6, 1, 4], [1, 2], [1, 8, 1]]]
test_board = solve_easy_nonogram(testing)

# Unknown cells will be painted in grey,
# Filled cells in black and empty cells in white
for row in test_board:
    for col_idx in range(0, len(row)):
        if row[col_idx] == -1:
            row[col_idx] = 1
        elif row[col_idx] == 1:
            row[col_idx] = 3

arr = numpy.array([numpy.array(row) for row in test_board])
plt.matshow(arr, cmap='Greys')
plt.show()
end = time.time()
print(end - start)

