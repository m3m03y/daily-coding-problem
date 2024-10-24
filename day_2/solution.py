"""
Solution for day 2 task
"""
def create_new_array_from_sums(original_arr: list) -> list:
    """
    Given an array of integers, return a new array 
    such that each element at index i of the new 
    array is the product of all the numbers in 
    the original array except the one at i.
    """
    new_arr = []

    for i in range(len(original_arr)):
        new_element = 1
        for idx, element in enumerate(original_arr):
            if i != idx:
                new_element *= element
        new_arr.append(new_element)
    return new_arr
