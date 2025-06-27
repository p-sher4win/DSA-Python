# Implementation
"""
1. Create a variable minValue = arr[0], which will store the first element in the array.
2. Go through each element in the array using a for loop.
3. Compare and check whether the current value store in minValue is less than the new element while looping, if yes then update the value store in minValue with the new smallest value.
4. Once the whole loop is over, the final value stored in minValue is the lowest element in the array.
"""

# Code
arr = [12, 55, 28, 94, 30, 444, 73, 5, 345, 98, 76]

minValue = arr[0]

for num in arr:
    if num < minValue:
        minValue = num

print(minValue)