import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from jovian.pythondsa import evaluate_test_case, evaluate_test_cases
from bs_rotated_list import *

# Test cases listed
# Test 0
test = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}
test0 = test

# nums0 = test['input']['nums']
# output0 = test['output']
# result0 = count_rotation(nums0)
# print(result0, result0 == output0)
# evaluate_test_case(count_rotation, test)

# Test 1
# A list of size 8 rotated 5 times.
test1 = {
    'input': {
        'nums': [4, 5, 6, 7, 8, 1, 2, 3]
    },
    'output': 5
}

# Test 2
# A list that wasn't rotated at all.
test2 = {
    'input': {
        'nums': [11, 12, 15, 19]
    },
    'output': 0
}

# Test 3
# A list that was rotated just once.
test3 = {
    'input': {
        'nums': [10, -40, -32, 0]
    },
    'output': 1
}

# Test 4
# A list that was rotated n-1 times, where n is the size of the list.
test4 = {
    'input': {
        'nums': [2, 3, 4, 5, 6, 7, 8, 9, 1]
    },
    'output': 8
}

# Test 5
# A list that was rotated n times, where n is the size of the list
test5 = {
    'input': {
        'nums': [101, 202, 303, 404, 505]
    },
    'output': 0
}

# Test 6
# An empty list.
test6 = {
    'input': {
        'nums': []
    },
    'output': 0
}

# Test 7
# A list containing just one element.
test7 = {
    'input': {
        'nums': [19]
    },
    'output': 0
}

# All test cases
tests = [test0, test1, test2, test3, test4, test5, test6, test7]
# for test in tests:
#     print(test)

# evaluate_test_cases(count_rotation_linear, tests)

# evaluate_test_case(binary_count_rotation, test0)
# evaluate_test_cases(binary_count_rotation, tests)

# Test for complexity
large_test = {
    'input': {
        'nums': list(range(10000)) + list(range(10000))
    },
    'output': 10000
}

# print(large_test['input']['nums'])
# print(count_rotation_linear(large_test['input']['nums']))

result, passed, runtime = evaluate_test_case(count_rotation_linear, large_test, display=False)
print(f"Result: {result}\nPassed: {passed}\nExecution Time: {runtime}ms\n\n")

result, passed, runtime = evaluate_test_case(binary_count_rotation, large_test, display=False)
print(f"Result: {result}\nPassed: {passed}\nExecution Time: {runtime}ms")