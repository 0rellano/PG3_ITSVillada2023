
def search_matrix(matrix: list[list[float]], target: int) -> bool:
    for row in matrix:
        if target in row:
            return True
    return False
