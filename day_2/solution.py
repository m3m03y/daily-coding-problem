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
    product_of_all = 1

    for element in original_arr:
        product_of_all *= element

    new_arr = []
    for element in original_arr:
        new_arr.append(product_of_all/element)
    return new_arr
