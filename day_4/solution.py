"""
Solution for day 4 task
"""

def find_missing_positive_intiger(nums: list) -> int:
    """
    Given an array of integers, find the first missing positive 
    integer in linear time and constant space. In other words, 
    find the lowest positive integer that does not exist in 
    the array. The array can contain duplicates and negative 
    numbers as well.
    """
    if len(nums) == 0:
        return 1

    for idx, _ in enumerate(nums):
        while (idx+1 != nums[idx] and
                0 < nums[idx] <= len(nums)):
            position = nums[idx]
            if nums[idx] == nums[position - 1]:
                break
            nums[idx], nums[position-1] = nums[position-1], nums[idx]

    for idx, number in enumerate(nums, 1):
        if number != idx:
            return idx

    return len(nums) + 1
