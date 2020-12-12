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
