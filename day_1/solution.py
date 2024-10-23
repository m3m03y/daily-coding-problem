"""
Solution for day 1 task
"""
def if_sum_from_list_eq_k(k: int, numbers: list):
    """
    Given a list of numbers and a number k, 
    return whether any two numbers from the list 
    add up to k.
    """
    if len(numbers) < 2:
        return False

    for idx, i in enumerate(numbers):
        if i > k:
            continue

        for j in numbers[idx+1:]:
            if i + j == k:
                return True
    return False
