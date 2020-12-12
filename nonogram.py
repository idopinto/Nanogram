BLACK = 1
X = 0
UNKNOWN = -1
import copy


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
    solution_array = []
    _helper_row_variations(row, 0, blocks, 0, solution_array)
    return solution_array

def _helper_row_variations(row, ind_row, blocks, ind_b, solution_array):
    row_copy = row[:]
    if ind_b >= len(blocks):
        for j in range(ind_row, len(row_copy)):
            #if row_copy[j] == -1:
                row_copy[j] = 0
        solution_array.append(row_copy)
        return
    elif ind_row >= len(row_copy):
        return
    else:
        if row_copy[ind_row] == -1:
            row_copy[ind_row] = 0
        _helper_row_variations(row_copy, ind_row + 1, blocks, ind_b, solution_array)
        if blocks[ind_b] > len(row_copy) - ind_row:
            return
        else:
            if row_copy[ind_row] == 1 and is_valid_row(row_copy,ind_row, blocks[ind_b]):
                # [1,1,-1,0], [0]->3 : [1,-1,0],2:[-1,0]: 1
                for j in range(ind_row, blocks[ind_b] + ind_row):
                    row_copy[j] = 1
            if ind_row + blocks[ind_b] < len(row_copy):
                row_copy[ind_row + blocks[ind_b]] = 0
            _helper_row_variations(row_copy, ind_row + blocks[ind_b] + 1, blocks, ind_b + 1, solution_array)



def is_valid_row(row,ind_row, block):
    if block == 0:
        return True
    for i in range(len(row)):
        if row[i] == 0:
            return False
    is_valid_row(row[ind_row:],ind_row+1,block-1)


print(row_variations([1,1,-1,0],[3]))