# First two Fibonacci numbers are 0 and 1, next fibonacci number is the sum of the previous two numbers

length = int(input("Enter number: "))

# prev_1 = 0
# prev_0 = 1
#
# print(prev_1)
# print(prev_0)

# Using a simple for loop
# for i in range(length):
#     next_num = prev_0 + prev_1
#     print(next_num)
#     prev_1 = prev_0
#     prev_0 = next_num


# Using Recursion
# count = 2
#
# def fibonacci(prev, prev1):
#     global count
#     if count <= length:
#         next_num = prev + prev1
#         print(next_num)
#         prev1 = prev
#         prev = next_num
#         count += 1
#         fibonacci(prev, prev1)
#     else:
#         return
#
# fibonacci(prev_0, prev_1)


# Finding the nth Fibonacci Number using Recursion

def f(n):
    if n <= 1:
        return n
    else:
        return f(n-1) + f(n-2)

print(f(length))