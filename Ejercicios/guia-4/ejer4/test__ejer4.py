from ejer4 import calculate_statistics


def test_calculate_statistics():
    assert calculate_statistics([2, 4, 6, 8, 10]) == (6, 2.8284271247461903)
    assert calculate_statistics([1, 3, 5, 7, 9]) == (5, 2.8284271247461903)