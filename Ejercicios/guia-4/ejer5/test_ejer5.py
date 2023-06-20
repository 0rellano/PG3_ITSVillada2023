from ejer5 import search_matrix

def test_search_matrix():
    matrix1 = [
        [1, 2],
        [3, 4]
    ]
    assert search_matrix(matrix1, 2) == True
    assert search_matrix(matrix1, 4) == True
    assert search_matrix(matrix1, 5) == False

