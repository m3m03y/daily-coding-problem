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

    numbers_set = set()
    for number in numbers:
        rest = k - number
        if rest in numbers_set:
            return True
        numbers_set.add(number)
    return False
