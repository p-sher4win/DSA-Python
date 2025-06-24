# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given number.

from generic_binary_search import binary_search

# Function to find first position
def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            else:
                return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'

    return binary_search(0, len(nums)-1, condition)

# Function to find last position
def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return 'right'
            else:
                return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'

    return binary_search(0, len(nums)-1, condition)

def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)

# Sample test case (first = 6, last = 8)
nums = [1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9]
target = 7

print(first_and_last_position(nums, target))