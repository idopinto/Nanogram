from nonogram import *

def test_():
    assert constraint_satisfactions(3,[1]) == sorted([[1,0,0], [0,1,0], [0,0,1]])
    assert constraint_satisfactions(3, [2]) == sorted([[1,1,0], [0,1,1]])
    assert constraint_satisfactions(3, [1,1]) == sorted([[1,0,1]])
    assert constraint_satisfactions(4, [1,1]) == sorted([[1,0,1,0], [0,1,0,1], [1,0,0,1]])
    assert constraint_satisfactions(5, [2,1]) == sorted([[1,1,0,1,0], [1,1,0,0,1], [0,1,1,0,1]])
    assert constraint_satisfactions(10, [10]) == [[1,1,1,1,1,1,1,1,1,1,]]
    assert constraint_satisfactions(10,[11]) == []
    assert constraint_satisfactions(3, [1,2]) == []
    assert constraint_satisfactions(10, [5,2,1]) == [[1,1,1,1,1,0,1,1,0,1]]

def test_row_variation():
    assert row_variations([1, 1, -1, 0], [3]) == [[1, 1, 1, 0]]
    assert row_variations([-1, -1, -1, 0], [2]) == sorted([[0, 1, 1, 0], [1, 1, 0, 0]])
    assert row_variations([-1, 0, 1, 0, -1, 0], [1, 1]) == sorted([[0, 0, 1, 0, 1, 0], [1, 0, 1, 0, 0, 0]])
    assert row_variations([-1, -1, -1] , [1]) == sorted([[1, 0, 0], [0, 1, 0], [0, 0, 1] ])
    assert row_variations([0, 0, 0], [1]) == []
    assert row_variations([0, 0, -1, 1, 0], [3]) == []
    assert row_variations([0, 0, -1, 1, 0] , [2]) == [[0, 0, 1, 1, 0]]
    assert row_variations([0, 0, 1, 1, 0], [2]) == [[0, 0, 1, 1, 0]]


    # assert constraint_satisfactions(4, [1,1]) == sorted([[1,0,1,0], [0,1,0,1], [1,0,0,1]])
    # assert constraint_satisfactions(5, [2,1]) == sorted([[1,1,0,1,0], [1,1,0,0,1], [0,1,1,0,1]])
    # assert constraint_satisfactions(10, [10]) == [[1,1,1,1,1,1,1,1,1,1,]]
    # assert constraint_satisfactions(10,[11]) == []
    # assert constraint_satisfactions(3, [1,2]) == []
    # assert constraint_satisfactions(10, [5,2,1]) == [[1,1,1,1,1,0,1,1,0,1]]
