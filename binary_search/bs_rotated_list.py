import math

# Linear search algorithm
def count_rotation_linear(nums):

    # Declare variable position = 0
    position = 0

    # While value of position is less than the size of list
    while position < len(nums):

        # Check if position is 1 and the value at index position < value at index position-1
        if position > 0 and nums[position] < nums[position-1]:

            # Return position if check is true
            return position

        # Move to next position
        position += 1

    # Return zero for no rotations
    return 0


# Binary Search Algorithm
def binary_count_rotation(nums):
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = math.ceil((hi+lo)/2)
        mid_number = nums[mid]

        if mid > 0 and mid_number < nums[mid-1]:
            return mid

        elif mid_number > nums[hi]:
            lo = mid + 1
        else:
            hi = mid - 1

    return 0
