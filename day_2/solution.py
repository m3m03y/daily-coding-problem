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
    new_arr = [1 for _ in original_arr]
    sub_product = 1

    # calculate product of all elements to the left
    for idx, element in enumerate(original_arr):
        new_arr[idx] *= sub_product
        sub_product *= element

    sub_product = 1
    # calculcate product of all elements to the left
    # multiplied by product of all elements to the right
    for idx in range(len(original_arr) - 1, -1, -1):
        new_arr[idx] *= sub_product
        sub_product *= original_arr[idx]

    return new_arr
