"""Program to find the position of a given number in a list of numbers arranged in decreasing order. Also need to minimize the number of times the elements are accessed from the list."""

# Approach 1 to implement the function
# def locate_card(cards, query):
#     # Create a variable position with value 0
#     position = 0
#
#     # Set up a loop for repetition
#     while True:
#
#         # Check if element at the current position matches the query
#         if cards[position] == query:
#
#             # Answer found! Return and exit.
#             return position
#         position += 1
#
#         if position == len(cards):
#             return -1


# Approach 2: Linear Search, handle empty cards list, brute force
def locate_card_linear(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1


# Helper function for binary search
def test_location(cards, query, mid):
    mid_number = cards[mid]
    # print(f"middle_index: {mid}, middle_number: {mid_number}")

    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

# Approach 3: Binary Search
def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        # mid_number = cards[mid]
        result = test_location(cards, query, mid)

        # print(f"low: {lo}, high: {hi}, middle_index: {mid}, middle_number: {mid_number}")

        if result == 'right':
            lo = mid + 1
        elif result == 'left':
            hi = mid - 1
        elif result == 'found':
            return mid

    return -1