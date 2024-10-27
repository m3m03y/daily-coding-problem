"""
Solution for day 4 task
"""

def find_missing_positive_intiger(original_arr: list) -> int:
    """
    Given an array of integers, find the first missing positive 
    integer in linear time and constant space. In other words, 
    find the lowest positive integer that does not exist in 
    the array. The array can contain duplicates and negative 
    numbers as well.
    """

    original_arr.sort()
    first_positive = 1
    for number in original_arr:
        if number < 0:
            continue
        if number > first_positive:
            break
        if number == first_positive:
            first_positive += 1

    return first_positive
