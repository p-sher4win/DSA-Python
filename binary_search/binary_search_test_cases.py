import warnings
warnings.filterwarnings("ignore", category=UserWarning)

from binary_search import *
from jovian.pythondsa import evaluate_test_case, evaluate_test_cases

from generic_binary_search import *

# Test cases
tests = []

# Test 0
# query occurs in the middle
test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

# locate_card(**test['input']) == test['output']
tests.append(test)

# Test 1
# query occurs in the middle
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

# Test 2
# query is the first element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# Test 3
# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# Test 4
# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})

# Test 5
# cards does not contain query
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# Test 6
# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# Test 7
# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# Test 8
# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

# for test in tests:
#     print(test)

# result = locate_card(test['input']['cards'], test['input']['query'])
# print(result)
# print(result == test['output'])

# evaluate_test_case(locate_card, tests[0])

# evaluate_test_cases(locate_card, tests)

large_test = {
    'input': {
        'cards': list(range(10000000, 0, -1)),
        'query': 2
    },
    'output': 9999998
}

# result, passed, runtime = evaluate_test_case(locate_card_linear, large_test, display=False)
# print(f"Result: {result}\nPassed: {passed}\nExecution Time: {runtime}ms\n\n")
#
# result, passed, runtime = evaluate_test_case(locate_card, large_test, display=False)
# print(f"Result: {result}\nPassed: {passed}\nExecution Time: {runtime}ms")


# Testing the Generic Binary Search Function
evaluate_test_cases(locate_card_bs, tests)