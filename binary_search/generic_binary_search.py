"""
1. Come up with a condition to determine whether the answer lies before, after or at a given position
2. Retrieve the midpoint and the middle element of the list.
3. If it is the answer, return the middle position as the answer.
4. If answer lies before it, repeat the search with the first half of the list
5. If the answer lies after it, repeat the search with the second half of the list.
"""

# Generic Binary Search Function
def binary_search(lo, hi , condition):
    while lo <= hi:
        mid = (hi + lo) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        if result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

def locate_card_bs(cards, query):

    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return  'right'

    return binary_search(0, len(cards) - 1, condition)