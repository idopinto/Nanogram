BLACK = 1
X = 0
UNKNOWN = -1
import numpy
import matplotlib.pyplot as plt


# TODO מתי אפשר לפסול ומתי אפשר לגמור בשיר מזמור
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


def intersection_row(rows):
    """
    """
    intersection = []
    # [[0, 0, 1], [0, 1, 1], [0, 0, 1]]) -> [0, -1, 1]
    if len(rows) > 0:
        for i in range(len(rows[0])):
            temp_cell = rows[0][i]
            if temp_cell != UNKNOWN:
                for j in range(1, len(rows)):
                    if rows[j][i] != temp_cell:
                        temp_cell = UNKNOWN
                        break
            intersection.append(temp_cell)
    return intersection


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


def solve_easy_nonogram(constraints):
    board = get_board(constraints)
    _helper_solve_easy_nonogram(board, constraints)
    return board


def _helper_solve_easy_nonogram(board, constraints):
    if not board:
        return None

    temp_board = board[:]
    for i in range(len(board)):
        # row_copy = board[i][:]
        board[:] = update_board_row(i, board, constraints[0][i])
    for j in range(len(board[0])):
        board[:] = update_board_col(j, board, constraints[1][j])

    if temp_board != board:
        _helper_solve_easy_nonogram(board, constraints)
    else:
        return None

    # TODO


#
# def _helper_solve_easy_nonogram(board,constraints,ind_row,ind_col):
#
#     if not board:
#         return None
#
#     temp_board = board[:]
#
#     board[:] = update_board_row(ind_row , board,constraints[0][ind_row])
#     board[:] = update_board_col(ind_col, board, constraints[1][ind_col])
#     if temp_board != board:
#         _helper_solve_easy_nonogram(temp_board, constraints,ind_row+1,ind_col)
#         _helper_solve_easy_nonogram(temp_board, constraints,ind_row,ind_col+1)
#     else:
#         return None


def update_board_row(row_index, board, constraint):
    if UNKNOWN not in board[row_index]:
        return board
    #
    # count = board[row_index].count(UNKNOWN)
    # if count > constraint[0] * 2:
    #     return board

    else:
        row_variation = row_variations(board[row_index], constraint)
        board[row_index] = intersection_row(row_variation)
    return board


def update_board_col(col_index, board, constraint):
    cols_matrix = [list(x) for x in zip(*board)]
    if UNKNOWN not in cols_matrix[col_index]:
        board = [list(x) for x in zip(*cols_matrix)]
        return board
    else:
        cols_matrix[col_index] = intersection_row(row_variations(cols_matrix[col_index], constraint))
    board = [list(x) for x in zip(*cols_matrix)]

    return board


def get_board(constraints):
    board = [[-1] * len(constraints[1])] * len(constraints[0])

    return board


my_constraints = [[[3], [5], [5], [3], [1], [1], [1, 1]], [[2, 1], [4], [7], [4], [2]]]
my_constraints_2 = [[[1, 3, 3], [3, 1, 2], [1, 3], [2, 1], [1, 2], [2, 1], [1, 3], [4, 1, 2], [1, 3, 3]],
                    [[1, 1, 3], [1, 1], [3, 3], [3, 3], [1, 1, 1, 1], [1, 1, 1], [1, 1], [1, 3, 1], [2, 1, 2],
                     [2, 1, 1, 2]]]
my_constraint_4 = [[[5, 2], [1, 1, 4], [1, 2, 3, 2], [4, 1, 3, 3, 2], [1, 2, 3, 5], [4, 4], [7]],
                   [[4], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [4], [1, 3], [1, 1, 2], [2, 2, 1], [2, 2, 1],
                    [2, 1, 1], [1, 2], [5], [3], [3], [1], [2], [2], [1]]]
my_constraints_3 = [
    [[2], [2, 1], [1, 3], [1, 1, 1, 1], [1, 1, 5], [1, 1, 1, 1, 1, 1], [1, 1, 1, 2, 1], [1, 1, 1, 1], [1, 1, 4, 3],
     [4, 3, 2], [1, 1, 1, 1, 1], [7, 2, 1], [1, 1, 1, 1, 3], [1, 1, 1, 1, 1, 1],
     [1, 1, 5, 3],
     [1, 1, 5, 1, 1], [1, 1, 2, 2, 1, 1],
     [1, 1, 2, 2, 1, 1], [1, 1, 1, 1, 5],
     [1, 1, 2, 2, 1, 1]],
    [[1, 2], [6, 9], [1, 1], [16], [1, 1, 1],
     [1, 7, 1],
     [2, 1, 2, 6], [2, 2, 2], [1, 2, 2, 6],
     [1, 1, 1, 1, 6, 1], [2, 3, 2, 1, 1],
     [1, 1, 1, 2, 10], [4, 2, 2, 1, 1, 1], [11],
     [1]]]

temp = [[[1, 1], [2, 1], [4, 1], [6, 1], [1, 4], [9], [3, 3], [1, 4], [3], [5], [5], [6], [5], [4], [6], [2, 3], [3, 1],
         [2, 2], [4, 1], [2, 2], [5], [3]],
        [[1], [3, 3], [4, 5], [2, 1, 4, 2, 2], [6, 7, 1, 2], [5, 9, 2], [1, 13, 4], [1, 10, 2], [1, 7, 3],
         [1, 1, 1, 1, 1]]]

# TODO: Put solution board in `board` variable
board = solve_easy_nonogram(my_constraints_3)

# Unknown cells will be painted in grey,
# Filled cells in black and empty cells in white
for row in board:
    for col_idx in range(0, len(row)):
        if row[col_idx] == -1:
            row[col_idx] = 1
        elif row[col_idx] == 1:
            row[col_idx] = 3

arr = numpy.array([numpy.array(row) for row in board])
plt.matshow(arr, cmap='Greys')
plt.show()
